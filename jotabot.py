
import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="j!")
TOKEN = 'NDI3MTcwMjk1MjI5NDQ4MTk1.DZgpUA.IVDG3A2mb3owOEKJ0Ez1Frup7YE'

@bot.command ()
async def test(ctx):
    await ctx.send("test")






bot.run(TOKEN, bot=True, reconnect=True)
