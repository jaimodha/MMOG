package metadata;

/**
 * The Constants class stores important variables as constants for later use.
 */
public class Constants {

    // Request (1xx) 
    public final static short CMSG_AUTH = 101;
    public final static short CMSG_DISCONNECT=102;
    public final static short CMSG_REGISTER =103;
    public final static short CMSG_CREATE_CHARACTER=104;
    public final static short CMSG_CHAT=105;
    public final static short CMSG_MOVE=106;
    public final static short CMSG_ATTACK=107;
    public final static short CMSG_HEALTH	=108;
    public final static short CMSG_CONTROL_POINT_STATE=111;
    public final static short CMSG_CONTROL_POINT_CAP=112;
    public final static short CMSG_PLAYGAME=113;
    public final static short REQ_HEARTBEAT=301;

    //Test Request + Response
    public final static short RAND_INT = 1;
    public final static short RAND_STRING = 2;
    public final static short RAND_SHORT = 3;
    public final static short RAND_FLOAT = 4;
    // Other
    public static final int SAVE_shortERVAL = 60000;
    public static final String CLIENT_VERSION = "1.00";
    public static final short TIMEOUT_SECONDS = 90;
    
    //response (2xx)
    public final static short SMSG_AUTH = 201;
    public final static short SMSG_DISCONNECT = 202;
    public final static short SMSG_REGISTER = 203;
    public final static short SMSG_CREATE_CHARACTER	= 204;
    public final static short SMSG_CHAT	= 205;
    public final static short SMSG_MOVE	= 206;
    public final static short SMSG_ATTACK = 207;
    public final static short SMSG_HEALTH	= 208;
    public final static short SMSG_RESOURCE = 209;
    public final static short SMSG_CONTROL_POINT_STATE = 211;
    public final static short SMSG_CONTROL_POINT_CAP = 212;
    public final static short SMSG_PLAYGAME = 213;
    public final static short SMSG_RENDER_CHARACTER = 310;
    public final static short SMSG_REMOVE_CHARACTER =	311;
    public final static short SMSG_SPAWN_GUARDS = 312;
    public final static short SMSG_DESTROY_NPC = 313;
    public final static short SMSG_SPAWN_GOLEMCP = 321;
    public final static short SMSG_DESTROY_GOLEMCP = 322;
    public final static short SMSG_SPAWN_GOLEM_NPC = 323;
    public final static short SMSG_GOLEM_PIECE = 324;
    

}
