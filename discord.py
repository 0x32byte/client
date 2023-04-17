import discord
from discord.ext import commands

prefix = ">"
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("[   INFO ] Discord Connected")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="TheAngels"))

@bot.command()
async def ping(ctx):
      await ctx.send("Pong !")

bot.run("MTA5MTUzMjE1ODEwNTAzNDg3Mw.GyoE8l.1Jgs3G3ZRS5yXfPvk3mzwclZcRkM1AsNV9EPeU")
