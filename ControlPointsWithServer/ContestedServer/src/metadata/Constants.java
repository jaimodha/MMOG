package metadata;

/**
 * The Constants class stores important variables as constants for later use.
 */
public class Constants {

    // Request (1xx) + Response (2xx)
    public final static short CMSG_AUTH = 101;
    public final static short SMSG_AUTH = 201;
    public final static short CMSG_MOVE = 106;
    public final static short SMSG_MOVE = 206;
    public final static short CMSG_CONTROL_POINT_STATE = 111;
    public final static short SMSG_CONTROL_POINT_STATE = 211;
    public final static short CMSG_SAVE_EXIT_GAME = 119;
    public final static short SMSG_SAVE_EXIT_GAME = 219;
    public final static short REQ_HEARTBEAT = 301;
    public final static short SMSG_CREATE_ENV = 329;

    //Test Request + Response
    public final static short RAND_INT = 1;
    public final static short RAND_STRING = 2;
    public final static short RAND_SHORT = 3;
    public final static short RAND_FLOAT = 4;
    // Other
    public static final int SAVE_INTERVAL = 60000;
    public static final String CLIENT_VERSION = "1.00";
    public static final int TIMEOUT_SECONDS = 90;
    public static final int RED = 0;
    public static final int BLUE = 1;
}
