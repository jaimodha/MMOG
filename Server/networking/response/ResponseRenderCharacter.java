package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseRenderCharacter extends GameResponse {

	private String characterName;
	private int factionId;
	

	
	public byte[] temp ;
	
	 public ResponseRenderCharacter()
    {
    	responseCode = Constants.SMSG_RENDER_CHARACTER;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addString(characterName);
		 packet.addInt32(factionId);
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public String getCharacterName() {
		return characterName;
	}

	public void setCharacterName(String characterName) {
		this.characterName = characterName;
	}

	public int getFactionId() {
		return factionId;
	}

	public void setFactionId(int factionId) {
		this.factionId = factionId;
	}

	
	
}
