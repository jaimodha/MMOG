package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseSpawnGolem extends GameResponse {

	
	private int controlPointId;
	
	
     public byte[] temp ;
	
	 public ResponseSpawnGolem()
    {
    	responseCode = Constants.SMSG_SPAWN_GOLEM_NPC;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addInt32(controlPointId);
		 
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public int getControlPointId() {
		return controlPointId;
	}

	public void setControlPointId(int controlPointId) {
		this.controlPointId = controlPointId;
	}

	
	
	
}
