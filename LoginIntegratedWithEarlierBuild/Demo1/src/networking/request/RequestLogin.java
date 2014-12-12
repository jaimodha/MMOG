package networking.request;

import java.io.IOException;
import java.util.ArrayList;

import core.Database;
import core.GameClient;
import core.GameServer;
import utility.DataReader;
import networking.response.ResponseAuth;
import networking.response.ResponseLogin;
import metadata.Constants;
import model.CharacterModel;
import model.UserList;
import model.UserModel;

public class RequestLogin extends GameRequest{

    public static String username;
	private String password;
	private ResponseAuth res;
	boolean en = false;
	
	Database db = new Database();
	
	public RequestLogin()
	{
		 responses.add(res = new ResponseAuth());
	}
	 
	
	
	 public  void parse() throws IOException
	 {
		 username = DataReader.readString(dataInput);
	     password = DataReader.readString(dataInput);
		    
		 
	 }
	 public void doBusiness() throws Exception
	 {
		 // if login is valid
			if(!en)
			{
		    boolean rs = db.ValidateUser(username, password);
		    if(rs)
		    {
		    	
		    	UserModel um = db.getUserbyUsername(username); 
		    	
		    	if (client.getUm() == null || um.getUserid() != client.getUm().getUserid()) {
	                GameClient thread = client.getServer().getThreadByPlayerID(um.getUserid());
	                // If account is already in use, remove and disconnect the client
	                if (thread != null) {
	                    res.setStatus((short) 2); // Account is in use
	                    thread.stopClient();
	                    System.out.println("User '" + username + "' account is already in use.");
	                    //res.setFlag(0);
	                    res.setStatus((short)0);
	                } else {
	                    // Continue with the login process
	                    GameServer.getInstance().setActivePlayer(um);
	                    //um.setClient(client);
                         um.setCharlist(db.getCharacterfromUser(username));
                         //System.out.println(um.getCharlist().size()+"-------------");
	                    // Pass Player reference into thread
	                    client.setUm(um);
	                    // Keep track of the new client thread
	                    client.getServer().addToActiveThreads(client);
	                    // Set response information
	                    client.getServer().setActivePlayer(um);
	                    res.setStatus((short) 0); // Login is a success
	                    res.setPlayer(um);
	                    System.out.println("++++++");
	                 
	                }
	                res.setStatus((short)1);
	                res.setFlag(1);
	            }
	                
		    	}
		    	else 
		    	{
		    		res.setStatus((short)0);
	                //res.setStatus((short) 4); // Consecutive logins
	                res.setFlag(0);
	           	}
		    en =true;
			}
		    	
	//	    }
		  
	 }
	 public byte[] respond() 
	 {
		 return res.constructResponseInBytes();
	 }
	
}
