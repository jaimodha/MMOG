package networking.request;

import java.io.IOException;

import model.Player;
import networking.response.ResponseMove;
import utility.DataReader;

public class RequestMove extends GameRequest{

	private float x;
	private float y;
	private float z;
	private float rotation;
	
	private ResponseMove responseMove;
	
	public RequestMove()
	{
		responses.add(responseMove = new ResponseMove());
	}
	
	@Override
	public void parse() throws IOException {
		x = DataReader.readFloat(dataInput);
        y = DataReader.readFloat(dataInput);
		z = DataReader.readFloat(dataInput);
		rotation = DataReader.readFloat(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		Player player = client.getPlayer();
		player.setX(x);
		player.setY(y);
		player.setZ(z);
		player.setRotation(rotation);
		responseMove.setPlayer(player);
		
		//tell other clients
		client.getServer().addResponseForAllOnlinePlayers(player.getPlayer_id(), responseMove);
	}
	
}
