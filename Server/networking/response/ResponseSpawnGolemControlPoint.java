package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseSpawnGolemControlPoint extends GameResponse {

	
	private int locationId;
	
	
     public byte[] temp ;
	
	 public ResponseSpawnGolemControlPoint()
    {
    	responseCode = Constants.SMSG_SPAWN_GOLEMCP;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addInt32(locationId);
		 
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public int getLocationId() {
		return locationId;
	}

	public void setLocationId(int locationId) {
		this.locationId = locationId;
	}

	
	
	

	

	
	
}
