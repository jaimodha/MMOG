package networking.response;

import java.util.ArrayList;

import metadata.Constants;
import model.ControlPointModel;
import utility.GamePacket;

public class ResponseControlPointState extends GameResponse {

	private int controlPointId;
	private int controlPointState;
	private ControlPointModel cp;

	
	public byte[] temp ;
	
	 public ResponseControlPointState()
    {
    	responseCode = Constants.SMSG_CONTROL_POINT_STATE;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 GamePacket packet=new GamePacket(responseCode);
		
		 
		 //**for test
		 // System.out.println(responseCode);
		 //System.out.println(message);
		 //*****
		 controlPointId = cp.getCountrolid();
		 packet.addInt32(controlPointId);
		 packet.addInt32(controlPointState);
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

	public int getControlPointState() {
		return controlPointState;
	}

	public void setControlPointState(int controlPointState) {
		this.controlPointState = controlPointState;
	}

	public ControlPointModel getCp() {
		return cp;
	}

	public void setCp(ControlPointModel cp) {
		this.cp = cp;
	}

	

	
}
