package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseGolemPiece extends GameResponse {

	
	private int factionId;
	
	
     public byte[] temp ;
	
	 public ResponseGolemPiece()
    {
    	responseCode = Constants.SMSG_GOLEM_PIECE;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addInt32(factionId);
		 
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

	
	
}
