package networking.response;

import metadata.Constants;
import model.UserModel;
import utility.GamePacket;

public class ResponseCharacterAttack extends GameResponse {


	
    private UserModel um;
	
	public byte[] temp ;
	
	 public ResponseCharacterAttack()
    {
    	responseCode = Constants.SMSG_ATTACK;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 String characterName = null;
		 int attackid = 0;
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 for(int i=0;i<um.getCharlist().size();i++)
		 {
			 if(um.getCharlist().get(i).isIsActive() == true)
			 {
				 characterName = um.getCharlist().get(i).getName();
				 attackid = um.getCharlist().get(i).getAttackId();
			 }
		 }
		 packet.addString(characterName);
		 packet.addInt32(attackid);
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public UserModel getUm() {
		return um;
	}

	public void setUm(UserModel um) {
		this.um = um;
	}

	
	

	

	
	
}
