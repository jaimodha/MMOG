package model;

public class ControlPoint {
	
	int cpId;
	int timer;
	int factionId;
	
	public ControlPoint(int cpId, int timer, int factionId)
	{
		this.cpId = cpId;
		this.timer = timer;
		this.factionId = factionId;
	}

	public int getCpId() {
		return cpId;
	}

	public void setCpId(int cpId) {
		this.cpId = cpId;
	}

	public int getTimer() {
		return timer;
	}

	public void setTimer(int timer) {
		this.timer = timer;
	}

	public int getFactionId() {
		return factionId;
	}

	public void setFactionId(int factionId) {
		this.factionId = factionId;
	}
	
}
