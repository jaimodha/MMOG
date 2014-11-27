package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseShort extends GameResponse {

    private short number;

    public ResponseShort() {
        responseCode = Constants.RAND_SHORT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(number);
        
        return packet.getBytes();
    }
    
	public short getNumber() {
		return number;
	}

	public void setNumber(short number) {
		this.number = number;
	}
}
