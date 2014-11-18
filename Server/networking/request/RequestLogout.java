package networking.request;

import java.io.IOException;

import metadata.Constants;

public class RequestLogout extends GameRequest {

	public RequestLogout()
	{
		request_id=Constants.CMSG_DISCONNECT;
	}

	 public  void parse() throws IOException
	 {

		 
		 // call validateion method here 
		 //if its true 
		     
		    
		 
	 }
	 public void doBusiness() throws Exception
	 {
		 //write response code here 
		 
		 
	 }
}
