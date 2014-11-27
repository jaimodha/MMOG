package networking.response;

import metadata.Constants;
import model.UserModel;
import utility.GamePacket;

public class ResponseLogout extends GameResponse {

	
	public byte[] temp ;
	private UserModel um;
	
	 public ResponseLogout()
    {
    	responseCode = Constants.SMSG_DISCONNECT;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		// System.out.println(responseCode);
		 //System.out.println(message);
		
		 packet.addInt32(um.getUserid());
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public UserModel getUm() {
		return um;
	}

	public void setUm(UserModel um) {
		this.um = um;
	}

	
	
}
