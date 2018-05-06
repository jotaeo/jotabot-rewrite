
import discord
from discord.ext import commands
import asyncio
import json

def fetch_config():
    config_file = open("config.json")
    config = json.load(config_file)
    return config

bot = commands.Bot(command_prefix="j!")
config = fetch_config()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! `{bot.latency}`")
    
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

    

bot.run(config["TOKEN"], bot=True, reconnect=True)
