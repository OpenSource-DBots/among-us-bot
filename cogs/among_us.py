from discord.ext import commands

class AmongUs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(AmongUs(client))
