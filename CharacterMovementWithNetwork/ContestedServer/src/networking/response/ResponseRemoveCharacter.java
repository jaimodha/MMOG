package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseRemoveCharacter extends GameResponse {

    private String username;

    public ResponseRemoveCharacter() {
        responseCode = Constants.SMSG_REMOVE_CHARACTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        
        return packet.getBytes();
    }
    
	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}
}
