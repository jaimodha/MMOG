package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseLogin extends GameResponse {

    private String username;
    private int type;
    private int faction;

    public ResponseLogin() {
        responseCode = Constants.SMSG_AUTH;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        packet.addInt32(type);
        packet.addInt32(faction);
        
        return packet.getBytes();
    }
    
	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public int getType() {
		return type;
	}

	public void setType(int type) {
		this.type = type;
	}

	public int getFaction() {
		return faction;
	}

	public void setFaction(int faction) {
		this.faction = faction;
	}
}
