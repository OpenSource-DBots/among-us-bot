from discord.ext import commands
import discord

class AmongUs(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.party_leader = discord.Member

    @commands.command(name='claim')
    async def claim(self, ctx):
        try:  # Try assigning a member as party leader
            embed = discord.Embed(
                description=f'{self.party_leader.mention}, you are the **Party Leader** in '
                            f'`{self.party_leader.voice.channel.name}`!',
                color=discord.Color.from_rgb(0, 125, 0))
            can_be_party_leader = True
        except Exception: # Failed to assign the member as party leader
            embed = discord.Embed(
                description=f'{self.party_leader.mention}, please join a voice-channel to be able claiming **Party Leader**.',
                color=discord.Color.from_rgb(125, 0, 0))
            can_be_party_leader = False

        # Assign the user as party leader if possible
        if can_be_party_leader:
            self.party_leader = ctx.author

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(AmongUs(client))
