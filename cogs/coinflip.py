import discord
from discord.ext import commands
import random

class coinflip(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def coinflip(self, ctx):
        responses = ['Heads',
        'Tails']
        await ctx.send(f'{(random.choice(responses))}')

def setup(client):
    client.add_cog(coinflip(client))