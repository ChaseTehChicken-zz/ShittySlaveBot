import discord
import random
from discord.ext import commands

sizes = ["1 Inch", "2 Inches", "3 Inches," "4 Inches", "5 Inches", "6 Inches", "7 Inches", "8 Inches", "9 Inches", "10 Inches", "11 Inches", "12 Inches"]

class pp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['peepee'])
    async def pp(self, ctx, member : discord.Member):
        if member == '':
            embed = discord.Embed(
               title=f'{ctx.author.name}, your peepee is {sizes} long!'
            )
            ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'{member}, your peepee is {sizes} long!'
            )
            ctx.send(embed=embed)

def setup(client):
    client.add_cog(pp(client))