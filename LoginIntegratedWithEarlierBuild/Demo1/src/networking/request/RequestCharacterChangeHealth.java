package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseCharacterChangeHealth;
import networking.response.ResponseCharacterCreation;

public class RequestCharacterChangeHealth extends GameRequest {

	private int healthChange;
	private ResponseCharacterChangeHealth res;
	
	public RequestCharacterChangeHealth()
	{
		responses.add(res = new ResponseCharacterChangeHealth());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		healthChange=DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		System.out.println(healthChange+"--1");
		for(int i=0;i<client.getUm().getCharlist().size();i++)
		{
			if(client.getUm().getCharlist().get(i).isIsActive())
			{
				healthChange = client.getUm().getCharlist().get(i).getHealth() + healthChange;
				client.getUm().getCharlist().get(i).setHealth(healthChange);
				System.out.println("@@@"+healthChange);
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
