package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseFloat extends GameResponse {

    private float number;

    public ResponseFloat() {
        responseCode = Constants.RAND_FLOAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addFloat(number);
        
        return packet.getBytes();
    }
    
	public float getNumber() {
		return number;
	}

	public void setNumber(float number) {
		this.number = number;
	}
}
