package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseRenderCharacter extends GameResponse {

    private String username;
    private int type;
    private int faction;
    private float x;
    private float y;
    private float z;

    public ResponseRenderCharacter() {
        responseCode = Constants.SMSG_RENDER_CHARACTER;
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

	public float getX() {
		return x;
	}

	public void setX(float x) {
		this.x = x;
	}

	public float getY() {
		return y;
	}

	public void setY(float y) {
		this.y = y;
	}

	public float getZ() {
		return z;
	}

	public void setZ(float z) {
		this.z = z;
	}
}
