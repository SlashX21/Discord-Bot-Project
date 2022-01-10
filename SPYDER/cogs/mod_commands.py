import discord
from discord.ext import commands
import requests
cognamemod = 'mod_commands'

class cognamemod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#body
    #clear messages
    @commands.command()
    @commands.has_role('developer')
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'{amount} messages cleared')

    #kick member
    @commands.command()
    @commands.has_role('developer')
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    #ban member
    @commands.command()
    @commands.has_role('developer')
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was banned from the server. Reason: {reason}')
#/body

def setup(bot):
    bot.add_cog(cognamemod(bot))