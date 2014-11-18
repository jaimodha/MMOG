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
    CMSG_DISCONNECT                     = 102
    CMSG_REGISTER                       = 103
    CMSG_CREATE_CHARACTER               = 104
    CMSG_CHAT                           = 105
    CMSG_MOVE                           = 106
    CMSG_ATTACK                         = 107
    CMSG_HEALTH                         = 108
    CMSG_CONTROL_POINT_STATE            = 111
    CMSG_CONTROL_POINT_CAP              = 112
    REQ_HEARTBEAT                       = 301
    
    SMSG_AUTH                           = 201
    SMSG_DISCONNECT                     = 202
    SMSG_REGISTER                       = 203
    SMSG_CREATE_CHARACTER               = 204
    SMSG_CHAT                           = 205
    SMSG_MOVE                           = 206
    SMSG_ATTACK                         = 207
    SMSG_HEALTH                         = 208
    SMSG_RESOURCE                       = 209
    SMSG_CONTROL_POINT_STATE            = 211
    SMSG_CONTROL_POINT_CAP              = 212
    SMSG_RENDER_CHARACTER               = 310
    SMSG_REMOVE_CHARACTER               = 311
    SMSG_SPAWN_GUARDS                   = 312
    SMSG_DESTROY_NPC                    = 313
    SMSG_SPAWN_GOLEMCP                  = 321
    SMSG_DESTROY_GOLEMCP                = 322
    SMSG_SPAWN_GOLEM_NPC                = 323
    SMSG_GOLEM_PIECE                    = 324
