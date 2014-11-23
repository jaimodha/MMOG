package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;
import model.Player;
public class ResponseString extends GameResponse {

	private Player player;
    private String password;
    private String user_id;
    private int faction_id;

    public ResponseString() {
        responseCode = Constants.RAND_STRING;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(player.getUsername());
        packet.addInt32(player.getFactionId());
        packet.addString(player.getPassword());

        return packet.getBytes();
    }
    
	public void setFactionId(int faction_id) {
		this.faction_id = faction_id;
	}

	public void setPassword(String password) {
		this.password = password;
	}

    public void setPlayer(Player player) {
        this.player = player;
    }
}
