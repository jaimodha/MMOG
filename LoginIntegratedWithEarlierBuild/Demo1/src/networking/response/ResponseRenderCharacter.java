package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseRenderCharacter extends GameResponse {

	private String characterName;
	private int type;
	private int factionId;
	private float x;
	private float y;
	private float z;

	
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
		 packet.addInt32(type);
		 packet.addInt32(factionId);
		 packet.addFloat(x);
		 packet.addFloat(y);
		 packet.addFloat(z);
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

	public int getType() {
		return type;
	}

	public void setType(int type) {
		this.type = type;
	}

	
	
}
