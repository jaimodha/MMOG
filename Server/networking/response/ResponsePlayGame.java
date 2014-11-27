package networking.response;

import utility.GamePacket;
import metadata.Constants;
import model.CharacterModel;
import model.UserModel;

public class ResponsePlayGame extends GameResponse {

	private int flag;
	public byte[] temp ;
	private UserModel user;
	
	
	public ResponsePlayGame()
	{
		responseCode = Constants.SMSG_PLAYGAME;
	}
	
	@Override
	public byte[] constructResponseInBytes() {
		// TODO Auto-generated method stub
		GamePacket packet = new GamePacket(responseCode);
		for(CharacterModel c : user.getCharlist())
		{
			if(c.isIsActive())
			{
				packet.addString(user.getUsername());
				packet.addString(c.getName());
				packet.addInt32(c.getCtype());
				packet.addInt32(c.getTeamid());
			
			}
		}
		return packet.getBytes();
	}

	public UserModel getUser() {
		return user;
	}

	public void setUser(UserModel user) {
		this.user = user;
	}
	
	

}
