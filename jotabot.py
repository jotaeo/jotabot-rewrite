
import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="j!")
TOKEN = 'NDI3MTcwMjk1MjI5NDQ4MTk1.DZgpUA.IVDG3A2mb3owOEKJ0Ez1Frup7YE'

@bot.command ()
async def test(ctx):
    await ctx.send("test")


@bot.command()
async def say(ctx, * ,msg):

    await ctx.send (msg)

@bot.command ()
async def math (ctx,a:int,b,c:int):
    if b== '+':
        await ctx.send (a+c)
    if b== "-":
        await ctx.send (a-c)
    if b== "*":
        await ctx.send (a*c)
    if b== "/":
        await ctx.send (a/c)


@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))




bot.run(TOKEN, bot=True, reconnect=True)
