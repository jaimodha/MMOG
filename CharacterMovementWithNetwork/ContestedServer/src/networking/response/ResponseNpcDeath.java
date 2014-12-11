package networking.response;

import java.util.ArrayList;

import utility.GamePacket;
import metadata.Constants;
import model.Npc;

public class ResponseNpcDeath extends GameResponse {

	private int cpId;
	
	
    public ResponseNpcDeath() {
        responseCode = Constants.SMSG_NPCDEATH;
    }
    
	public void setcpId(int id) {
		this.cpId = id;
	}
	
	
	
	public byte[] constructResponseInBytes() {
		 GamePacket packet = new GamePacket(responseCode);
		 packet.addInt32(cpId);
		 System.out.println("Response Sent"+cpId);


		 
		 
		 return packet.getBytes();
	}

}
