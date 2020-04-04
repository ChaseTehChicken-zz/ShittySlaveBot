import discord
import random
import os
from discord.ext import commands

responses = ["https://i.pinimg.com/originals/fe/a7/9f/fea79fed0168efcaf1ddfb14d8af1a6d.gif",
"https://66.media.tumblr.com/2d29fdbf47fd756caaea08f44b7eac92/tumblr_inline_ow4u7pIhWJ1u544cj_540.gif",
"https://media1.tenor.com/images/16662667791fc3275c25db595fdf89f8/tenor.gif?itemid=12374065",
"https://46.media.tumblr.com/b6406e8acd03a03f83b55db5082fcad7/tumblr_ohs63qIx0R1vpbklao1_500.gif"]

class tickle(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def tickle(self, ctx, *, user):
        nameLower = ctx.author.name.lower()
        if user == nameLower:
            embed = discord.Embed(
            title=f'{ctx.author.name} tickled themselves! How cute!')
            
            embed.set_image(url=f"{random.choice(responses)}")
            await ctx.send(embed=embed)
        
        else:
            embed = discord.Embed(
            title=f'{ctx.author.name} tickled {user}! How cute!')
            print(nameLower)
            
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(tickle(client))