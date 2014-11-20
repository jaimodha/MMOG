package core;

import model.Player;

public class Panda {
	private float x;
	private float y;
	private float rotation;
	private float wx;
	private float wy;
	private float speed;
	private float threshold;
	private GameServer server;
	private Player target;
	
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
		target = null;
		
		for(Player player : server.getActivePlayers())
		{
			currDist = getDist(player.getX(), player.getY());
			if ( currDist < closestDist)
			{
				closestDist = currDist;
				target = player;
			}
		}
		
		if (target == null)
		{
			move(wx, wy);
			if(getDist(wx, wy) < speed)
			{
				setWaypoint();
			}
		}
		else
		{
			move(target.getX(), target.getY());
		}
	}
	
	private void move(float tx, float ty)
	{
		float angle = (float)Math.atan2((double)ty - y, (double)tx - x);
		x += Math.cos(angle) * speed;
		y += Math.sin(angle) * speed;
		rotation = (float)(angle / Math.PI) * 180;
	}
	
	private float getDist(float x, float y)
	{
		float dist = 0;
		dist = (float) Math.sqrt(Math.pow(x - this.x, 2) + Math.pow(y - this.y, 2));
		return dist;
	}
}
