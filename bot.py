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

bot.run("MTQ4MTYxMzU4MjI5Nzg1ODE1MA.G20zs3.S0l3mfsqsUmjZvpiYrVek-7Yy0NjCw3FYcDJc8")
