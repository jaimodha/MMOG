package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseCharacterAttack extends GameResponse {

	private String username;
    private int attackId;

    public ResponseCharacterAttack() {
        responseCode = Constants.SMSG_ATTACK;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        packet.addInt32(attackId);
        
        return packet.getBytes();
    }

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public int getAttackId() {
		return attackId;
	}

	public void setAttackId(int attackId) {
		this.attackId = attackId;
	}
}
