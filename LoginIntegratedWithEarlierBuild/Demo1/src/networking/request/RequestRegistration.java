package networking.request;

import java.io.IOException;

import core.Database;
import utility.DataReader;
import networking.response.ResponseAuth;
import networking.response.ResponseRegistration;

public class RequestRegistration extends GameRequest{

	private String Username;
	private String Password;
	private ResponseRegistration res;
	Database db = new Database();

	public RequestRegistration()
	{
		responses.add(res = new ResponseRegistration());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		Username = DataReader.readString(dataInput);
		Password = DataReader.readString(dataInput);
		
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		boolean r = db.createAccount(Username, Password);
		if(r)
		{
			res.setFlag(1);
		}
		else
		{
			res.setFlag(0);
		}
	}

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return res.constructResponseInBytes();
	}

}
