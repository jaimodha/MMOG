package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseLogin;
import metadata.Constants;

public class RequestLogin extends GameRequest{

	private String username;
	private String password;
	private ResponseLogin responseLogin;
	public RequestLogin()
	{
		 responses.add(responseLogin = new ResponseLogin());
	}
	 
	
	
	 public  void parse() throws IOException
	 {
		 username = DataReader.readString(dataInput);
	      password = DataReader.readString(dataInput);
		    
		 
	 }
	 public void doBusiness() throws Exception
	 {
		 // if login is valid
	        responseLogin.setMessage("1");
	        // else
	        responseLogin.setMessage("0");
		 
	 }
}
