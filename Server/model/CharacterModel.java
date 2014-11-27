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
	double xpos;
	double ypos;
	double zpos;
	double h;
	int teamid;
	int movement;
	boolean IsAttacking;
	boolean IsActive = false;
	int attackId;
	int health = 100;
	
	public CharacterModel()
	{
	}
	
	public CharacterModel(int c_id,int ctype,String username,int teamid,String char_name)
	{
		this.c_id = c_id;
		this.ctype = ctype;
		this.username = username;
		this.teamid = teamid;
		this.name = char_name;
	}
	
	public CharacterModel(int ctype,int teamid,String name,boolean IsActive)
	{
		this.ctype = ctype;
		this.teamid=teamid;
		this.name = name;
		this.IsActive = IsActive;
	}
	
	

	public int getAttackId() {
		return attackId;
	}

	public void setAttackId(int attackId) {
		this.attackId = attackId;
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

	public double getXpos() {
		return xpos;
	}

	public void setXpos(double xpos) {
		this.xpos = xpos;
	}

	public double getYpos() {
		return ypos;
	}

	public void setYpos(double ypos) {
		this.ypos = ypos;
	}

	public double getZpos() {
		return zpos;
	}

	public void setZpos(double zpos) {
		this.zpos = zpos;
	}

	public double getH() {
		return h;
	}

	public void setH(double h) {
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

	public boolean isIsActive() {
		return IsActive;
	}

	public void setIsActive(boolean isActive) {
		IsActive = isActive;
	}

	public int getHealth() {
		return health;
	}

	public void setHealth(int health) {
		this.health = health;
	}
	
	
	
}
