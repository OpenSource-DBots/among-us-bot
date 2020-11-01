from discord.ext import commands
import discord


"""
Summary:
    Send a Discord embedded message
Params:
    ctx: context message
    description: The embed its description
    color: The color of the embed
"""
async def send_discord_embed(ctx, description: str, color: discord.Color):
    embed = discord.Embed(description=description, color=color)
    await ctx.send(embed=embed)


class AmongUs(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.party_leader = None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member == self.party_leader:
            # Make sure the user is still in the channel
            try:
                for user in self.get_users_in_channel(member.voice.channel.id):
                    if member != user:
                        await user.edit(mute=self.party_leader.voice.self_mute)
            except Exception:
                self.party_leader = None

    @commands.command(name='claim')
    async def claim(self, ctx):
        # Try assigning a user as party leader
        try:
            # Notify the user when its trying to claim party leader, but already is
            if self.party_leader == ctx.author:
                await send_discord_embed(
                    ctx=ctx,
                    description=f'{ctx.author.mention}, you are already a **Party Leader** of `{ctx.author.voice.channel.name}`',
                    color=discord.Color.from_rgb(125, 0, 0))

                return
            # Make sure no one else can claim party leader if there is already one
            elif self.party_leader is not None:
                await send_discord_embed(
                    ctx=ctx,
                    description=f'{ctx.author.mention}, **Party Leader** has already claimed by '
                                f'{self.party_leader.mention}',
                    color=discord.Color.from_rgb(125, 0, 0))

                return

            await send_discord_embed(
                ctx=ctx,
                description=f'{ctx.author.mention}, you are the **Party Leader** in '
                            f'`{ctx.author.voice.channel.name}`!',
                color=discord.Color.from_rgb(0, 125, 0))

            can_be_party_leader = True

        # Failed to assign the user as party leader
        except Exception:
            await send_discord_embed(
                ctx=ctx,
                description=f'{ctx.author.mention}, please join a voice-channel to be able claiming **Party Leader**.'
                            f'If you are, there went something wrong.',
                color=discord.Color.from_rgb(125, 0, 0))

            can_be_party_leader = False

        # Assign the user as party leader if possible
        if can_be_party_leader:
            self.party_leader = ctx.author
        else:
            self.party_leader = discord.Member

    """
    Summary:
        Get all the users in the same channel als the party leader
    Returns:
        List of all users in the same channel als the party leader
    """
    def get_users_in_channel(self, channel_id) -> list:
        members = self.client.get_channel(channel_id).members
        return members


def setup(client):
    client.add_cog(AmongUs(client))
