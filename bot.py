import discord
from discord.ext import commands
import os

TOKEN = os.getenv("MTQ1MTUzMjA1MjY4Njk2NjkyNQ.GwkzXw.jxEkb0nnb8cBdHVuvJlMOpVPhJOLwHBWnvmA6g")
LOG_CHANNEL_ID = int(os.getenv("1451521015531311165"))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(LOG_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="📥 멤버 입장",
            description=f"{member.mention} 님이 서버에 입장했습니다.",
            color=0x00ff00
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(LOG_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="📤 멤버 퇴장",
            description=f"{member.name} 님이 서버에서 퇴장했습니다.",
            color=0xff0000
        )
        await channel.send(embed=embed)

bot.run(MTQ1MTUzMjA1MjY4Njk2NjkyNQ.GwkzXw.jxEkb0nnb8cBdHVuvJlMOpVPhJOLwHBWnvmA6g)

