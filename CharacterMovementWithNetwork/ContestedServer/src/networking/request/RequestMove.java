package networking.request;

// Java Imports
import java.io.IOException;
// Custom Imports
import networking.response.ResponseCharacterMovement;
//import core.GameServer;
import utility.DataReader;

public class RequestMove extends GameRequest {

    // Data
    private float x;
    private float y;
    private float z;
    private float h;
    private int isMoving;
    
    // Responses
    private ResponseCharacterMovement responseMove;

    public RequestMove() {
        responses.add(responseMove = new ResponseCharacterMovement());
    }

    @Override
    public void parse() throws IOException {
        x = DataReader.readFloat(dataInput);
        y = DataReader.readFloat(dataInput);
        z = DataReader.readFloat(dataInput);
        h = DataReader.readFloat(dataInput);
        isMoving = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        client.getCharacter().setName(client.getCharacter().getName());
        client.getCharacter().setXpos(x);
        client.getCharacter().setYpos(y);
        client.getCharacter().setZpos(z);
        client.getCharacter().setH(h);
        client.getCharacter().setMovement(isMoving);
        responseMove.setCharacter(client.getCharacter());
        
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseMove);
        
    }
}
