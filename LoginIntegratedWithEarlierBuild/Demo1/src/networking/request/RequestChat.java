package networking.request;

import java.io.IOException;

import model.CharacterModel;
import networking.response.ResponseChat;
import utility.DataReader;

public class RequestChat extends GameRequest{


    // Data
    private String message;
    private String username;
    private int teamid;

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
        for(CharacterModel c :client.getUm().getCharlist())
		{
        	if(c.getUsername() == username)
        	{
        		teamid = c.getTeamid();
        	}
        }
        this.client.getServer().addResponseForAllPlayerInTheSameTeam(client.getId(),teamid, this.responseChat);
       
        
    }

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return responseChat.constructResponseInBytes();
	}

}
