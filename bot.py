from discord.ext import commands
from config import *
import os
import discord

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')


@client.command()
@commands.has_role(admin)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    print(f"loaded {extension}")
    await ctx.send(f"loaded {extension}")


@client.command()
@commands.has_role(admin)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"unloaded {extension}")
    await ctx.send(f"unloaded {extension}")


@client.command()
@commands.has_role(admin)
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    print(f"reloaded {extension}")
    await ctx.send(f"reloaded {extension}")


@client.command()
@commands.has_role(admin)
async def debug(ctx):
    client.unload_extension(f"cogs.listeners")
    print('''------------------------------------------------------
    You entered the debugmode
------------------------------------------------------
    ''')
    await ctx.send("you entered debug mode")


@client.command()
@commands.has_role(admin)
async def ext(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            embed = discord.Embed(
                title=f"Hier sind alle Cogs",
                colour=discord.Colour.dark_blue())

            embed.add_field(name="Cogs", value=filename, inline=True)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/710039508694859856/36cdca3ffaa8faee2bcd470ece7b1d58.png?size=256")
    await ctx.send(embed=embed)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename[:-3]} loaded")

print('''-------------------------------
Bot Online
--------------------------------
''')


client.run(token)