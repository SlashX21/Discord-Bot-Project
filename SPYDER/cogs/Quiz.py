import discord
from discord.ext import commands
import requests
cognamemod = 'quiz'

class cognamemod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#body
    #clear messages
    @commands.command()
    async def clear1(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'{amount} messages cleared')

    #kick member
    @commands.command()
    async def kick1(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    #ban member
    @commands.command()
    async def ban1(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was banned from the server. Reason: {reason}')
#/body

def setup(bot):
    bot.add_cog(cognamemod(bot))
