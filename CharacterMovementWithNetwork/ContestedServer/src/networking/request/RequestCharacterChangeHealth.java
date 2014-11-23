package networking.request;

// Java Imports
import java.io.IOException;
// Custom Imports
import networking.response.ResponseCharacterChangeHealth;
//import core.GameServer;
import utility.DataReader;

public class RequestCharacterChangeHealth extends GameRequest {

    // Data
	private String username;
    private int healthChange;
    
    // Responses
    private ResponseCharacterChangeHealth responseHealth;

    public RequestCharacterChangeHealth() {
        responses.add(responseHealth = new ResponseCharacterChangeHealth());
    }

    @Override
    public void parse() throws IOException {
    	username = DataReader.readString(dataInput);
    	healthChange = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseHealth.setUsername(username);
    	responseHealth.setHealthChange(healthChange);
        
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseHealth);
        
    }
}
