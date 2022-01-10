import discord
from discord.ext import commands
import requests
cognamegeneral = 'general_commands'

class cognamegeneral(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#body

#/body

def setup(bot):
    bot.add_cog(cognamegeneral(bot))