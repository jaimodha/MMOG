package networking.request;

//Java Imports
import java.io.IOException;

import dataAccessLayer.PlayerDAO;
import utility.DataReader;
import networking.response.ResponseCreateAccount;

//Custom Imports


public class RequestCreateAccount extends GameRequest{
	
	//Data
	private String username;
	private String password;
	//Responses
	private ResponseCreateAccount responseCreateAccount;
	
	public RequestCreateAccount()
	{
		responses.add(responseCreateAccount = new ResponseCreateAccount());
	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput).trim();
        password = DataReader.readString(dataInput).trim();
	}

	@Override
	public void doBusiness() throws Exception {
		//check if username available
		if(PlayerDAO.containsUsername(username))
		{
			responseCreateAccount.setStatus((short) 1);
		}
		else
		{
			PlayerDAO.createAccount(username, password);
			responseCreateAccount.setStatus((short) 0);
		}
	}

}
