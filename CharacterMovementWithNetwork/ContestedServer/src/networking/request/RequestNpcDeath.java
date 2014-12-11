package networking.request;

import java.io.IOException;
import java.util.ArrayList;

import model.Npc;
import networking.response.ResponseNpcDeath;
import utility.DataReader;

public class RequestNpcDeath extends GameRequest {
	
	int cpId;
	//String npcStatus;
	
private ResponseNpcDeath responseNpcDeath;	
	
	public RequestNpcDeath()
	{
		//responses.add(responseNpcAttack = new ResponseNpcAttack());
		responses.add(responseNpcDeath = new ResponseNpcDeath());
	}
	
	
	@Override
	public void parse() throws IOException {
		
		cpId = DataReader.readInt(dataInput);
		//npcStatus = DataReader.readString(dataInput);
		System.out.println(cpId);
	}

	@Override
	public void doBusiness() throws Exception {

		
		responseNpcDeath.setcpId(cpId);
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseNpcDeath);

	}


}
