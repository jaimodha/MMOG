package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseSpawnGuards extends GameResponse {

	
	private int controlPointId;
	private int factionId;
	private int guardId;
	

	
	public byte[] temp ;
	
	 public ResponseSpawnGuards()
    {
    	responseCode = Constants.SMSG_SPAWN_GUARDS;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addInt32(controlPointId);
		 packet.addInt32(factionId);
		 packet.addInt32(guardId);
		 
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

	public int getFactionId() {
		return factionId;
	}

	public void setFactionId(int factionId) {
		this.factionId = factionId;
	}

	public int getGuardId() {
		return guardId;
	}

	public void setGuardId(int guardId) {
		this.guardId = guardId;
	}

	
	

	

	

	

	

	
	
}
