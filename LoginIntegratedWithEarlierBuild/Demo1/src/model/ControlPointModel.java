package model;

import java.util.ArrayList;

public class ControlPointModel {

	int controlid;
	double xpos;
	double ypos;
	double zpos;
	double radius;
	int attackpoints;
	int defencepoints;
	int gs_resourcepoints;
	int state;
	int owner;
	
	
	public ControlPointModel()
	{
	}
	

	public ControlPointModel(int controlid,double xpos,double ypos,double zpos,double radius,int attackpoints,int defencepoints,int gs_resourcepoints,int owner,int state)
	{
		this.controlid = controlid;
		this.xpos = xpos;
		this.ypos = ypos;
		this.zpos=zpos;
		this.radius=radius;
		this.attackpoints=attackpoints;
		this.defencepoints = defencepoints;
		this.gs_resourcepoints = gs_resourcepoints;
		this.owner = owner;
		this.state= state;
	}
	
	
	
	public int getState() {
		return state;
	}


	public void setState(int state) {
		this.state = state;
	}


	public int getCountrolid() {
		return controlid;
	}

	public void setCountrolid(int controlid) {
		this.controlid = controlid;
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

	public int getAttackpoints() {
		return attackpoints;
	}

	public void setAttackpoints(int attackpoints) {
		this.attackpoints = attackpoints;
	}

	public int getDefencepoints() {
		return defencepoints;
	}

	public void setDefencepoints(int defencepoints) {
		this.defencepoints = defencepoints;
	}


	public int getGs_resourcepoints() {
		return gs_resourcepoints;
	}

	public void setGs_resourcepoints(int gs_resourcepoints) {
		this.gs_resourcepoints = gs_resourcepoints;
	}

	public int getOwner() {
		return owner;
	}

	public void setOwner(int owner) {
		this.owner = owner;
	}

	
	
}
