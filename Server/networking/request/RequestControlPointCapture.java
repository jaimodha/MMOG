package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseCharacterAttack;
import networking.response.ResponseControlPointCapture;

public class RequestControlPointCapture extends GameRequest{

	private  int controlPointId;
	private int factionId;
	private ResponseControlPointCapture res;
	
	public RequestControlPointCapture()
	{
		responses.add(res = new ResponseControlPointCapture());
	}
	
	@Override
	public void parse() throws IOException {
		// TODO Auto-generated method stub
		controlPointId=DataReader.readInt(dataInput);
		factionId = DataReader.readInt(dataInput);;
	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		for(int i=0;i<server.getCplist().size();i++)
		{
			if(server.getCplist().get(i).getCountrolid() == controlPointId)
			{
				
				server.getCplist().get(i).setOwner(factionId);
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
