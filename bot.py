import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot 已上線")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("TOKEN"))
