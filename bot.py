import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot 已上線")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTQ4MTYxMzU4MjI5Nzg1ODE1MA.GKOLow.jRHb33-sVcMk0NJYXdmoDt12Fl4khGm-wbZkiI")
