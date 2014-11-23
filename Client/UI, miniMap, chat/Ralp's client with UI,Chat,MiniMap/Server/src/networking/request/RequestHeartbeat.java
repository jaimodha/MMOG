package networking.request;


import java.io.IOException;
import java.util.List;

import networking.response.GameResponse;
import networking.response.ResponseHeartbeat;


public class RequestHeartbeat extends GameRequest {

    private ResponseHeartbeat response;

    public RequestHeartbeat() {
        this.response = new ResponseHeartbeat();
    }

    @Override
    public void parse() throws IOException {
        //Do nothing here.
    }

    @Override
    public void doBusiness() {
        synchronized (this.client) {
            for (GameResponse response : this.client.getUpdates()) {
                try {
                	System.out.println("RequestHeartbeat: "+response.toString());
                    this.client.getOutputStream().write(response.constructResponseInBytes());
                    
                } catch (IOException ex) {
                }
            }
           
            this.client.clearUpdateBuffer();
            
            
        }
      
    }

    
 }

