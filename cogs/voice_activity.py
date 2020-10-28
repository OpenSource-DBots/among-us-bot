from datetime import datetime
from discord.ext import commands


"""
Get the current time as hours : minutes : seconds
"""
def get_current_time() -> str:
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S")


class VoiceActivity(commands.Cog):

    def __init__(self, client):
        self.client = client
        print(f'[{get_current_time()}] VoiceActivity cog is ready')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild:  # Do not allow DMs or from the bot itself
            return

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('Pong!')
