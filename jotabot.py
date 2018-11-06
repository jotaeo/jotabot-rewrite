
import discord
from discord.ext import commands
import asyncio
import json

def fetch_config():
    config_file = open("config.json")
    config = json.load(config_file)
    return config

bot = commands.Bot(command_prefix="a!")
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
    if a == "9" and b == "+" and c == "10":
        await ctx.send ("21")
    if b== '+':
        await ctx.send (a+c)
    if b== "-":
        await ctx.send (a-c)
    if b== "*":
        await ctx.send (a*c)
    if b== "/":
        await ctx.send (a/c)
   

        
@bot.command ()
async def shrug (ctx):
    await ctx.send ("¯\_(ツ)_/¯")
    
@bot.command ()
async def test2 (ctx):
    await ctx.send ("Git test")
    
@bot.command ()
async def Info (ctx):
    await ctx.send ("Bot name: aigisbot")
    await ctx.send ("code used : python , discord.py rewrite")
    await ctx.send ("help commands ``a!help``")
    
@bot.command()
async def kimiwane (ctx):
    await ctx.send ("*tashikani ano toki watashi no sonara ni ita*")
    await ctx.send  ("*Itsudatte itsudatte itsudatte sugu yoko de waratte ita*")
    await ctx.send  ("*Naku shite mo torimodosu kimi wo* ``I will never leave you``")
    
@bot.command()
async def yamete (ctx):
    await ctx.send ("*yamete kudastop*")
 
bot.remove_command('help')

@bot.command()
async def help (ctx): 
    await ctx.send ("a!math : a math command , be sure to add a space")
    await ctx.send ("         between each variable , the follwing ")
    await ctx.send ("         are the commands you can use with it:")
    await ctx.send ("                  + : addition")
    await ctx.send ("                  - : subtraction")
    await ctx.send ("                  / : division")
    await ctx.send ("                  * : multiplication") 
    await ctx.send ("a!ping : shows ping of the bot server")
    await ctx.send ("a!info : shows basic info of the bot")
    

bot.run(config["TOKEN"], bot=True, reconnect=True)
