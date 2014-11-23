package networking.request;

import java.io.IOException;

import networking.response.ResponseStop;

public class RequestStop extends GameRequest{

	private ResponseStop responseStop;
	
	public RequestStop()
	{
		responses.add(responseStop);
	}
	
	@Override
	public void parse() throws IOException {
		
	}

	@Override
	public void doBusiness() throws Exception {
		responseStop.setId(client.getPlayer().getPlayer_id());
		
		client.getServer().addResponseForAllOnlinePlayers(client.getPlayer().getPlayer_id(), responseStop);
	}

}
