import discord
from discord.ext import commands

class Example(commands.Cog):

    def ___init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello')

def setup(client):
    client.add_cog(Example(client))