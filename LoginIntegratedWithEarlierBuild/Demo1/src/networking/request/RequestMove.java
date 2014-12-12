package networking.request;

import java.io.IOException;

import utility.DataReader;
import model.UserList;
import model.UserModel;
import networking.response.ResponseCharacterMovement;
import networking.response.ResponsePlayGame;
import networking.response.ResponseRegistration;

public class RequestMove extends GameRequest{

	
	private float x;
	private float y;
	private float z;
	private float h;
	private int isMoving;
	
	private ResponseCharacterMovement res;
	
	public RequestMove()
	{
		responses.add(res = new ResponseCharacterMovement());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		
		x = DataReader.readFloat(dataInput);
		y = DataReader.readFloat(dataInput);
		z = DataReader.readFloat(dataInput);
		h = DataReader.readFloat(dataInput);
		isMoving = DataReader.readInt(dataInput);
		
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		for(int i=0;i<client.getUm().getCharlist().size();i++)
		{
			if(client.getUm().getCharlist().get(i).isIsActive() == true)
			{
				client.getUm().getCharlist().get(i).setXpos(x);
				client.getUm().getCharlist().get(i).setYpos(y);
				client.getUm().getCharlist().get(i).setZpos(z);
				client.getUm().getCharlist().get(i).setH(h);
				res.setCharacter(client.getUm().getCharlist().get(i));
			}
		}
		
		//client.getServer().setActivePlayer(client.getUm());
		client.getServer().addResponseForAllOnlinePlayers(client.getUm().getUserid(), res);
		//remove something. keyword
	}

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return res.constructResponseInBytes();
	}

}
