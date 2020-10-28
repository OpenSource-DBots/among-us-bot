from datetime import datetime

from discord.ext import commands
import discord

import json


"""
Get an key in the json config file
"""
def get_json(key: str) -> str:
    with open('./config.json') as c:
        config = json.load(c)

    # Return the value of the key
    return config.get(key)


client = commands.Bot(command_prefix=get_json('prefix'))


def startup():
    print("-------------------------------------------------------------------")
    print("                                                   _           _   ")
    print("  __ _ _ __ ___   ___  _ __   __ _    _   _ ___   | |__   ___ | |_ ")
    print(" / _` | '_ ` _ \ / _ \| '_ \ / _` |  | | | / __|  | '_ \ / _ \| __|")
    print("| (_| | | | | | | (_) | | | | (_| |  | |_| \__ \  | |_) | (_) | |_ ")
    print(" \__,_|_| |_| |_|\___/|_| |_|\__, |   \__,_|___/  |_.__/ \___/ \__|")
    print("                             |___/                                 ")
    print("-------------------------------------------------------------------")
    print(f"Author: {get_json('author')} | Discord: {get_json('discord')} | Version: {get_json('version')}")

    client.run(token())


"""
Return the bot token
"""
def token() -> str:
    with open('./token.secret', 'r') as f:
        token = f.read()

    return token


"""
Get the current time as hours : minutes : seconds
"""
def get_current_time() -> str:
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S")


@client.event
async def on_ready():
    print(f'[{get_current_time()}] Bot \'{client.user.name}\' is now up and running!')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=get_json('watching_status')))


startup()
