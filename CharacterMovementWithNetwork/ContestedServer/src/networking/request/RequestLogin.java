package networking.request;

// Java Imports
import java.io.IOException;



// Custom Imports
//import core.GameServer;
import networking.response.ResponseLogin;
import utility.DataReader;

public class RequestLogin extends GameRequest {

    // Data
    private String username;
    private int type;
    private int faction;
    // Responses
    private ResponseLogin responseLogin;

    public RequestLogin() {
        responses.add(responseLogin = new ResponseLogin());
    }

    @Override
    public void parse() throws IOException {
        username = DataReader.readString(dataInput);
        type = DataReader.readInt(dataInput);
        faction = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseLogin.setUsername(username);
        responseLogin.setType(type);
        responseLogin.setFaction(faction);
        //
        client.getCharacter().setC_id((int)this.client.getId());
        //
        client.getCharacter().setName(username);
        client.getCharacter().setCtype(type);
        client.getCharacter().setTeamid(faction);
        
        client.getServer().addToActiveThreads(client);
        
        ResponseLogin[] responseNewPlayer = new ResponseLogin[client.getServer().getNumberOfCurrentThreads()];
        
        for(int i = 0; i < client.getServer().getNumberOfCurrentThreads(); i++)
        {
        	if(client.getId() != client.getServer().getActiveThreads().get(i).getId())
        	{
            	responses.add(responseNewPlayer[i] = new ResponseLogin());
           		responseNewPlayer[i].setUsername(client.getServer().getActiveThreads().get(i).getCharacter().getName());
           		responseNewPlayer[i].setType(client.getServer().getActiveThreads().get(i).getCharacter().getCtype());
           		responseNewPlayer[i].setFaction(client.getServer().getActiveThreads().get(i).getCharacter().getTeamid());
        	}
       			
        }
        //client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseLogin);
        
    }
}
