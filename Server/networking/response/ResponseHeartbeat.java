package networking.response;

import java.util.List;

import core.GameClient;
import metadata.Constants;
import metadata.Character;
import utility.GamePacket;

public class ResponseHeartbeat extends GameResponse {
	
	private GameResponse r ;
	private String a;
	//String msg="Hello you are online";
	public  byte[] constructResponseInBytes()
	{
		GamePacket packet=new GamePacket(responseCode);
		
		
		
		/*Character temp=r.getC().getC();
		System.out.println(temp.getHitpoint());
		 packet.addInt32(temp.getHitpoint());
		 packet.addString(temp.getCtype());
		 packet.addString(temp.getTeamid());*/
		
		 packet.addString(a);
		 return packet.getBytes();
		
	}
public void setResponse(GameResponse r)
{
	this.r=r;
}
public void setNo(String a)
{
this.a=a;	
}
	
	
}
