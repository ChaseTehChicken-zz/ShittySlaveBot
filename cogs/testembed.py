import discord
from discord.ext import commands

class testembed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command
    async def testembed(self, ctx):
        embed = discord.Embed(title="title", description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(testembed(client))