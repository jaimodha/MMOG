package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
import networking.response.ResponseCP;
import model.ControlPoint;

//import core.GameServer;
import utility.DataReader;

public class RequestCP extends GameRequest {

    // Data
    private int cpId;
    private int timer;
    private int factionId;
    
    // Responses
    private ResponseCP responseCP;

    public RequestCP() {
        responses.add(responseCP = new ResponseCP());
    }

    @Override
    public void parse() throws IOException {
        cpId = DataReader.readInt(dataInput);
        timer = DataReader.readInt(dataInput);
        factionId = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        ControlPoint cp = new ControlPoint(cpId, timer, factionId);
        responseCP.setCP(cp);
        
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseCP);
        
    }
}
