package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseControlPointState;

public class RequestControlPointState extends GameRequest{

	private int controlPointId ;
	private int controlPointState ;
	private ResponseControlPointState res;
	
	public RequestControlPointState()
	{
		 responses.add(res = new ResponseControlPointState());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		controlPointId=DataReader.readInt(dataInput);
		controlPointState=DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		for(int i=0;i<server.getCplist().size();i++)
		{
			if(server.getCplist().get(i).getCountrolid() == controlPointId)
			{
				
				server.getCplist().get(i).setState(controlPointState);
				res.setControlPointState(controlPointState);
				res.setCp(server.getCplist().get(i));
			}
		}
		
	}

	@Override
	public byte[] respond() throws IOException {
		// TODO Auto-generated method stub
		return res.constructResponseInBytes();
	}

}
