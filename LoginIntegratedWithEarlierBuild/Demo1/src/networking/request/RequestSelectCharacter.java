package networking.request;

import java.io.IOException;

import utility.DataReader;
import model.CharacterModel;
import model.UserModel;
import networking.response.ResponseRenderCharacter;

public class RequestSelectCharacter extends GameRequest{

	private String username;
	private String charactername;
	private int charId;
	private int charType;
	private int charFaction;
	private int selection;
	private ResponseRenderCharacter res;
	
	public RequestSelectCharacter()
	{
		 responses.add(res = new ResponseRenderCharacter());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		username = DataReader.readString(dataInput);
		charactername = DataReader.readString(dataInput);
		charId = DataReader.readInt(dataInput);
		charType = DataReader.readInt(dataInput);
		charFaction = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		res.setCharacterName(charactername);
		res.setType(charType);
		res.setFactionId(charFaction);
		res.setX(0);
		res.setY(0);
		res.setZ(0);
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), res);
		for(UserModel user : client.getServer().getActivePlayers())
		{
			if(!user.equals(client.getUm()))
			{
				ResponseRenderCharacter addChar = new ResponseRenderCharacter();
				for(CharacterModel c : user.getCharlist())
				{
					if(c.isIsActive())
					{
						addChar.setCharacterName(c.getName());
						addChar.setType(c.getCtype());
						addChar.setFactionId(c.getTeamid());
						addChar.setX((float) c.getXpos());
						addChar.setY((float) c.getYpos());
						addChar.setZ((float) c.getZpos());
						client.addResponseForUpdate(addChar);
					}
				}
			}
		}
	}

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return null;
	}

}
