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

    # Group and User Data
    GROUP_USER_DATA = eval(environ.get("GROUP_USER_DATA", ""))
    """
    For 'GROUP_USER_DATA', read it carefully.
    create a dictionary or json data, and add data like this

    Syntax Below:-
    {
        GroupId1 : {
            userid1 : lang1,
            userid2 : lang2,
            userid3 : lang3,
            ....
        },
        GroupId2 : {
            userid1 : lang1,
            userid2 : lang2,
            userid3 : lang3,
            ....
        },
        ....
    }

    eg.,
    {
        -610274425 : {
            5105154963 : 'hi',
            4175164933 : 'eng'
        },
        -100610274425: {
            2125464768 : 'ru',
            3135566963 : 'eng'
        }
    }

    Now in this example,
    In group -610274425, user with userid 5105154963, his message will translate to hindi,
    And user with userid 4175164933, his message will translate to english.

    Hope you understand it.
    """

