package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseChangeResourcePoints extends GameResponse {

	
	private int factionId;
	private int resourceAmount;

	
	public byte[] temp ;
	
	 public ResponseChangeResourcePoints()
    {
    	responseCode = Constants.SMSG_RESOURCE;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addInt32(factionId);
		 packet.addInt32(resourceAmount);
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public int getFactionId() {
		return factionId;
	}

	public void setFactionId(int factionId) {
		this.factionId = factionId;
	}

	public int getResourceAmount() {
		return resourceAmount;
	}

	public void setResourceAmount(int resourceAmount) {
		this.resourceAmount = resourceAmount;
	}

	

	

	

	

	

	
	
}
