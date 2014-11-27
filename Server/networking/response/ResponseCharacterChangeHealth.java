package networking.response;

import metadata.Constants;
import model.UserModel;
import utility.GamePacket;

public class ResponseCharacterChangeHealth extends GameResponse {

	private String characterName;
	private int healthChange;
	private UserModel um;

	
	public byte[] temp ;
	
	 public ResponseCharacterChangeHealth()
    {
    	responseCode = Constants.SMSG_HEALTH;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 for(int i=0;i<um.getCharlist().size();i++)
		 {
			 if(um.getCharlist().get(i).isIsActive() == true)
			 {
				 characterName = um.getCharlist().get(i).getName();
				 healthChange = um.getCharlist().get(i).getHealth();
			 }
		 }
		 System.out.println(characterName +"--"+healthChange );
		 packet.addString(characterName);
		 packet.addInt32(healthChange);
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

	public int getHealthChange() {
		return healthChange;
	}

	public void setHealthChange(int healthChange) {
		this.healthChange = healthChange;
	}

	public UserModel getUm() {
		return um;
	}

	public void setUm(UserModel um) {
		this.um = um;
	}

	

	

	
	
}
