from discord.ext import commands
import discord
from config import *


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx):
        await ctx.send("lol")


def setup(bot):
    bot.add_cog(User(bot))
