package networking.response;

import metadata.Constants;
import model.UserModel;
import utility.GamePacket;

public class ResponseCharacterCreation extends GameResponse {

	private int flag;
	private int charcount;
	private String charname;
	private int charid;
	private int chartype;
	private int charfaction;
	public byte[] temp ;
	
	

	public ResponseCharacterCreation()
    {
    	responseCode = Constants.SMSG_CREATE_CHARACTER;
    }
	
	 public byte[] constructResponseInBytes()
	 {
		 System.out.println(responseCode);
		 GamePacket packet=new GamePacket(responseCode);
		// System.out.println(responseCode);
		 //System.out.println(message);
		 
		
		//System.out.println(cr_func+"  "+cr_name);
		 System.out.println(flag+"-------");
		 packet.addInt32(flag);
		 if(getFlag() == 1)
		 {
			 packet.addInt32(charcount);
			 packet.addString(charname);
			 packet.addInt32(charid);
			 packet.addInt32(chartype);
			 packet.addInt32(charfaction);
			 System.out.println(charcount+"-"+charname+"-"+charid+"-"+chartype+"-"+charfaction+"@@");
		 }
		 temp = packet.getBytes();
		 //System.out.println(temp+"----");
		 return temp;
	 }

	public int getFlag() {
		return flag;
	}

	public void setFlag(int flag) {
		this.flag = flag;
	}

	public int getCharcount() {
		return charcount;
	}

	public void setCharcount(int charcount) {
		this.charcount = charcount;
	}

	public String getCharname() {
		return charname;
	}

	public void setCharname(String charname) {
		this.charname = charname;
	}

	public int getCharid() {
		return charid;
	}

	public void setCharid(int charid) {
		this.charid = charid;
	}

	public int getChartype() {
		return chartype;
	}

	public void setChartype(int chartype) {
		this.chartype = chartype;
	}

	public int getCharfaction() {
		return charfaction;
	}

	public void setCharfaction(int charfaction) {
		this.charfaction = charfaction;
	}
 
	
	
}
