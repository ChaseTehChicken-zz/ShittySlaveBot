import discord
import os 
import random
import nekos
from discord.ext import commands

#responses = ["https://media.tenor.com/images/b6d0903e0d54e05bb993f2eb78b39778/tenor.gif",
#"https://media.tenor.com/images/eed8d1a51f647b4be696879a0ad6f1f1/tenor.gif",
#"https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif",
#"https://media1.giphy.com/media/lrr9rHuoJOE0w/source.gif",
#"https://i.imgur.com/r9aU2xv.gif",
#"https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
#"https://media1.giphy.com/media/143v0Z4767T15e/giphy.gif"]

hugg = nekos.img("hug")

class cuddle(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def cuddle(self, ctx, member : discord.Member):
        nameLower = ctx.author.name.lower()
        if member == ctx.author.name:
            embed = discord.Embed(
            title=f'{ctx.author.name} cuddled themselves! How cute!')
            
            embed.set_image(url=f"{hugg}")
            await ctx.send(embed=embed)        
        else:
            embed = discord.Embed(
            title=f'{ctx.author.name} cuddled @{member}! How cute!')
            print(nameLower)
            
        embed.set_image(url=f"{hugg}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(cuddle(client))