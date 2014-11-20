package metadata;

/**
 * The Constants class stores important variables as constants for later use.
 */
public class Constants {

    // Request (1xx) + Response (2xx)
    public final static short CMSG_AUTH = 101;
    public final static short SMSG_AUTH = 201;
    public final static short CMSG_CREATE_ACCOUNT = 102;
    public final static short SMSG_CREATE_ACCOUNT = 202;
    public final static short SMSG_ADD = 203;
    public final static short CMSG_CHAT = 112;
    public final static short SMSG_CHAT = 212;
    public final static short CMSG_HEARTBEAT = 113;
    public final static short SMSG_HEARTBEAT = 213;
    public final static short CMSG_MOVE = 114;
    public final static short SMSG_MOVE = 214;
    public final static short CMSG_STOP = 115;
    public final static short SMSG_STOP = 215;
    public final static short SMSG_PANDA = 216;
    public final static short CMSG_SAVE_EXIT_GAME = 119;
    public final static short SMSG_SAVE_EXIT_GAME = 219;
    public final static short SMSG_CREATE_ENV = 329;

    // Other
    public static final int SAVE_INTERVAL = 60000;
    public static final String CLIENT_VERSION = "1.00";
    public static final int TIMEOUT_SECONDS = 90;
}
