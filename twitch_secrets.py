# Consider using a .env or another form of Configuration file!
CLIENT_ID: str = "INSERT CLIENT ID HERE"  # The CLIENT ID from the Twitch Dev Console
with open("./.af_detect_client_secret") as f:
    CLIENT_SECRET = f.readlines()[0]
BOT_ID = "INSERT BOT ACCOUNT ID"  # The Account ID of the bot user...
OWNER_ID = "INSERT BOT OWNER ID"  # Your personal User ID..
CRELLY_ID = "719949561"  # The cow
