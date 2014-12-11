package networking.request;

import java.io.IOException;
import java.util.ArrayList;

import utility.DataReader;
import model.Npc;
import networking.response.ResponseCharacterChangeHealth;

public class RequestNpcAttack extends GameRequest {
	
	private int npcId;
	private int npcDamage;
	String str;

//private ResponseNpcAttack responseNpcAttack;
private ResponseCharacterChangeHealth responseNpcAttack;
	
	public RequestNpcAttack()
	{
		//responses.add(responseNpcAttack = new ResponseNpcAttack());
		responses.add(responseNpcAttack = new ResponseCharacterChangeHealth());
	}
	
	
	@Override
	public void parse() throws IOException {
		
		npcId = DataReader.readInt(dataInput);
		npcDamage = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		ArrayList<Npc> npcList = client.getServer().getNpcList();
		
		for(Npc npc : npcList)
			if(npc.getNpc_id()==npcId)
			{
				
				responseNpcAttack.setUsername(npc.getTargetUsername());
		    	responseNpcAttack.setHealthChange(npcDamage);
		        
		        client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseNpcAttack); 
		        /*
		        str = npc.getTargetUsername();
				//System.out.println(str);
				str = str+" has taken "+npcDamage+" Damage"+" from NPC"+npcId;
				//System.out.println(str);*/
				
			}
		
		//responseNpcAttack.setMsg(str);

	}

}
