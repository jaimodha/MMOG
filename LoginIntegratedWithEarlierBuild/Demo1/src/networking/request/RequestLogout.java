package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseAuth;
import networking.response.ResponseLogout;
import metadata.Constants;

public class RequestLogout extends GameRequest {

	
	private ResponseLogout res;
	public RequestLogout()
	{
		request_id=Constants.CMSG_DISCONNECT;
		responses.add(res = new ResponseLogout());
		
	}

	 public  void parse() throws IOException
	 {
		
	 }
	 public void doBusiness() throws Exception
	 {
		 //write a code for update the queue of all the client that 
		 // this person is logged out
		 client.getServer().removeActivePlayer(client.getUm().getUserid());
		 res.setUm(client.getUm());
		 client.getServer().addResponseForAllOnlinePlayers(client.getUm().getUserid(), res);
	 }

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return res.constructResponseInBytes();
	}
}
