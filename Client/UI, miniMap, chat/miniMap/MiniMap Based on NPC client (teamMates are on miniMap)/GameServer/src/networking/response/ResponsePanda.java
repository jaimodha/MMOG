package networking.response;

import utility.GamePacket;
import metadata.Constants;
import model.Panda;

public class ResponsePanda  extends GameResponse{

	private Panda panda;
	
	public ResponsePanda()
	{
		responseCode = Constants.SMSG_PANDA;
	}
	@Override
	public byte[] constructResponseInBytes() {
		GamePacket packet = new GamePacket(responseCode);
        packet.addFloat(panda.getX());
        packet.addFloat(panda.getY());
        packet.addFloat(panda.getRotation());
        return packet.getBytes();
	}

	public void setPanda(Panda panda)
	{
		this.panda = panda;
	}
}
