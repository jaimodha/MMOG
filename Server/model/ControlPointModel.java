package model;

import java.util.ArrayList;

public class ControlPointModel {

	int countrolid;
	double xpos;
	double ypos;
	double zpos;
	int attackpoints;
	int defencepoints;
	int money;
	int gs_resourcepoints;
	String owner;
	
	ArrayList<ControlPointModel> cpmodel;
	
	public ControlPointModel()
	{
		cpmodel = new ArrayList<ControlPointModel>();
	}

	public int getCountrolid() {
		return countrolid;
	}

	public void setCountrolid(int countrolid) {
		this.countrolid = countrolid;
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

	public int getMoney() {
		return money;
	}

	public void setMoney(int money) {
		this.money = money;
	}

	public int getGs_resourcepoints() {
		return gs_resourcepoints;
	}

	public void setGs_resourcepoints(int gs_resourcepoints) {
		this.gs_resourcepoints = gs_resourcepoints;
	}

	public String getOwner() {
		return owner;
	}

	public void setOwner(String owner) {
		this.owner = owner;
	}

	public ArrayList<ControlPointModel> getCpmodel() {
		return cpmodel;
	}

	public void setCpmodel(ArrayList<ControlPointModel> cpmodel) {
		this.cpmodel = cpmodel;
	}

	
	
}
