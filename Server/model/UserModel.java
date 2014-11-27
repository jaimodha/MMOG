package model;

import java.util.ArrayList;

public class UserModel {

	int userid;
	String username;
	String password;
	boolean IsConnected;
	ArrayList<CharacterModel> charlist;
	
	
	public UserModel()
	{
		charlist=new ArrayList<CharacterModel>();
	}

	
	
	public int getUserid() {
		return userid;
	}



	public void setUserid(int userid) {
		this.userid = userid;
	}



	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	
	public boolean isIsConnected() {
		return IsConnected;
	}

	public void setIsConnected(boolean isConnected) {
		IsConnected = isConnected;
	}

	public ArrayList<CharacterModel> getCharlist() {
		return charlist;
	}

	public void setCharlist(ArrayList<CharacterModel> charlist) {
		this.charlist = charlist;
	}

	
	
}
