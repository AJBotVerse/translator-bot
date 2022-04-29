#!/usr/bin/env python3


### Importing
# Importing External Packages
from pyrogram import Client, filters
from pyrogram.types import Update, Message

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


### Handlers
# Start & Help Handler
@app.on_message(filters.private & filters.command(["start", "help"]))
async def start_help_handler(
    bot : Update,
    msg : Message
    ):
    return await msg.reply_text("<b>Lol</b>")


# Running The Bot
if __name__ == '__main__':
    print("Running Bot Now!!!")
    app.run()

