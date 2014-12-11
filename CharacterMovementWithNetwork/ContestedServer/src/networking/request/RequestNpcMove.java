package networking.request;

import java.io.IOException;
import java.util.ArrayList;

import model.Npc;
import networking.response.GameResponse;
import networking.response.ResponseNpcMove;
import utility.DataReader;


public class RequestNpcMove extends GameRequest{
	
	private int npcId1;
	private int npcId2;
	private String targetUser;
	private String action1;
	private String action2;
	
	private ResponseNpcMove responseNpcMove;
	
	public RequestNpcMove()
	{
		responses.add(responseNpcMove = new ResponseNpcMove());
	}
	
	@Override
	public void parse() throws IOException {
		targetUser = DataReader.readString(dataInput);
		npcId1 = DataReader.readInt(dataInput);
		//npcId2 = DataReader.readInt(dataInput);
		//action1 = DataReader.readString(dataInput);
		//action2 = DataReader.readString(dataInput);
		//System.out.println(npcId1 +"   "+npcId2+"    "+targetUser);
	}
	
	public void doBusiness() throws Exception {
		ArrayList<Npc> npcList = client.getServer().getNpcList();
		
		for(Npc npc : npcList)
		{
			//to check if chase started
			if(npc.getNpc_id()==npcId1)
			{
				npc.setTargetUsername(targetUser);
				npc.setChasing(true);
				npc.setFree(false);
				npc.setStatus("start");
				//npc.setOldTarget(targetUser);
			}
			
			//to check if chase stopped
			if(npcId1 == 0)
			{
				if(npc.isChasing())
					if(npc.getTargetUsername().equals(targetUser))
					{
						npc.setOldTarget(npc.getTargetUsername());
						npc.setTargetUsername("none");
						npc.setChasing(false);
						npc.setFree(true);
						npc.setStatus("stop");
					}	
			}
		}
					
		responseNpcMove.setListOfNpc(npcList);
		
        //System.out.println(targetUser);
        //System.out.println(npcId1);
        //System.out.println(npcId2);
    }

}
