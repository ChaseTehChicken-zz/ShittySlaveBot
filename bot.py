import discord
import random
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix = "slave.")
status = cycle(['Currently searching for toilet paper',
    'Coles has no toilet paper',
    'Woolworths has no toilet paper',
    'Anyone selling toilet paper?',
    'Toilet Paper wont save you from Coronavirus smh',
    'How am I supposed to wipe my fuckin arse??'])



@client.event
async def on_ready():
    change_status.start()
    print('logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_command_error(ctx, error):
    pass

@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


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
            return


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run("NjgxNDA3NTMwMzQxMzY3ODA5.XmTVkg.P6mHlL47RQYEYfsU91_gm4t4rp8")