import discord
from discord.ext import commands

class Test(commands.Cog):

    def ___init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send('Yea its working mate')

def setup(client):
    client.add_cog(Test(client))