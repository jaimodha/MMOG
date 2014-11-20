package networking.response;

//Custom Imports
import metadata.Constants;
import model.Player;
import utility.GamePacket;

public class ResponseNewPlayer extends GameResponse{

    private Player player;

    public ResponseNewPlayer() {
        responseCode = Constants.SMSG_ADD;
    }
    
	@Override
	public byte[] constructResponseInBytes() {
		GamePacket packet = new GamePacket(responseCode);
		
		packet.addInt32(player.getPlayer_id());
        packet.addString(player.getUsername());
        packet.addFloat(player.getX());
        packet.addFloat(player.getY());
        packet.addFloat(player.getZ());
        packet.addFloat(player.getRotation());
        return packet.getBytes();
	}

	public void setPlayer(Player player) {
        this.player = player;
    }
}
