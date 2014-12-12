package core;

// Java Imports
import java.io.IOException;
import java.net.Socket;
import java.net.ServerSocket;
import java.sql.SQLException;
import java.util.ArrayList;
//import java.util.ArrayList;
import java.util.HashMap;
//import java.util.List;






import java.util.List;

import org.omg.CORBA.Request;



// Custom Imports
import configuration.GameServerConf;
//import dataAccessLayer.DAO;
import metadata.GameRequestTable;
import model.CharacterModel;
import model.ControlPointModel;
import model.Npc;
import model.UserModel;
//import model.Player;
import networking.response.GameResponse;
import utility.ConfFileParser;

/**
 * The GameServer class serves as the main module that runs the server.
 * Incoming connection requests are established and redirected to be managed
 * by another class called the GameClient. Several specialized methods are also
 * stored here to perform other specific needs.
 */
public class GameServer {

    private static GameServer gameServer; // References GameServer instance
    private GameServerConf configuration; // Stores server config. variables
    private boolean ready = false; // Used to keep server looping
    private HashMap<Long, GameClient> activeThreads = new HashMap<Long, GameClient>(); // Stores active threads by thread ID
    private ArrayList<ControlPointModel> cplist;
    private HashMap<Integer, UserModel> activePlayers = new HashMap<Integer, UserModel>(); // Stores active players by player ID

    /**
     * Initialize the GameServer by setting up the request types and creating a
     * connection with the database.
     */
    public GameServer() {
        configuration = new GameServerConf();

        // Initialize the table with request codes and classes for static retrieval
        GameRequestTable.init();

        cplist = new ArrayList<ControlPointModel>();
        ControlPointModel cp1 = new ControlPointModel(1, -107.575, 0.6066, 0.490075,10, 0, 0, 0, 0,1);
        ControlPointModel cp2= new ControlPointModel(2, -100.575, -35.6066, 0.090075,10, 0, 0, 0,1,2);
        cplist.add(cp1);
        cplist.add(cp2);
        
        //CharacterModel cm = new CharacterModel();
        //ControlPointModel cp = new ControlPointModel();
        //NPCModel np = new NPCModel();
        //UserModel um = new UserModel();
         
        // Initialize database connection
       /* if (DAO.getInstance() == null) {
            System.err.println("Failed to connect to database.");
            System.exit(-1);
        }*/
    }

    
    
    public ArrayList<ControlPointModel> getCplist() {
		return cplist;
	}



	public void setCplist(ArrayList<ControlPointModel> cplist) {
		this.cplist = cplist;
	}



	/**
     * Configure the game server by reading values from the configuration file.
     */
    
    private void configure() {
        ConfFileParser confFileParser = new ConfFileParser("conf/gameServer.conf");
        configuration.setConfRecords(confFileParser.parse());
    }

    /**
     * Search for any other possible configuration variables and mark the server
     * ready to start.
     */
    private void getReady() {
        configure();
        ready = true;
    }

    /**
     * Check whether the server is prepared to run.
     * 
     * @return the ready status
     */
    private boolean isReady() {
        return ready;
    }

    /**
     * Run the game server by waiting for incoming connection requests.
     * Establishes each connection and stores it into a GameClient thread to
     * manage incoming and outgoing activity.
     */
    private void run() {
        ServerSocket listenSocket;
        int serverPort = configuration.getPortNumber();

        try {
            // Start to listen on the given port for incoming connections
            listenSocket = new ServerSocket(serverPort);
            System.out.println("Server has started on port: " + listenSocket.getLocalPort());
            System.out.println("Waiting for clients...");
            // Loop indefinitely to establish multiple connections
            while (true) {
                try {
                    // A client socket will represent a connection between the client and this server
                    Socket clientSocket = listenSocket.accept();
                    System.out.println("A Connection Established!");

                    // Create a thread to represent a client that holds the client socket
                    GameClient client = new GameClient(clientSocket, this);
                    // Run the thread
                    client.start();
                } catch (IOException e) {
                    System.out.println(e.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    /**
     * Get the GameClient thread for the player using the player ID.
     *
     * @param playerID holds the player ID
     * @return the GameClient thread
     */
    public GameClient getThreadByPlayerID(int playerID) {
        for (GameClient aClient : activeThreads.values()) {
            if (aClient.getUm().getUserid() == playerID) {
                return aClient;
            }
        }

        return null;
    }

    /**
     * Get the GameClient thread for the player using the username.
     *
     * @param username holds the username
     * @return the GameClient thread
     */
    /*public GameClient getThreadByPlayerUserName(String userName) {
        for (GameClient aClient : activeThreads.values()) {
            if (aClient.getPlayer().getUsername().equals(userName)) {
                return aClient;
            }
        }

        return null;
    }*/

    public int getNumberOfCurrentThreads() {
        return activeThreads.size();
    }

    public void addToActiveThreads(GameClient client) {
        activeThreads.put(client.getId(), client);
    }
    
    public List<UserModel> getActivePlayers() {
        return new ArrayList<UserModel>(activePlayers.values());
    }

    public UserModel getActivePlayer(int player_id) {
        return activePlayers.get(player_id);
    }

    public void setActivePlayer(UserModel player) {
        activePlayers.put(player.getUserid(), player);
    }
    
    public void removeActivePlayer(int player_id) {
        activePlayers.remove(player_id);
    }

    public void deletePlayerThreadOutOfActiveThreads(Long threadID) {
        activeThreads.remove(threadID);
    }

    /**
     * Push a pending response to a user's queue.
     * 
     * @param player_id holds the player ID
     * @param response is the instance containing the response information
     */
    /*public void addResponseForUser(int player_id, GameResponse response) {
        GameClient client = getThreadByPlayerID(player_id);

        if (client != null) {
            client.addResponseForUpdate(response);
        } else {
            System.out.println("In addResponseForUser--client is null");
        }
    }*/

    /**
     * Push a pending response to a user's queue.
     *
     * @param username holds the username
     * @param response is the instance containing the response information
     */
    /*public void addResponseForUser(String username, GameResponse response) {
        GameClient client = getThreadByPlayerUserName(username);

        if (client != null) {
            client.addResponseForUpdate(response);
        } else {
            System.out.println("In addResponseForUser--client is null");
        }
    }*/

    /**
     * Push a pending response to all users' queue except one user.
     * 
     * @param player_id holds the excluding player ID
     * @param response is the instance containing the response information
     */
    public void addResponseForAllOnlinePlayers(long player_id, GameResponse response) {
        for (GameClient client : activeThreads.values()) {
            if (client.getUm().getUserid() != player_id) {
            	System.out.println("cccc");
                client.addResponseForUpdate(response);
            }
        }
    }
    
    ///////////chat
    /**
     * get all the active client in the same team
     * @param factionId is the team they belongs to (red or blue)
     * @return
     */
	public List<GameClient> getThreadsByTeam(int factionId) {
    	 List<GameClient> clients =new ArrayList<GameClient>() ;
    	 for (GameClient client : activeThreads.values()) {
    		 //System.out.println("getThreadby team: "+client.getPlayer().getFactionId()+"....."+ factionId);
    		
    		 for(CharacterModel c :client.getUm().getCharlist())
    		 {
	    		 if(c.getTeamid() == factionId ){
	    				 clients.add(client);
	    		 }
    		 }
    	 }
    	 return clients;
    }
    /**
     * being called by ResponseChat, to send the message to their team player
     * @param client_id 
     * @param factionId
     * @param response contains response from ResponseChat
     */
    public void addResponseForAllPlayerInTheSameTeam(long client_id,int factionId, GameResponse response){
    	List<GameClient> clients = this.getThreadsByTeam(factionId);
    	if (clients != null) {
    		System.out.println("clients size: "+clients.size());
	    	for (GameClient client : clients) {
	    	
		    		 for(CharacterModel c :client.getUm().getCharlist())
		    		 {
			    		if (client_id !=client.getUm().getUserid()) {
			    		System.out.println("RES: "+c.getTeamid()+" "+client.getId()+" Send: "+response.toString());
			    		 client.addResponseForUpdate(response);
		    		 }
	    		 }
	    	}
    	}
    	else {
        System.out.println("clients is null");
    	}
    }
    ///////////
    

    public static GameServer getInstance() {
        return gameServer;
    }

    public static void main(String args[]) throws SQLException {
        gameServer = new GameServer();

        gameServer.getReady();

        if (gameServer.isReady()) {
            gameServer.run();
        }
    }
}
