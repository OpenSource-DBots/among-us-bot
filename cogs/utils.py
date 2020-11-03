from discord.ext import commands
import discord


class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')  # Remove the default help command

    @commands.command(name='help', aliases=['h', 'info'])
    async def help(self, ctx):
        embed = discord.Embed(title='Among Us Bot Information', color=discord.Color.from_rgb(0, 255, 0))
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='Standard Commands',
                        value=f':small_blue_diamond:{self.client.command_prefix}claim\n'
                              f':small_blue_diamond:{self.client.command_prefix}unclaim',
                        inline=True)
        embed.add_field(name='Advance Commands',
                        value=f':small_blue_diamond:{self.client.command_prefix}prefix',
                        inline=True)
        embed.add_field(name='How does this bot work?',
                        value=f'You have to join a voice channel in order to `{self.client.command_prefix}claim` it. '
                              f'When you have claimed the voice channel - whenever you mute yourself, the other will '
                              f'be muted as well. And whenever you unmute yourself, the other will be unmuted as well. '
                              f'If you do not want to be a party leader anymore, simply type '
                              f'`{self.client.command_prefix}unclaim`.\n'
                              f'If you want to see this message again type `{self.client.command_prefix}help`.',
                        inline=False)
        embed.add_field(name='Invite Bot',
                        value=f'[Link](https://discord.com/api/oauth2/authorize?'
                              f'client_id=771021720240783386&permissions=4212736&scope=bot)',
                        inline=True)
        embed.add_field(name='Support',
                        value=f'[Join](https://discord.gg/E6yuVmwxGM)',
                        inline=True)
        embed.add_field(name='Creator',
                        value=f'[Lars#7391](https://discord.gg/E6yuVmwxGM)',
                        inline=True)

        await ctx.send(embed=embed)

    @commands.command(name='prefix')
    @commands.has_permissions(administrator=True)
    async def set_prefix(self, ctx, *, prefix=None):
        if prefix is None:
            return

        try:
            # Set the new prefix
            self.client.set_prefix(prefix=prefix)

            # Update the prefix in the bot presence
            await self.client.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(type=discord.ActivityType.watching,
                                          name=f'out for imposters | {self.client.command_prefix}help'))

            embed = discord.Embed(
                description=f'The prefix has been changed to `{prefix}`',
                color=discord.Color.from_rgb(0, 255, 0)
            )
            await ctx.send(embed=embed)

            return

        except Exception:
            pass

        embed = discord.Embed(
            description=f'Please use the valid format: `{self.client.command_prefix}prefix <prefix>`',
            color=discord.Color.from_rgb(255, 0, 0)
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utils(client))
