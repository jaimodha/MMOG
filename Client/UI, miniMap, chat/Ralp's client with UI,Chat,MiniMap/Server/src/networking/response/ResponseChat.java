package networking.response;

// Custom Imports
import java.util.LinkedList;
import java.util.Queue;

import core.GameServer;
import model.Player;
import metadata.Constants;
import utility.GamePacket;

public class ResponseChat extends GameResponse {

    private String message;
    private String username;
    
    public ResponseChat() {
        responseCode = Constants.SMSG_CHAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        packet.addString(message);
        
        return packet.getBytes();
    }
    
	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	
	@Override
    public String toString() {
		return username+">>"+message;
		
	}
}
