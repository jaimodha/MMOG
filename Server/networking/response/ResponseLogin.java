package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseLogin extends GameResponse {

	private String message;
	public byte[] temp ;
	
	 public ResponseLogin()
    {
    	responseCode = Constants.SMSG_AUTH;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		 System.out.println(responseCode);
		 System.out.println(message);
		// packet.addInt32(responseCode);
		 packet.addString(message);
		 temp = packet.getBytes();
		 System.out.println(temp+"----");
		 return temp;
	 }

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	
}
