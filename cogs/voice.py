import discord
from discord.ext import commands

class voice(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

def setup(client):
    client.add_cog(voice(client))