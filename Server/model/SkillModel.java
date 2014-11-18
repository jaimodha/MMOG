package model;

import java.util.ArrayList;

public class SkillModel {

	int skillid;
	String skillname;
	String description;
	
	ArrayList<SkillModel> sklist;
	
	public SkillModel()
	{
		sklist = new ArrayList<SkillModel>();
	}

	public int getSkillid() {
		return skillid;
	}

	public void setSkillid(int skillid) {
		this.skillid = skillid;
	}

	public String getSkillname() {
		return skillname;
	}

	public void setSkillname(String skillname) {
		this.skillname = skillname;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public ArrayList<SkillModel> getSklist() {
		return sklist;
	}

	public void setSklist(ArrayList<SkillModel> sklist) {
		this.sklist = sklist;
	}
	
	
}
