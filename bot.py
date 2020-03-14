import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(688307584557383721)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(688307584557383721)
    await channel.send(f'{member} leave')



bot.run("Njg4MDYwMzc3Mjc5MzY1MjE1.XmyVJQ.Qm7I6QVt7FRp9_55_i0HcvKZsis")