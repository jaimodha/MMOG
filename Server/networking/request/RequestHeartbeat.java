package networking.request;

import java.io.IOException;

import networking.response.GameResponse;
import networking.response.ResponseAuth;
import networking.response.ResponseHeartbeat;
import metadata.Constants;

public class RequestHeartbeat extends GameRequest {

	private ResponseHeartbeat reb;
	boolean op=false;
	public RequestHeartbeat()
	{
		 //responses.add(responseLogin = new ResponseLogin());
		 responses.add(reb = new ResponseHeartbeat());
		
	}
	
	
	public  void parse() throws IOException
	{
		
		//System.out.println("Update list after for loop"+client.getUpdates().size());
		
	}
	public  void doBusiness() throws Exception
	{
		//System.out.println("in heartbeat...."+client.getId());
		for(GameResponse r: client.getUpdates())
		{
			System.out.println("helooo---req hb");
			client.getOutputStream().write(r.constructResponseInBytes());
			
		}
		client.clearUpdateBuffer();
	}

	public  byte[] respond() throws IOException
	
	{
		byte[] a={};
		return a;
	}

}
