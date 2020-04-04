import discord
import random
from discord.ext import commands
from itertools import cycle

class inspiration(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def inspiration(self, ctx):
        await ctx.send("yes no")


def setup(client):
    client.add_cog(inspiration(client))