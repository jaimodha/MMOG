package networking.response;

import utility.GamePacket;
import metadata.Constants;

public class ResponseStop extends GameResponse{

	private int id;
	
	public ResponseStop() {
        responseCode = Constants.SMSG_STOP;
    }
	
	@Override
	public byte[] constructResponseInBytes() {
		GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(id);
        return packet.getBytes();
	}

	public void setId(int id)
	{
		this.id = id;
	}
}
