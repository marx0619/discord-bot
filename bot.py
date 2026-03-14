import discord
from discord.ext import commands
import os

# 權限設定
intents = discord.Intents.default()
intents.message_content = True

# 建立機器人
bot = commands.Bot(command_prefix="!", intents=intents)

# 機器人上線
@bot.event
async def on_ready():
    print(f"{bot.user} 已上線!")

# 測試指令
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# 從 Railway 讀 TOKEN
TOKEN = os.getenv("TOKEN")

# 如果沒抓到 TOKEN
if TOKEN is None:
    print("❌ 沒有讀到 TOKEN")
else:
    print("✅ TOKEN 已讀取")

bot.run(TOKEN)
