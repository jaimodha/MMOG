# define Constants

class Constants:
    RAND_INT                            = 1
    RAND_STRING                         = 2
    RAND_SHORT                          = 3
    RAND_FLOAT                          = 4

    SERVER_IP = 'localhost'
    SERVER_PORT = 9252
    DEBUG = True
    MSG_NONE                            = 0
    
    CMSG_AUTH                           = 101
    CMSG_MOVE                           = 106
    CMSG_ATTACK                         = 107
    CMSG_HEALTH                         = 108
    
    SMSG_AUTH                           = 201
    SMSG_MOVE                           = 206
    SMSG_ATTACK                         = 207
    SMSG_HEALTH                         = 208
    
    REQ_HEARTBEAT                       = 301