package model;

import java.util.ArrayList;

public class CharacterModel {
	
	String name;
	float xpos;
	float ypos;
	float zpos;
	float h;
	int factionId;
	
	ArrayList<CharacterModel> cmlist;
	
	public CharacterModel()
	{
		cmlist = new ArrayList<CharacterModel>();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
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

	public int getFactionId() {
		return factionId;
	}

	public void setFactionId(int factionId) {
		this.factionId = factionId;
	}

	public ArrayList<CharacterModel> getCmlist() {
		return cmlist;
	}

	public void setCmlist(ArrayList<CharacterModel> cmlist) {
		this.cmlist = cmlist;
	}

	
	
	
}
