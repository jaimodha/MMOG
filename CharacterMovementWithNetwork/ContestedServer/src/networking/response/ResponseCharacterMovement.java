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
        packet.addFloat(character.getXpos());
        packet.addFloat(character.getYpos());
        packet.addFloat(character.getZpos());
        packet.addFloat(character.getH());
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
