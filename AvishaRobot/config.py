
class Config(object):
    LOGGER = True

    #####

    ANILIST_CLIENT = getenv("ANILIST_CLIENT", "8679")
  
    ANILIST_SECRET = getenv("ANILIST_SECRET", "NeCEq9A1hVnjsjZlTZyNvqK11krQ4HtSliaM7rTN")
  
    API_ID = getenv("API_ID", None)
   
    API_HASH = getenv("API_HASH",None)
   
    TOKEN = getenv("TOKEN", None)
  
    OWNER_ID = getenv("OWNER_ID", "6195725562") 

    OWNER_USERNAME = ("OWNER_USERNAME", "loco_x_Pilot")
    
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "the_friendz")
   
    START_IMG = getenv("START_IMG", "https://graph.org/file/eaa3a2602e43844a488a5.jpg")

    JOIN_LOGGER = getenv("JOIN_LOGGER", "-1002080453210")
   
    EVENT_LOGS = getenv("EVENT_LOGS",  "-1002080453210")
  
    ERROR_LOGS = getenv("ERROR_LOGS", "-1001929735324")

    MONGO_DB_URI= getenv("MONGO_DB_URI", None)
   
    LOG_CHANNEL = getenv("LOG_CHANNEL", "-1001852000392")
   
    BOT_USERNAME = getenv("BOT_USERNAME" , "avishaBot")
   
    DATABASE_URL = getenv("DATABASE_URL", None)

    CASH_API_KEY = getenv("CASH_API_KEY", "V48U2FLLKRHSVD4X")
    
    TIME_API_KEY = getenv("TIME_API_KEY", "1CUBX1HXGNHW")

    SPAMWATCH_API = getenv("SPAMWATCH_API", "3624487efd8e4ca9c949f1ab99654ad1e4de854f41a14afd00f3ca82d808dc8c")
    
    SPAMWATCH_SUPPORT_CHAT = getenv("SPAMWATCH_SUPPORT_CHAT", "h_cc_help")
    
    WALL_API = getenv("WALL_API", "2455acab48f3a935a8e703e54e26d121")
    
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "xYCR1ZyK3ZsofjH7Y6hPcyzC")
    
    OPENWEATHERMAP_ID = getenv("OPENWEATHERMAP_ID", "887da2c60d9f13fe78b0f9d0c5cbaade")

    BAN_STICKER = getenv("BAN_STICKER", "CAACAgEAAxkBAAIrTWYljyX_lqcubkAzg0jy45CRvxAFAAKvAgACrLHoRU50VVvh3xWwNAQ")

    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "8f3315b5806c21004b2822f07825187d")
    
    # Optional fields
    
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

  
