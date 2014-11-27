package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseRegistration extends GameResponse {

	private int flag;
	public byte[] temp ;
	
	 public ResponseRegistration()
    {
    	responseCode = Constants.SMSG_REGISTER;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		// System.out.println(responseCode);
		 //System.out.println(message);
		
		 packet.addInt32(flag);
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public int getFlag() {
		return flag;
	}

	public void setFlag(int flag) {
		this.flag = flag;
	}

	
	
}
