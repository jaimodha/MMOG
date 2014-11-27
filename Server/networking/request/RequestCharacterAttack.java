package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseCharacterAttack;
import networking.response.ResponseHeartbeat;

public class RequestCharacterAttack extends GameRequest{

	private int attackId;
	private ResponseCharacterAttack res;
	
	public RequestCharacterAttack()
	{
		 responses.add(res = new ResponseCharacterAttack());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		attackId=DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		String char_name=null;
		for(int i=0;i<client.getUm().getCharlist().size();i++)
		{
			if(client.getUm().getCharlist().get(i).isIsActive() == true)
			{
				client.getUm().getCharlist().get(i).setIsAttacking(true);
				char_name = client.getUm().getCharlist().get(i).getName();
				client.getUm().getCharlist().get(i).setAttackId(attackId);
			}
		}
		
		res.setUm(client.getUm());
		
	}

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return res.constructResponseInBytes();
	}

}
