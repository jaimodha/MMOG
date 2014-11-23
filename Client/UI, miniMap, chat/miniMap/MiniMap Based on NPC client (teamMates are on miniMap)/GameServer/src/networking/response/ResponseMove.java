package networking.response;

import metadata.Constants;
import model.Player;
import utility.GamePacket;

public class ResponseMove extends GameResponse{

	private Player player;

    public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }
    
	@Override
	public byte[] constructResponseInBytes() {
GamePacket packet = new GamePacket(responseCode);
		
		packet.addInt32(player.getPlayer_id());
        packet.addFloat(player.getX());
        packet.addFloat(player.getY());
        packet.addFloat(player.getZ());
        packet.addFloat(player.getRotation());
        return packet.getBytes();
	}

	public void setPlayer(Player player)
	{
		this.player = player;
	}
}
