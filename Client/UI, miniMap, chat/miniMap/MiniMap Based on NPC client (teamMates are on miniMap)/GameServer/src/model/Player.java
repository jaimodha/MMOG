package model;

import core.GameClient;

public class Player {
	private int player_id;
    private String username;
    private String password;
    private float x;
    private float y;
    private float z;
    private float rotation;
    private GameClient client; // References GameClient instance
    
    public Player(int player_id) {
        this.player_id = player_id;
    }
    
	public int getPlayer_id() {
		return player_id;
	}
	public void setPlayer_id(int player_id) {
		this.player_id = player_id;
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
	
	public float getX() {
		return x;
	}
	public void setX(float x) {
		this.x = x;
	}
	
	public float getY() {
		return y;
	}
	public void setY(float y) {
		this.y = y;
	}
	
	public float getZ() {
		return z;
	}
	public void setZ(float z) {
		this.z = z;
	}

	public float getRotation() {
		return rotation;
	}

	public void setRotation(float rotation) {
		this.rotation = rotation;
	}
	
	public GameClient getClient() {
		return client;
	}

	public void setClient(GameClient client) {
		this.client = client;
	}
}
