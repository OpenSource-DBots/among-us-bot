import discord

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')


token = open('token.secret', 'r')

client = BotClient()
client.run(token.read())
