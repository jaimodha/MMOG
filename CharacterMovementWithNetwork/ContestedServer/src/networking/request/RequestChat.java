package networking.request;

// Java Imports
import java.io.IOException;

import core.GameServer;

import metadata.Constants;
import networking.response.GameResponse;
// Custom Imports
//import core.GameServer;
import networking.response.ResponseChat;
import utility.DataReader;

public class RequestChat extends GameRequest {

    // Data
    private String message;
    private String username;

    // Responses
    private ResponseChat responseChat;

    public RequestChat() {
        responses.add(responseChat = new ResponseChat());
    }

    @Override
    public void parse() throws IOException {
    	username = DataReader.readString(dataInput);
        message = DataReader.readString(dataInput);
        
    }

    @Override
    public void doBusiness() throws Exception {
    	responseChat.setUsername(username);
        responseChat.setMessage(message);
        System.out.println("FID: "+client.getCharacter().getTeamid());
        this.client.getServer().addResponseForAllPlayerInTheSameTeam(client.getId(),client.getCharacter().getTeamid(), this.responseChat);
       
        
    }
}