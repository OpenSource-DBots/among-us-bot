from discord.ext import commands
import discord


class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')  # Remove the default help command

    @commands.command(name='help', aliases=['h', 'info'])
    async def help(self, ctx):
        embed = discord.Embed(title='Among Us Bot Information', color=discord.Color.from_rgb(0, 125, 0))
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='Standard Commands',
                        value='.claim\n'
                              '.unclaim',
                        inline=True)
        embed.add_field(name='Advance Commands',
                        value='.prefix',
                        inline=True)
        embed.add_field(name='How does this bot work?',
                        value='You have to join a voice channel in order to `.claim` it. When you have claimed the '
                              'voice channel - whenever you mute yourself, the other will be muted as well. And '
                              'whenever you unmute yourself, the other will be unmuted as well. If you do not want to '
                              'be a party leader anymore, simply type `.unclaim`.\n'
                              'If you want to see this message again type `.help`.',
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
    async def set_prefix(self, ctx, *, prefix):
        embed = discord.Embed(
            description='This command has not been created yet.',
            color=discord.Color.from_rgb(125, 0, 0)
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utils(client))
