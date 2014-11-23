package networking.request;

// Java Imports
import java.io.IOException;
// Custom Imports
import networking.response.ResponseCharacterAttack;
//import core.GameServer;
import utility.DataReader;

public class RequestCharacterAttack extends GameRequest {

    // Data
    private int attackId;
    
    // Responses
    private ResponseCharacterAttack responseAttack;

    public RequestCharacterAttack() {
        responses.add(responseAttack = new ResponseCharacterAttack());
    }

    @Override
    public void parse() throws IOException {
        attackId = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseAttack.setUsername(client.getCharacter().getName());
        responseAttack.setAttackId(attackId);
        
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseAttack);
        
    }
}
