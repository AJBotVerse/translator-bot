#!/usr/bin/env python3


### Importing
# Importing External Packages
from pyrogram import Client

# Importing Inbuilt Packages
import logging

# Importing Credentials & Required Data
try:
    from testexp.config import Config
except ModuleNotFoundError:
    from config import Config

### For Displaying Errors&Warnings Better
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler("translator.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logging.getLogger(
    "pyrogram"
).setLevel(
    logging.WARNING
)

# Connecting to Bot
print("Connecting to Bot")
app = Client(
    "TranslatorBot",
    bot_token = Config.TG_BOT_TOKEN,
    api_id = Config.APP_ID,
    api_hash = Config.API_HASH
)
print("Connection Establised")


# Running The Bot
if __name__ == '__main__':
    print("Running Bot Now!!!")
    app.run()

