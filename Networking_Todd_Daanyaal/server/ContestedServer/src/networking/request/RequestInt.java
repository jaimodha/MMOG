package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import utility.DataReader;

public class RequestInt extends GameRequest {

    // Data
    private int number;
    // Responses
    private ResponseInt responseInt;

    public RequestInt() {
        responses.add(responseInt = new ResponseInt());
    }

    @Override
    public void parse() throws IOException {
        number = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseInt.setNumber(number);
        
    }
}
