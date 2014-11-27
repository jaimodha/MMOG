package networking.response;

import metadata.Constants;
import model.CharacterModel;
import model.UserModel;
import utility.GamePacket;

public class ResponseCharacterMovement extends GameResponse {

	private String username;
	private float x;
	private float y;
	private float z;
	private float h;
	private int isMoving;
	private UserModel um;

	
	public byte[] temp ;
	
	 public ResponseCharacterMovement()
    {
    	responseCode = Constants.SMSG_MOVE;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 for(CharacterModel c : um.getCharlist())
			{
				if(c.isIsActive())
				{
					 packet.addString(username);
					 packet.addFloat((float)c.getXpos());
					 packet.addFloat((float)c.getYpos());
					 packet.addFloat((float)c.getZpos());
					 packet.addFloat((float)c.getH());
				}
			}
				
		
		
		 
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public float getX() {
		return x;
	}

	public void setX(float x) {
		this.x = x;
	}

	public float getY() {
		return y;
	}

	public void setY(float y) {
		this.y = y;
	}

	public float getZ() {
		return z;
	}

	public void setZ(float z) {
		this.z = z;
	}

	public float getH() {
		return h;
	}

	public void setH(float h) {
		this.h = h;
	}

	public int getIsMoving() {
		return isMoving;
	}

	public void setIsMoving(int isMoving) {
		this.isMoving = isMoving;
	}

	public UserModel getUm() {
		return um;
	}

	public void setUm(UserModel um) {
		this.um = um;
	}

	 

	
	
}
