from discord.ext import commands
import discord


class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help', aliases=['h', 'info'])
    async def help(self, ctx):
        pass

    @commands.command(name='set-prefix', aliases=['setprefix', 'sp', 'prefix'])
    async def set_prefix(self, ctx, prefix):
        pass


def setup(client):
    client.add_cog(Utils(client))
