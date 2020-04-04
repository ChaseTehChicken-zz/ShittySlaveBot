import discord
from discord.ext import commands

chaseyy_id = 420454043593342977

class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == chaseyy_id:
            role = discord.utils.get(member.server.roles, name='mooted')
            await ctx.add_roles(member, role)
            embed = discord.Embed(title="User muted!")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(mute(client))