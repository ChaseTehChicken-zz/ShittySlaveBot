import discord
from discord.ext import commands


class rank(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["perms"])
    async def rank(self, ctx):
        if ctx.author.id == 420454043593342977:
            await ctx.send(f"Your rank is Bot Owner..\nHello Chaseyy")
            return
        elif ctx.author.id == 298653078943694849:
            await ctx.send("Your rank is stinky bab\nHello Cosy")
            return
        elif ctx.author.id == 598274737730355200:
            await ctx.send("Your rank is soaked bab\nHello Wallow")
        else:
            await ctx.send("You are a Bot User")
        return

def setup(client):
    client.add_cog(rank(client))