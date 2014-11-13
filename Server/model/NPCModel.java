package model;

import java.util.ArrayList;

public class NPCModel {
	
    int npcid;
	String npcname;
	double xpos;
	double ypos;
	double zpos;
	double h;
	double p;
	double r;
	
	ArrayList<NPCModel> npclist;
	
	public NPCModel()
	{
		npclist = new ArrayList<NPCModel>();
	}

	public int getNpcid() {
		return npcid;
	}

	public void setNpcid(int npcid) {
		this.npcid = npcid;
	}

	public String getNpcname() {
		return npcname;
	}

	public void setNpcname(String npcname) {
		this.npcname = npcname;
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

	public ArrayList<NPCModel> getNpclist() {
		return npclist;
	}

	public void setNpclist(ArrayList<NPCModel> npclist) {
		this.npclist = npclist;
	}
	
	

}
