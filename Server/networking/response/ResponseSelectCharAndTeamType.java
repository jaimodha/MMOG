package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseSelectCharTeamType extends GameResponse {

    private String charType;
    private String faction;

    public ResponseSelectCharTeamType() {
        responseCode = Constants.CMSG_CREATE_CHARACTER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(charType);
        packet.addString(faction);
        return packet.getBytes();
    }
    
	
	public String getCharType(){
		return charType;
	}
	
	public String getFaction(){
		return faction;
	}

	public void setCharType(String message){
		this.charType = message;
	}
	
	public void setFaction(String message){
		this.faction = message;
	}
}
