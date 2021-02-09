# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1578262
API_HASH = "664ecb8d62405ae3e3e015216f6e2615"

# Get this from @Botfather
TOKEN = "1325820510:AAFlkHgB_xioveMAqZ-E_U88vsB0_35xH40"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb+srv://userbot:userbot@cluster0.hwmx5.mongodb.net/cluster0?retryWrites=true&w=majority"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1445283714,
    715779594
]

# The ID of the group where your bot streams
GROUP = -1001256038785

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 15

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
