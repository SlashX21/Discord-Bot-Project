import discord
from discord.ext import commands
import requests
import json
cognameapi = 'api_commands'

class cognameapi(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#body
    #duke status
    @commands.command()
    async def duke(self, obj):
        response = requests.get('https://api.torn.com/user/4?selections=profile&key=AYrvjGqavnPgOeCR')
        hospital = response.json()["status"]
        await obj.send(f'Duke: {hospital}')

    #leslie status
    @commands.command()
    async def leslie(self, obj):
        response = requests.get('https://api.torn.com/user/15?selections=profile&key=AYrvjGqavnPgOeCR')
        hospital = response.json()['status']
        await obj.send(f'Leslie: {hospital}')
#/body

def setup(bot):
    bot.add_cog(cognameapi(bot))