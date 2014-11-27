package model;

public class Npc {
	
	private int npc_id;
	private String targetUsername;
	private int health;
	private int team;
	private String status;
	
	public Npc() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	
	
	public Npc(int npc_id, String targetUsername, String status) {
		super();
		this.npc_id = npc_id;
		this.targetUsername = targetUsername;
		this.status = status;
	}



	public Npc(int npc_id, String targetUsername, int health, int team, String status) {
		super();
		this.npc_id = npc_id;
		this.targetUsername = targetUsername;
		this.health = health;
		this.team = team;
		this.status = status;
	}
	
	
	
	public String getStatus() {
		return status;
	}



	public void setStatus(String status) {
		this.status = status;
	}



	public int getNpc_id() {
		return npc_id;
	}
	public void setNpc_id(int npc_id) {
		this.npc_id = npc_id;
	}
	public String getTargetUsername() {
		return targetUsername;
	}
	public void setTargetUsername(String targetUsername) {
		this.targetUsername = targetUsername;
	}
	public int getHealth() {
		return health;
	}
	public void setHealth(int health) {
		this.health = health;
	}
	public int getTeam() {
		return team;
	}
	public void setTeam(int team) {
		this.team = team;
	}

}
