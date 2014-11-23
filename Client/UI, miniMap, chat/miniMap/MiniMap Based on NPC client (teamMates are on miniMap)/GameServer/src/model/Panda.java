package model;

import core.GameServer;

public class Panda {
	private float x;
	private float y;
	private float rotation;
	private float wx;
	private float wy;
	private float speed;
	private float threshold;
	private GameServer server;
	private long lastAct;
	
	public Panda(GameServer server)
	{
		this.server = server;
		x = 0;
		y = 0;
		speed = 15;
		rotation = 0;
		wx = 0;
		wy = 0;
		threshold = 15;
		lastAct = System.currentTimeMillis();
	}
	
	private void setWaypoint()
	{
		wx = (float) (Math.random() * 100 - 50);
		wy = (float) (Math.random() * 100 - 50);
	}
	
	public void updatePanda()
	{
		float closestDist = threshold;
		float currDist;
		float time = System.currentTimeMillis() - (float)lastAct / 1000;
		if (time > 1) time = 1;
		
		Player target = null;
		
		if (server.getActivePlayers().size() > 0) {
			for (Player player : server.getActivePlayers()) {
				currDist = getDist(player.getX(), player.getY());
				if (currDist < closestDist) {
					closestDist = currDist;
					target = player;
				}
			}
			if (target == null) {
				move(wx, wy);
				if (getDist(wx, wy) < speed * time) {
					setWaypoint();
				}
			} else {
				move(target.getX(), target.getY());
			}
		}
		lastAct = System.currentTimeMillis();
	}
	
	private void move(float tx, float ty)
	{
		float time = System.currentTimeMillis() - (float)lastAct / 1000;
		float angle = (float)Math.atan2((double)ty - y, (double)tx - x);
		x += Math.cos(angle) * speed * time;
		y += Math.sin(angle) * speed * time;
		rotation = (float)(angle / Math.PI) * 180;
	}
	
	private float getDist(float x, float y)
	{
		float dist = 0;
		dist = (float) Math.sqrt(Math.pow(x - this.x, 2) + Math.pow(y - this.y, 2));
		return dist;
	}
	
	public float getX()
	{
		return x;
	}
	
	public float getY()
	{
		return y;
	}
	
	public float getRotation()
	{
		return rotation;
	}
}
