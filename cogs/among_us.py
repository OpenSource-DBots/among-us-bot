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
                description=f'{ctx.author.mention}, you are the **Party Leader** in '
                            f'`{ctx.author.voice.channel.name}`!',
                color=discord.Color.from_rgb(0, 125, 0))
            can_be_party_leader = True
        except Exception:  # Failed to assign the member as party leader
            embed = discord.Embed(
                description=f'{ctx.author.mention}, please join a voice-channel to be able claiming **Party Leader**.',
                color=discord.Color.from_rgb(125, 0, 0))
            can_be_party_leader = False

        # Assign the user as party leader if possible
        if can_be_party_leader:
            self.party_leader = ctx.author
        else:
            self.party_leader = discord.Member

        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.party_leader:
            for user in self.get_users_in_channel(member.voice.channel.id):
                if member != user:
                    await user.edit(mute=self.party_leader.voice.self_mute)

    def get_users_in_channel(self, channel_id) -> list:
        members = self.client.get_channel(channel_id).members
        return members

def setup(client):
    client.add_cog(AmongUs(client))
