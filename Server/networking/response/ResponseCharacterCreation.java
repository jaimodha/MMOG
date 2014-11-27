package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseCharacterCreation extends GameResponse {

	private int flag;
	public byte[] temp ;
	
	

	public ResponseCharacterCreation()
    {
    	responseCode = Constants.SMSG_CREATE_CHARACTER;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 System.out.println(responseCode);
		 GamePacket packet=new GamePacket(responseCode);
		// System.out.println(responseCode);
		 //System.out.println(message);
		 
		//packet.addInt32(cr_func);
		//packet.addString(cr_name.trim());
		//packet.addString(cr_type.trim());
		//System.out.println(cr_func+"  "+cr_name);
		 System.out.println(flag+"-------");
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
