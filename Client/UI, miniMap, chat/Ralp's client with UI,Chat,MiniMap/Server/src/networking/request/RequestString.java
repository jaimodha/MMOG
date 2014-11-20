package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseString;
import utility.DataReader;
import model.Player;

public class RequestString extends GameRequest {

    // Data
	
    private String user_id;
    private String password;
    private int factionId;
    // Responses
    private ResponseString responseString;

    public RequestString() {
        responses.add(responseString = new ResponseString());
    }

    @Override
    public void parse() throws IOException {
    	user_id = DataReader.readString(dataInput);
    	factionId = DataReader.readInt(dataInput);
        password = DataReader.readString(dataInput);
        
    }

	@Override
    public void doBusiness() throws Exception {
    	System.out.println("User '" + user_id + "' is connecting...");
    	Player player = new Player();
    	player.setID((int)this.client.getId());
    	player.setClient(this.client);
    	player.setUsername(user_id);
    	player.setPassword(password);
    	player.setFactionId(factionId);
    	//System.out.println("-------RequestString---facid: "+factionId);
    	client.setPlayer(player);
    	client.getServer().addToActiveThreads(this.client);
    	
        responseString.setPlayer(player);
        
        
    }
}
