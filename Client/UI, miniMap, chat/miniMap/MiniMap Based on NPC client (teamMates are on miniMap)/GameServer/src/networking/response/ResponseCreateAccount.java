package networking.response;

import utility.GamePacket;
import metadata.Constants;

public class ResponseCreateAccount extends GameResponse{

	private short status;
	
	public ResponseCreateAccount() {
        responseCode = Constants.SMSG_CREATE_ACCOUNT;
    }
	
	public void setStatus(short status)
	{
		this.status = status;
	}
	
	@Override
	public byte[] constructResponseInBytes() {
		GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        return packet.getBytes();
	}

}
