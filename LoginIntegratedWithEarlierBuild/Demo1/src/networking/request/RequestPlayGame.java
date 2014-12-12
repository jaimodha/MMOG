package networking.request;

import java.io.IOException;

import core.Database;
import utility.DataReader;
import model.CharacterModel;
import model.UserModel;
import networking.response.ResponseAuth;
import networking.response.ResponseCharacterCreation;
import networking.response.ResponsePlayGame;

public class RequestPlayGame extends GameRequest{

	
	private int cr_id;
	private String cr_name;
	private int cr_type;
	private int cr_func;
	private ResponsePlayGame cr;
	Database db;
	
	public RequestPlayGame ()
	{
		responses.add(cr = new ResponsePlayGame());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		cr_id=DataReader.readInt(dataInput);
		System.out.println(cr_id+"---------");
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		
			for(int i=0;i<client.getUm().getCharlist().size();i++)
			{
				System.out.println(client.getUm().getCharlist().get(i).getC_id() +"-"+cr_id);
				if(client.getUm().getCharlist().get(i).getC_id()==cr_id)
				{
					client.getUm().getCharlist().get(i).setIsActive(true);
					break;
				}
			}
			
		    //cr.setFlag(0);
		
		
		cr.setUser(client.getUm());
		//client.getServer().setActivePlayer(client.getUm());
		client.getServer().addResponseForAllOnlinePlayers(client.getUm().getUserid(), cr);
		
		for(UserModel u:client.getServer().getActivePlayers() )
		{
			if(u.getUserid() != client.getUm().getUserid() )
			{
				ResponsePlayGame rp =  new ResponsePlayGame();
				rp.setUser(u);
				System.out.println("response for all user");
				client.getOutputStream().write(rp.constructResponseInBytes());
			}
		}
		
		
	}

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return cr.constructResponseInBytes();
	}

}
