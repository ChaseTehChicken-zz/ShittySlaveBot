import os
import json
import discord
from discord.ext import commands

class echo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['repeat', 'copy'])
    async def echo(self, channel, *, userInput):
        await channel.send(userInput)

def setup(client):
    client.add_cog(echo(client))
