from datetime import datetime
import discord
import json
import logging

"""
Summary:
    Get the current date time info
Returns:
    The current date time
"""
def get_time() -> str:
    current_time = datetime.now()
    return current_time.strftime('%H:%M:%S')


"""
Summary:
    Prints the bot name in ascii art
"""
def bot_ascii_art():
    print("----------------------------------------------------------------------")
    print("                                         _    _       ____        _   ")
    print("     /\                                 | |  | |     |  _ \      | |  ")
    print("    /  \   _ __ ___   ___  _ __   __ _  | |  | |___  | |_) | ___ | |_ ")
    print("   / /\ \ | '_ ` _ \ / _ \| '_ \ / _` | | |  | / __| |  _ < / _ \| __|")
    print("  / ____ \| | | | | | (_) | | | | (_| | | |__| \__ \ | |_) | (_) | |_ ")
    print(" /_/    \_\_| |_| |_|\___/|_| |_|\__, |  \____/|___/ |____/ \___/ \__|")
    print("                                  __/ |                               ")
    print("                                 |___/                                ")
    print("----------------------------------------------------------------------")


"""
Summary:
    Display the basic bot info: author, discord tag and version
"""
def bot_basic_info():
    with open('./config.json', 'r') as cfg:
        raw_json = json.loads(cfg.read())
        print(f'Author: {raw_json["author"]} | Discord: {raw_json["discord"]} | Version: {raw_json["version"]}')


class Client(discord.Client):

    """
    Run the Discord bot
    """
    def run(self):
        bot_ascii_art()
        bot_basic_info()

        try:  # Start the discord bot
            self.loop.run_until_complete(self.start(self.bot_token))
        except discord.LoginFailure:
            logging.critical('Invalid token')

    async def on_connect(self):
        print(f'[{get_time()}] \'{self.user}\' is connecting to the Discord services!')

    async def on_ready(self):
        print(f'[{get_time()}] \'{self.user}\' has connected!')

    @property
    def bot_token(self) -> str:
        with open('./token.secret') as cfg:
            token = cfg.read()
            return token

    """
    Summary:
        Get the current time as h:m:s
    Returns:
        The current time as h:m:s
    """
    @property
    def get_time(self) -> str:
        current_time = datetime.now()
        return current_time.strftime('%H:%M:%S')


def main():
    client = Client()
    client.run()


if __name__ == '__main__':
    main()
