package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseRemoveUser extends GameResponse {

	private String characterName;
	public byte[] temp ;
	
	 public ResponseRemoveUser()
    {
    	responseCode = Constants.SMSG_REMOVE_CHARACTER;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addString(characterName);
		 
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

	

	
	
}
