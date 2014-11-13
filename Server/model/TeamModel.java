package model;

import java.util.ArrayList;

public class TeamModel {
	
	int teamid;
	String teamname;
	
	ArrayList<TeamModel> tmlist;
	
	public TeamModel()
	{
		tmlist = new ArrayList<TeamModel>();
	}

	public int getTeamid() {
		return teamid;
	}

	public void setTeamid(int teamid) {
		this.teamid = teamid;
	}

	public String getTeamname() {
		return teamname;
	}

	public void setTeamname(String teamname) {
		this.teamname = teamname;
	}

	public ArrayList<TeamModel> getTmlist() {
		return tmlist;
	}

	public void setTmlist(ArrayList<TeamModel> tmlist) {
		this.tmlist = tmlist;
	}
	
	
	
}
