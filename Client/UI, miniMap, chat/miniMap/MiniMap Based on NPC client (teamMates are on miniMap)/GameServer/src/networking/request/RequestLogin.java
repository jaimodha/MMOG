package networking.request;

//Java Imports
import java.io.IOException;


//Custom Imports
import core.GameClient;
import core.GameServer;
import dataAccessLayer.PlayerDAO;
import model.Player;
//import networking.response.ResponseCreateEnv;
import networking.response.ResponseLogin;
import networking.response.ResponseNewPlayer;
import utility.DataReader;

public class RequestLogin extends GameRequest{

	//Data
	private String username;
	private String password;
	//Responses
	private ResponseLogin responseLogin;
	//private ResponseCreateEnv responseCreateEnv;
	
	public RequestLogin() {
        responses.add(responseLogin = new ResponseLogin());
        //responses.add(responseCreateEnv = new ResponseCreateEnv());
    }
	
	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput).trim();
        password = DataReader.readString(dataInput).trim();
	}

	@Override
	public void doBusiness() throws Exception {
		System.out.println("User '" + username + "' is connecting...");

        Player player = null;
        
        player = PlayerDAO.getAccount(username, password);
        if (player == null) {
            responseLogin.setStatus((short) 1); // User info is incorrect
            System.out.println("User '" + username + "' has failed to log in.");
        } else {
            // Prevent consecutive login attempts
            if (client.getPlayer() == null || player.getPlayer_id() != client.getPlayer().getPlayer_id()) {
                GameClient thread = client.getServer().getThreadByPlayerID(player.getPlayer_id());
                // If account is already in use, remove and disconnect the client
                if (thread != null) {
                    responseLogin.setStatus((short) 2); // Account is in use
                    thread.stopClient();
                    System.out.println("User '" + username + "' account is already in use.");
                } else {
                    // Continue with the login process
                    GameServer.getInstance().setActivePlayer(player);
                    player.setClient(client);

                    // Pass Player reference into thread
                    client.setPlayer(player);
                    // Keep track of the new client thread
                    client.getServer().addToActiveThreads(client);
                    // Set response information
                    responseLogin.setStatus((short) 0); // Login is a success
                    responseLogin.setPlayer(player);
                    
                    //send all players information to new client
                    ResponseNewPlayer[] responseNewPlayer = new ResponseNewPlayer[client.getServer().getActivePlayers().size()];
                    
                    for(int i = 0; i < client.getServer().getActivePlayers().size(); i++)
                    {
                    	if(client.getPlayer().getPlayer_id() != client.getServer().getActivePlayers().get(i).getPlayer_id())
                    	{
	                    	responses.add(responseNewPlayer[i] = new ResponseNewPlayer());
	                   		responseNewPlayer[i].setPlayer(client.getServer().getActivePlayers().get(i));	
                    	}
                   			
                    }
                    
                    //notify other players of new player
                    ResponseNewPlayer responseAddSelf = new ResponseNewPlayer();
                    responseAddSelf.setPlayer(player);
                    client.getServer().addResponseForAllOnlinePlayers(client.getPlayer().getPlayer_id(), responseAddSelf);

                    System.out.println("User '" + player.getUsername() + "' has successfully logged in.");
                }
            } else {
                responseLogin.setStatus((short) 4); // Consecutive logins
            }
        }
	}
	
}
