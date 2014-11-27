package networking.response;

import metadata.Character;
import metadata.Constants;
import model.CharacterModel;
import model.UserModel;
import utility.GamePacket;

public class ResponseAuth extends GameResponse {

		private short status;
		private int flag;
	    private UserModel player;
        
	    public ResponseAuth() {
	        responseCode = Constants.SMSG_AUTH;
	    }

	    @Override
	    public byte[] constructResponseInBytes() {
	       
	    	GamePacket packet = new GamePacket(responseCode);
	       // packet.addShort16(status);
	       if(flag == 1)
	       {
	        packet.addInt32(flag);
	        packet.addInt32(player.getCharlist().size());
	        System.out.println(player.getCharlist().size());
	        for(CharacterModel ch: player.getCharlist())
	        {
	        	System.out.println(ch.getName());
	        	packet.addString(ch.getName());
	        	packet.addInt32(ch.getCtype());
	        	packet.addInt32(ch.getTeamid());
	        }
	        /*if (status == 0) {
	            packet.addInt32(player.getUserid());
	            packet.addString(player.getUsername());
	           
	        }*/
	       }
	       else
	       {
	    	   packet.addInt32(flag);
	    	   packet.addInt32(0);
	       }
	        return packet.getBytes();
	    }

	    public void setStatus(short status) {
	        this.status = status;
	    }

	    public void setPlayer(UserModel player) {
	        this.player = player;
	    }

		public int getFlag() {
			return flag;
		}

		public void setFlag(int flag) {
			this.flag = flag;
		}
	    
	    
	
}
