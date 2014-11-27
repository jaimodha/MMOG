package networking.response;

import metadata.Constants;
import model.ControlPointModel;
import utility.GamePacket;

public class ResponseControlPointCapture extends GameResponse {

	private int controlPointId;
	private int factionId;
	private ControlPointModel cp;

	
	public byte[] temp ;
	
	 public ResponseControlPointCapture()
    {
    	responseCode = Constants.SMSG_CONTROL_POINT_CAP;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 controlPointId = cp.getCountrolid();
		 factionId = cp.getOwner();
		 packet.addInt32(controlPointId);
		 packet.addInt32(factionId);
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public int getControlPointId() {
		return controlPointId;
	}

	public void setControlPointId(int controlPointId) {
		this.controlPointId = controlPointId;
	}

	public int getFactionId() {
		return factionId;
	}

	public void setFactionId(int factionId) {
		this.factionId = factionId;
	}

	public ControlPointModel getCp() {
		return cp;
	}

	public void setCp(ControlPointModel cp) {
		this.cp = cp;
	}

	

	
}
