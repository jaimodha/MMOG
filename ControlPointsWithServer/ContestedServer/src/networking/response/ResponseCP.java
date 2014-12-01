package networking.response;

// Custom Imports
import metadata.Constants;
import model.ControlPoint;
import utility.GamePacket;

public class ResponseCP extends GameResponse {

	private ControlPoint cp;

    public ResponseCP() {
        responseCode = Constants.SMSG_CONTROL_POINT_STATE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(cp.getCpId());
        packet.addInt32(cp.getTimer());
        packet.addInt32(cp.getFactionId());
        
        return packet.getBytes();
    }

	public ControlPoint getCP() {
		return cp;
	}

	public void setCP(ControlPoint cp) {
		this.cp = cp;
	}
}
