package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseExitGame extends GameResponse {

    private int id = 0;

    public ResponseExitGame() {
        responseCode = Constants.SMSG_SAVE_EXIT_GAME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(id);
        return packet.getBytes();
    }
    
    public void setID( int id )
    {
    	this.id = id;
    }
}
