#!/usr/bin/env python3


### Importing
# Importing External Packages
from pyrogram import Client, filters
from pyrogram.types import Update, Message

# Importing Inbuilt Packages
import logging

# Importing dev modules
from google_trans.google_trans_new import google_translator

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


### Objects and some variables
translator = google_translator()
group_user_data = Config.GROUP_USER_DATA


### Some well defined functions
def trans(text, lang):
    try:
        translate_text = translator.translate(
            text,
            lang_tgt = lang
        )
    except Exception as e:
        print(e)
        return
    else:
        return translate_text


### Connecting to Bot
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

# Log files Handler
@app.on_message(filters.chat(Config.OWNER_ID) & filters.private & filters.command("log"))
async def logHandler(
    bot : Update,
    msg : Message
    ):
    try:
        await msg.reply_document('translator.log')
    except Exception as e:
        await msg.reply_text(
            f"Something went wrong while sending log file.\n{e}"
        )

# Translate Handler
@app.on_message(filters.group)
async def translate_handler(
    bot : Update,
    msg : Message
    ):
    group_id = msg.chat.id
    try:
        user_data = group_user_data[group_id]
    except KeyError:
        pass
    except Exception as e:
        print(e)
    else:
        userid = msg.from_user.id
        try:
            lang = user_data[userid]
        except KeyError:
            pass
        except Exception as e:
            print(e)
        else:
            trans_text = trans(msg.text, lang)
            if trans_text:
                await msg.reply_text(
                    trans_text,
                    reply_to_message_id = msg.id
                )
    finally:
        return


### Running The Bot
if __name__ == '__main__':
    print("Running Bot Now!!!")
    app.run()

