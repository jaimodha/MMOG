package networking.response;

import java.util.ArrayList;

import utility.GamePacket;
import metadata.Constants;
import model.Npc;

public class ResponseNpcMove extends GameResponse{
	
	private ArrayList<Npc> listOfNpc;
	
	public void setListOfNpc(ArrayList<Npc> listOfNpc) {
		this.listOfNpc = listOfNpc;
	}

	public ResponseNpcMove() {
        responseCode = Constants.SMSG_NPCMOVE;
    }
	
	public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        //packet.addInt32(12);
        //packet.addString("Success");
        
        for(Npc npc : listOfNpc){
        	packet.addInt32(npc.getNpc_id());
        	//System.out.println(npc.getNpc_id()+"  "+npc.getStatus()+"   "+npc.getTargetUsername());
        	packet.addString(npc.getStatus());
        	if(npc.getStatus().equals("stop")){
        		packet.addString(npc.getOldTarget());}
        		//npc.setStatus("none");}
        	else
        		packet.addString(npc.getTargetUsername());
        }
        
        return packet.getBytes();
    }

}
