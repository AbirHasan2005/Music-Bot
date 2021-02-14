from pyrogram import filters

try:
    from config.config import *
except ImportError:
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--token",
        help="Bot token",
        required=True,
    )
    parser.add_argument(
        "--api-id",
        help="Telegram api_id, get it from my.telegram.org/apps",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--api-hash",
        help="Telegram api_hash, get it from my.telegram.org/apps",
        required=True,
    )
    parser.add_argument(
        "--mongodb-uri",
        help="MongoDB URI, if you don't provide the bot will lack some cool features",
        required=True,
    )
    parser.add_argument(
        "--sudo-users",
        help="List of user ids, separate by underscore (example: 1_3)",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--group",
        help="Id of the group where the bot streams",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--users-must-join",
        help="If provided, only members of the group can use the bot",
        type=bool,
        required=False,
        default=False,
    )
    parser.add_argument(
        "--lang",
        help="Bot language, choose from strings/",
        required=True,
    )
    parser.add_argument(
        "--dur-limit",
        help="Video download duration limit (in minutes)",
        type=int,
        required=True,
    )
    args = parser.parse_args()
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
    USERS_MUST_JOIN = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
    LANG = "en"

# Max video duration allowed for user downloads in minutes
    DUR_LIMIT = 15

# No need to touch the following.
    LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
    SUDO_FILTER = filters.user(SUDO_USERS)

async def custom_filter(_, __, ___):
    return bool(LOG_GROUP)

LOG_GROUP_FILTER = filters.create(custom_filter)
