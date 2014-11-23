package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
import networking.response.GameResponse;

/**
 * The RequestHeartbeat class is mainly used to release all pending responses
 * the client. Also used to keep the connection alive.
 */
public class RequestHeartbeat extends GameRequest {

    public RequestHeartbeat() {
    }

    @Override
    public void parse() throws IOException {
    }

    @Override
    public void doBusiness() throws Exception {
        for (GameResponse response : client.getUpdates()) {
            try {
                client.getOutputStream().write(response.constructResponseInBytes());
            } catch (IOException ex) {
                System.err.println(ex.getMessage());
            }
        }
        client.clearUpdateBuffer();
    }
}
