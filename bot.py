import discord 
import random 
import os 
import json 
import config 
import logging 
import nekos 
import requests 
from discord.ext import commands 
from discord.ext import tasks 
from itertools import cycle 

client = commands.Bot(command_prefix = "slave.")
logging.basicConfig(level=logging.INFO)
status = cycle(['Currently searching for toilet paper',
    'Coles has no toilet paper',
    'Woolworths has no toilet paper',
    'Anyone selling toilet paper?',
    'Toilet Paper wont save you from Coronavirus smh',
    'How am I supposed to wipe my fuckin arse??'])

version = "0.3"
dpyVersion = discord.__version__
serverCount = len(client.guilds)
memberCount = len(set(client.get_all_members()))

@client.event
async def on_ready():
    change_status.start()
    print('logged in as') 
    print(client.user.name)
    print(client.user.id)
    


@client.event
async def on_command_error(ctx, error):
    if ctx.author.id == 420454043593342977:
        await ctx.channel.send("You done did fucked up chaseyy")
    else:
        await ctx.channel.send("Oh shit! I've had an error! Please try again or alert @Chaseyy#9999!")

@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}') 
 
@client.command() 
async def stats(ctx): 
 
 
    embed = discord.Embed( 
        title=f'{client.user.name} Stats',  
        description="\uFEFF", 
        colour=ctx.author.colour, 
        timestamp=ctx.message.created_at) 
 
    embed.add_field(name='Bot Version:', value=version)
    embed.add_field(name='Discord.Py Version', value=dpyVersion)
    embed.add_field(name='Total Guilds:', value=serverCount)
    embed.add_field(name='Total Users:', value=memberCount)
    embed.add_field(name='Bot Developers:', value="<@420454043593342977>")

    embed.set_footer(text=f"Carpe Noctem | {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)


@client.command(aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

@load.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command Unavaliable')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')


@client.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'successfully kicked: {member} for reason: {reason}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'successfully banned: {member} for reason: {reason}')
    print(f'Member {member} banned with reason: {reason}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_descriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_descriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Sucessfully unbanned {user}')
            print(f'Member unbanned: {member}')
            return

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("NjgxNDA3NTMwMzQxMzY3ODA5.XohXDg.W-o4IRRV0miOaRZAPVyi3WPz5lY")