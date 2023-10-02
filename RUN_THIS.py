import requests
import json
import discord
from discord.ext import commands

#players = requests.get('ip/status')
bot = discord.Client(intents=discord.Intents.all(), command_prefix='>')
bot_token = "hide"
client = commands.Bot(command_prefix='>', intents=discord.Intents.all())

@bot.event
async def on_message(message):
    if message.content.startswith("ping"): #crtl
        await message.channel.send("Pong!")

@bot.event
async def on_ready():
    print("Бип-буп! Запуск успешный!")

@client.command
async def hello(ctx):
    await ctx.send("Hi!")

# @client.command()
# async def ping(ctx):
#     await ctx.send("Pong")

bot.run(bot_token)
