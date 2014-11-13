package model;

import java.util.ArrayList;

public class CharacterModel {
	
	int u_id;
	int c_id;
	String name;
	String ctype;
	int rewardpoint;
 	int hitpoint;
	int movementspeed;
    ArrayList<SkillModel> s;
	double xpos;
	double ypos;
	double zpos;
	double h;
	double p;
	double r;
	int teamid;
	int movement;
	
	ArrayList<CharacterModel> cmlist;
	
	public CharacterModel()
	{
		cmlist = new ArrayList<CharacterModel>();
		s = new ArrayList<SkillModel>();
	}

	public int getU_id() {
		return u_id;
	}

	public void setU_id(int u_id) {
		this.u_id = u_id;
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

	public String getCtype() {
		return ctype;
	}

	public void setCtype(String ctype) {
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

	public ArrayList<SkillModel> getS() {
		return s;
	}

	public void setS(ArrayList<SkillModel> s) {
		this.s = s;
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

	public double getP() {
		return p;
	}

	public void setP(double p) {
		this.p = p;
	}

	public double getR() {
		return r;
	}

	public void setR(double r) {
		this.r = r;
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

	public ArrayList<CharacterModel> getCmlist() {
		return cmlist;
	}

	public void setCmlist(ArrayList<CharacterModel> cmlist) {
		this.cmlist = cmlist;
	}
	
	
	
	
}
