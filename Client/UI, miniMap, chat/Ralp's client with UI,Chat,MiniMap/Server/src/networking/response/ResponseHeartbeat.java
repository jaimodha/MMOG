package networking.response;

import core.GameClient;
import metadata.Constants;
import utility.GamePacket;

public class ResponseHeartbeat extends GameResponse{
    
    public ResponseHeartbeat(){
        this.responseCode=Constants.SMSG_HEARTBEAT;
    }
    
    @Override
    public byte[] constructResponseInBytes() {
        //If clients get this response, it does nothing.
        GamePacket packet = new GamePacket(this.responseCode);
        packet.addShort16((short)0);
        return packet.getBytes();
    }
    
    @Override
    public String toString() {
    	String response = "=========In ResponseHeartbeat==========";
//        System.out.println("=========In ResponseHeartbeat==========");
//        System.out.println();
    	return response;
    }
}