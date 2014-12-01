package networking.request;

// Java Imports
import java.io.IOException;



// Custom Imports
//import core.GameServer;
import networking.response.ResponseLogin;
import utility.DataReader;

public class RequestLogin extends GameRequest {

    // Data
    private String name;
    private int factionId;
    // Responses
    private ResponseLogin responseLogin;

    public RequestLogin() {
        responses.add(responseLogin = new ResponseLogin());
    }

    @Override
    public void parse() throws IOException {
        name = DataReader.readString(dataInput);
        factionId = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseLogin.setName(name);
        responseLogin.setFactionId(factionId);
        client.getCharacter().setName(name);
        client.getCharacter().setFactionId(factionId);
        
        client.getServer().addToActiveThreads(client);
        
        ResponseLogin[] responseNewPlayer = new ResponseLogin[client.getServer().getNumberOfCurrentThreads()];
        
        for(int i = 0; i < client.getServer().getNumberOfCurrentThreads(); i++)
        {
        	if(client.getId() != client.getServer().getActiveThreads().get(i).getId())
        	{
            	responses.add(responseNewPlayer[i] = new ResponseLogin());
           		responseNewPlayer[i].setName(client.getServer().getActiveThreads().get(i).getCharacter().getName());
           		responseNewPlayer[i].setFactionId(client.getServer().getActiveThreads().get(i).getCharacter().getFactionId());
        	}
       			
        }
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseLogin);
        
    }
}
