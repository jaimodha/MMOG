package model;

import java.util.ArrayList;

public class UserModel {

	String username;
	String password;
	String email;
	boolean IsConnected;
	
	ArrayList<UserModel> ulist;
	
	public UserModel()
	{
		ulist = new ArrayList<UserModel>();
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

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public boolean isIsConnected() {
		return IsConnected;
	}

	public void setIsConnected(boolean isConnected) {
		IsConnected = isConnected;
	}

	public ArrayList<UserModel> getUlist() {
		return ulist;
	}

	public void setUlist(ArrayList<UserModel> ulist) {
		this.ulist = ulist;
	}
	
	
}
