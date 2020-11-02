from discord.ext import commands
import discord


class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')  # Remove the default help command

    @commands.command(name='help', aliases=['h', 'info'])
    async def help(self, ctx):
        embed = discord.Embed(title='Among Us Bot Information')
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name='Standard Commands',
                        value='.claim\n'
                              '.unclaim',
                        inline=True)
        embed.add_field(name='Advance Commands',
                        value='.prefix',
                        inline=True)
        embed.add_field(name='How does this bot work?',
                        value='There must be one **Party Leader** to control the other voice activity in the claimed '
                              'channel. You can claim a voice channel by entering it and typing `.claim`. This command '
                              'will assign you as **Party Leader** in that voice channel you are in. If you want to '
                              'give the Party Leader to someone else - simply type `.unclaim` so someone else can '
                              'claim it.',
                        inline=False)
        embed.add_field(name='Invite Bot',
                        value=f'[Link](https://discord.com/api/oauth2/authorize?client_id=771021720240783386&permissions=4212736&scope=bot)',
                        inline=True)
        embed.add_field(name='Support',
                        value=f'[Join](https://discord.gg/E6yuVmwxGM)',
                        inline=True)
        embed.add_field(name='Creator',
                        value=f'[Lars#7391](https://discord.gg/E6yuVmwxGM)',
                        inline=True)

        await ctx.send(embed=embed)

    @commands.command(name='set-prefix', aliases=['setprefix', 'sp', 'prefix'])
    async def set_prefix(self, ctx, prefix):
        pass


def setup(client):
    client.add_cog(Utils(client))
