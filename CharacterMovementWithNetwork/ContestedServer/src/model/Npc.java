package model;

public class Npc {
	
	private int npc_id;
	private String targetUsername;
	private String oldTarget;
	private int health;
	private int team;
	private String status;
	private boolean isChasing;
	private boolean isAttacking;
	private boolean isFree;
	private boolean isDead;
	
	public Npc() {
		super();
		this.isDead = false;
		// TODO Auto-generated constructor stub
	}
	
	
	
	public Npc(int npc_id, String targetUsername, String status) {
		super();
		this.npc_id = npc_id;
		this.targetUsername = targetUsername;
		this.status = status;
		this.isDead = false;
	}



	public Npc(int npc_id, String targetUsername, int health, int team, String status) {
		super();
		this.npc_id = npc_id;
		this.targetUsername = targetUsername;
		this.health = health;
		this.team = team;
		this.status = status;
		this.isDead = false;
	}
	
	
	
	
	public boolean isDead() {
		return isDead;
	}



	public void setDead(boolean isDead) {
		this.isDead = isDead;
	}



	public String getOldTarget() {
		return oldTarget;
	}



	public void setOldTarget(String oldTarget) {
		this.oldTarget = oldTarget;
	}



	public String getStatus() {
		return status;
	}



	public void setStatus(String status) {
		this.status = status;
	}


	
	

	public boolean isChasing() {
		return isChasing;
	}



	public void setChasing(boolean isChasing) {
		this.isChasing = isChasing;
	}



	public boolean isAttacking() {
		return isAttacking;
	}



	public void setAttacking(boolean isAttacking) {
		this.isAttacking = isAttacking;
	}



	public boolean isFree() {
		return isFree;
	}



	public void setFree(boolean isFree) {
		this.isFree = isFree;
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
