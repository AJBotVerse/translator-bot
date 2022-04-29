# Translator Bot

A language translating bot that can translate message in other preferred language.

## Whom can it help?
This bot can help two people who don't have common language or if they have but they are not fluent in that common language.

For example, You find a friend on internet who speak some foreign language(that you don't understand),and you both(or either you or your friend) have little problem in English. So Now how will you chat with each other? Learn english(or each other's language),
An excellent option, but of course it will take time.

So for that problem this bot is introduced.

## Environment Variables
* `BOT_TOKEN` - Make a bot from https://t.me/BotFather
* `API_ID` - Get this value from https://my.telegram.org/apps
* `API_HASH` - Get this value from https://my.telegram.org/apps
* `OWNER_ID` - Your(owner's) telegram id
* `GROUP_USER_DATA` - Now this is little hard to explain, see below

For `GROUP_USER_DATA`, read it carefully.
Create a dictionary or json data, and add data like this

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

For Example,

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
In group *-610274425*, user with userid *5105154963*, his message will translate to hindi,

And user with userid *4175164933*, his message will translate to english.

Hope you understand it.

## Direct Deploy
### Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/wJljK9)

## Contributions
A Huge thanks to @lushan88a for [google_trans_new](https://github.com/lushan88a/google_trans_new)