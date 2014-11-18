package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseFloat;
import utility.DataReader;

public class RequestFloat extends GameRequest {

    // Data
    private float number;
    // Responses
    private ResponseFloat responseFloat;

    public RequestFloat() {
        responses.add(responseFloat = new ResponseFloat());
    }

    @Override
    public void parse() throws IOException {
        number = DataReader.readFloat(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        responseFloat.setNumber(number);
    }
}
