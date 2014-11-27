package networking.request;

import java.io.IOException;
import java.util.ArrayList;

import core.Database;
import utility.DataReader;
import model.CharacterModel;
import model.UserList;
import model.UserModel;
import networking.response.ResponseAuth;
import networking.response.ResponseCharacterCreation;
import networking.response.ResponseLogin;

public class RequestCharacterCreation extends GameRequest{
	private String cr_name;
	private int cr_type;
	private int cr_func;
	private ResponseCharacterCreation cr;
	Database db = new Database();
	
	public  RequestCharacterCreation() {
		responses.add(cr = new ResponseCharacterCreation());
	}
	
	@Override
	public void parse() throws IOException {
		
		cr_name=DataReader.readString(dataInput);
		cr_type=DataReader.readInt(dataInput);
		cr_func=DataReader.readInt(dataInput);
		System.out.println(cr_type+"--"+cr_name+"--"+cr_func);
	}

	@Override
	public void doBusiness() throws Exception {
		
		if(db.CreateCharacter(cr_type, cr_name,client.getUm().getUsername(), cr_func))
		{
			 cr.setFlag(1);
			 /////
			CharacterModel ch = new CharacterModel(cr_type,cr_func,cr_name,true); 
			client.getUm().getCharlist().add(ch);
         	/////
		}
		else
		{
			for(int i=0;i<client.getUm().getCharlist().size();i++)
			{
				if(client.getUm().getCharlist().get(i).getName().equals(cr_name))
				{
					client.getUm().getCharlist().get(i).setIsActive(true);
					break;
				}
			}
			
		    cr.setFlag(0);
		}
		
	}

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return cr.constructResponseInBytes();
	}

}
