#!/usr/bin/env python3


### Importing
from os import environ

class Config(object):

    # Make a bot from https://t.me/BotFather and enter the token here
    TG_BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    
    # Get this value from https://my.telegram.org/apps
    APP_ID = int(environ.get("API_ID", 12345))
    
    # Get this value from https://my.telegram.org/apps
    API_HASH = environ.get("API_HASH", "")
    
    # Your(owner's) telegram id
    OWNER_ID = int(environ.get("OWNER_ID", None))

