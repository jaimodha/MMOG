package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseShort;
import utility.DataReader;

public class RequestShort extends GameRequest {

    // Data
    private short number;
    // Responses
    private ResponseShort responseShort;

    public RequestShort() {
        responses.add(responseShort = new ResponseShort());
    }

    @Override
    public void parse() throws IOException {
        number = DataReader.readShort(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseShort.setNumber(number);
        
    }
}
