package networking.response;

import utility.GamePacket;

public class ResponseLogin extends GameResponse {

	private String message;
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		 packet.addString(message);
		 return packet.getBytes();
	 }

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	
}
