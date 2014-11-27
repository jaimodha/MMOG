package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseDestroyNPC extends GameResponse {

	
	private int npcId;
	
	
     public byte[] temp ;
	
	 public ResponseDestroyNPC()
    {
    	responseCode = Constants.SMSG_DESTROY_NPC;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addInt32(npcId);
		 
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public int getNpcId() {
		return npcId;
	}

	public void setNpcId(int npcId) {
		this.npcId = npcId;
	}

	
	
	
}
