import discord
from discord.ext import commands
import json

class suggest(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suggest(self, msg, ctx, *, usersuggest):
        file=open(r"Z:\Documents\Desktop\ShittySlaveBot-master\cogs\utils\suggestions.json", 'r')
        data=json.load(file)
        data.append(usersuggest)
        with open(r"Z:\Documents\Desktop\ShittySlaveBot-master\cogs\utils\suggestions.json", 'w') as f:
            f.write(str(json.dumps(data)))
            f.close()
        await ctx.send("Suggestion Added!")

def setup(client):
    client.add_cog(suggest(client))