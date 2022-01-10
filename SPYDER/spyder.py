#spyder.py
import discord
from discord.ext import commands, tasks
import requests
import asyncio
import json
import os
import datetime

bot = commands.Bot(command_prefix='/', case_insensitive=True)
bot.remove_command('help')

#activate bot
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=1, name='TORN'))
    print("Ready to kick some ass")

#assign newly joined members with unverified role and a display a welcome message in embed
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='unverified')
    await member.add_roles(role, reason=None, atomic=True)

    embed = discord.Embed(title="Welcome to the faction's official discord server", colour=discord.Colour(0x50e3c2), description="To verify, use the /verify command followed by your torn_name and torn_id. For example: /verify abcde 12345")
    embed.set_thumbnail(url='https://w7n4r7h4.stackpathcdn.com/wp-content/uploads/2018/07/Spyder-Logo.png')
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = bot.get_channel(id=642607479636623361)
    channel1 = bot.get_channel(id=642606741561016330)

    await channel.send(embed=embed)
    await channel1.send(f'```{member.name}#{member.discriminator} <{member.nick}> has joined the server\n{datetime.datetime.utcnow()}```')

#sends a notification about the member who has been kicked
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(id=642606741561016330)
    await channel.send((f'```{member.name}#{member.discriminator} <{member.nick}> has been removed from the server\n{datetime.datetime.utcnow()}```'))

#sends a notification about the member who has been banned
@bot.event
async def on_member_ban(member):
    channel = bot.get_channel(id=642606741561016330)
    await channel.send((f'```{member.name}#{member.discriminator} <{member.nick}> has been banned from the server\n{datetime.datetime.utcnow()}```'))

#<body>
#show ping
@bot.command()
async def ping(ctx):
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(f'{round(latency * 1000)} ms')


#promote a member to the role developer
@bot.command()
@commands.has_role('Developer')
async def mod(ctx, member : discord.Member):
    role = discord.utils.get(member.guild.roles, name='Moderator')
    await member.add_roles(role)
    await ctx.channel.purge(limit=1)
#</body>

#cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('loaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('unloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#help command
@bot.command()
async def help(ctx):
    await ctx.send('Command list: \n/ping (show ping) \n/kick (kick a member) \n/ban (ban a member) \n/clear (clear 10 messages if theres no amount specified) \n/duke (duke status) \n/leslie (leslie status)')

#3nB6qJgepDm3vuNb6YjQMw==
bot.run('NjIzOTE0MzY2MjE5MzIxMzU1.XYREmA.zgARSMv-gR0DdBdvgnC7Fpb0Sng')