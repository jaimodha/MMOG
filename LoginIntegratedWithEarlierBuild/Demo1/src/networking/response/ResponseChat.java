package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseChat extends GameResponse {

	private String username;
	private String message;

	
	public byte[] temp ;
	
	 public ResponseChat()
    {
    	responseCode = Constants.SMSG_CHAT;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 
		 packet.addString(username);
		 packet.addString(message);
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	 public String getUsername() {
			return username;
		}

		public void setUsername(String username) {
			this.username = username;
		}

		
		public String getMessage() {
			return message;
		}

		public void setMessage(String message) {
			this.message = message;
		}

	
	
}
