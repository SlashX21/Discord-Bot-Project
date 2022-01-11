import discord
from discord.ext import commands
from discord.utils import get
import requests
import json
import random
import asyncio
import datetime
import time
from random import randint
import math
from cryptography.fernet import Fernet
from newsapi import NewsApiClient

bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command('help')
#activate bot
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=1, name='with Merlin'))
    print("Ready to take off")

@bot.command()
async def shutdown(self,ctx):
    if ctx.message.author.id == 702048286789599323:
      print("shutdown")
      try:
        await self.bot.logout()
      except:
        print("EnvironmentError")
        self.bot.clear()
    else:
      await ctx.send("You do not own this bot!")
#<test>



@bot.command()
async def timer(ctx): 
    await ctx.send('How many day(s)?: ')
    msg = await bot.wait_for('message')
    arg1 = int(msg.content)
    await ctx.channel.purge(limit=2)

    await ctx.send('How many hour(s)?: ')
    msg = await bot.wait_for('message')
    arg2 = int(msg.content)
    await ctx.channel.purge(limit=2)
    await ctx.send('How many minute(s)?: ')
    msg = await bot.wait_for('message')
    arg3 = int(msg.content)
    await ctx.channel.purge(limit=2)
    await ctx.send('How many seconds(?): ')
    msg = await bot.wait_for('message')
    arg4 = int(msg.content)
    await ctx.channel.purge(limit=2)
    seconds_in_days = int(arg1)*86400
    seconds_in_days = int(arg2)*3600
    seconds_in_minutes = int(arg3)*60
    seconds_in_seconds = int(arg4)
    seconds_left = (seconds_in_days+seconds_in_days+seconds_in_minutes+seconds_in_seconds)
    await ctx.send('```timer has started for {a} day(s) {b} hour(s) {c} minute(s) and {d} second(s)```'.format(a = arg1, b = arg2, c = arg3, d = arg4))
    time.sleep(seconds_left)
    await ctx.send('```Time is up```')
    
@bot.command()
async def calc(ctx, *, arg):
    calculation = int(eval(arg))
    await ctx.send(calculation)

@bot.command()
async def quadratic(ctx):
    await ctx.send('coefficient of x^2: ')
    msg = await bot.wait_for('message')
    a = int(msg.content)
    print(a)
    await ctx.channel.purge(limit=2)
    await ctx.send('coefficient of x: ')
    msg = await bot.wait_for('message')
    b = int(msg.content)
    await ctx.channel.purge(limit=2)
    await ctx.send('constant term: ')
    msg = await bot.wait_for('message')
    c = int(msg.content)
    await ctx.channel.purge(limit=2)
    solution_1 = float(((-b) + math.sqrt((b ** 2.0) - (4.0 * a * c)))/(2.0*a))
    solution_2 = float(((-b) - math.sqrt((b ** 2.0) - (4.0 * a * c)))/(2.0*a))
    await ctx.send('The solution for {} x^2 + {} x + {} is x = {} and x = {}'.format(a, b, c, "%.3f" % solution_1, "%.3f" % solution_2))

# @bot.command()
# async def settimer(ctx, day, hour, mins):
#     global time_left
#     seconds_in_day = (int(day)*86400)
#     seconds_in_hour = (int(hour)*3600)
#     seconds_in_min = (int(mins)*60)
#     time_left = (time_in_day+time_in_hour+time_in_min)



@bot.command()
async def encrypt(ctx, *, arg):
    global cipher_text
    global key
    plain_text = arg
    key = b'OQXYGo3OzywwgBbU8ZOLQ4VfBnLhoQGWQ_NyaCJhRgA='
    fernet = Fernet(key)
    cipher_text = fernet.encrypt(b'plain_text')
    await ctx.send(cipher_text)

@bot.command()
async def decrypt(ctx):
    global cipher_text
    global key
    fernet = Fernet(key)
    plain_text = fernet.decrypt(cipher_text)
    await ctx.send(plain_text)

# @bot.command()
# async def runtimer(ctx):
#     global time_left
#     embed1 = discord.Embed(title="Timer Starts!")
#     await ctx.send(embed=embed1)
#     while time_left>0:
#         time_left -= 1
#         await asyncio.sleep(1)
#     else:
#         embed2 = discord.Embed(title="Time's UP!!!")
#         await ctx.send(embed=embed2)


# @bot.command()
# async def timeleft(ctx):
#     global time_left
#     Time_to_show = (str(datetime.timedelta(seconds = time_left)))
#     embed = discord.Embed(title=f'time left : {Time_to_show}')
#     await ctx.send(embed=embed)


@bot.command()
async def magic8(ctx, arg1):
    response = ['You can do it', 'maybe you should find a better way', 'trust the people around you', 'forget about it', 'you deserve better', 'you just suck', 'believe in yourself', 'Work for it']
    words = random.choice(response)
    embed1 = discord.Embed(title=words, color=0xf1c40f)
    await ctx.send(embed=embed1)

@bot.command()
async def maths(ctx):
    global game_timer
    global player_score
    game_timer = 40
    player_score = 0
    def wrapper(context):
        def check_msg(message):
            return context.author == message.author and context.channel == message.channel
        return check_msg


@bot.command()
async def help1(ctx):
    embed = discord.Embed(
        title = 'Help Center',
        description = 'This are the commands available \n $settimer to set a timer using the format of $settimer day hour min \n $runtimer to run the timer \n $timeleft to check the remaining time of the timer \n $magic8 is used for fortune telling by typing your question after the code'
    )
    await ctx.send(embed=embed)
#</test>

@bot.command()
async def news(ctx, *, keyword):
    news_request = requests.get(f'https://newsapi.org/v2/everything?q={keyword}&pageSize=5&apiKey=f48caecd17044caab83abd99edc58135').json()
    newslist = news_request['articles']
    titles = []
    descriptions = []
    urls = []
    for info in newslist:
        titles.append(info['title']) 
        descriptions.append(info['description'])
        urls.append(info['url'])
    for i in range(5):
        embed = discord.Embed(title=titles[i], description = descriptions[i], url = urls[i])
        # await ctx.send(f"```{titles[i]}\n\n{descriptions[i]}\n\n```{urls[i]}")
        await ctx.send(embed=embed)

#3nB6qJgepDm3vuNb6YjQMw==
bot.run('NzA3NTgwMTcwODczMDc3Nzkx.XrK3Yg.JVujLWfgRkBe2cv0wAqs43NtiX4')