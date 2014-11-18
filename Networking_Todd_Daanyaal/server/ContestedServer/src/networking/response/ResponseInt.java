package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseInt extends GameResponse {

    private int number;

    public ResponseInt() {
        responseCode = Constants.RAND_INT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(number);
        
        return packet.getBytes();
    }
    
	public int getNumber() {
		return number;
	}

	public void setNumber(int number) {
		this.number = number;
	}
}
