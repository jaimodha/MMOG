package networking.response;

// Custom Imports
import metadata.Constants;
import model.CharacterModel;
import utility.GamePacket;

public class ResponseCharacterMovement extends GameResponse {

	private CharacterModel character;

    public ResponseCharacterMovement() {
        responseCode = Constants.SMSG_MOVE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(character.getName());
        packet.addFloat((float) character.getXpos());
        packet.addFloat((float) character.getYpos());
        packet.addFloat((float) character.getZpos());
        packet.addFloat((float) character.getH());
        packet.addInt32(character.getMovement());
        
        return packet.getBytes();
    }

	public CharacterModel getCharacter() {
		return character;
	}

	public void setCharacter(CharacterModel character) {
		this.character = character;
	}
}
