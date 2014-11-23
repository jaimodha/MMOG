package model;

import java.util.ArrayList;

public class CharacterModel {
	
	String username;
	int c_id;
	String name;
	int ctype;
	int rewardpoint;
 	int hitpoint;
	int movementspeed;
	int skill;
	float xpos;
	float ypos;
	float zpos;
	float h;
	int teamid;
	int movement;
	boolean IsAttacking;
	
	ArrayList<CharacterModel> cmlist;
	
	public CharacterModel()
	{
		cmlist = new ArrayList<CharacterModel>();
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public int getC_id() {
		return c_id;
	}

	public void setC_id(int c_id) {
		this.c_id = c_id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getCtype() {
		return ctype;
	}

	public void setCtype(int ctype) {
		this.ctype = ctype;
	}

	public int getRewardpoint() {
		return rewardpoint;
	}

	public void setRewardpoint(int rewardpoint) {
		this.rewardpoint = rewardpoint;
	}

	public int getHitpoint() {
		return hitpoint;
	}

	public void setHitpoint(int hitpoint) {
		this.hitpoint = hitpoint;
	}

	public int getMovementspeed() {
		return movementspeed;
	}

	public void setMovementspeed(int movementspeed) {
		this.movementspeed = movementspeed;
	}

	public int getSkill() {
		return skill;
	}

	public void setSkill(int skill) {
		this.skill = skill;
	}

	public float getXpos() {
		return xpos;
	}

	public void setXpos(float xpos) {
		this.xpos = xpos;
	}

	public float getYpos() {
		return ypos;
	}

	public void setYpos(float ypos) {
		this.ypos = ypos;
	}

	public float getZpos() {
		return zpos;
	}

	public void setZpos(float zpos) {
		this.zpos = zpos;
	}

	public float getH() {
		return h;
	}

	public void setH(float h) {
		this.h = h;
	}

	public int getTeamid() {
		return teamid;
	}

	public void setTeamid(int teamid) {
		this.teamid = teamid;
	}

	public int getMovement() {
		return movement;
	}

	public void setMovement(int movement) {
		this.movement = movement;
	}

	public boolean isIsAttacking() {
		return IsAttacking;
	}

	public void setIsAttacking(boolean isAttacking) {
		IsAttacking = isAttacking;
	}

	public ArrayList<CharacterModel> getCmlist() {
		return cmlist;
	}

	public void setCmlist(ArrayList<CharacterModel> cmlist) {
		this.cmlist = cmlist;
	}

	
	
	
}
