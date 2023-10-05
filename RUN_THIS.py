import requests
# import json
import discord
from discord.ext import commands

#players = requests.get('ip/status')
bot = discord.Client(intents=discord.Intents.all(), command_prefix='>')
bot_token = "hide"
client = commands.Bot(command_prefix='>', intents=discord.Intents.all())

@bot.event
async def on_message(message):
    if message.content.startswith("ping"):
        await message.channel.send("Pong!")

@bot.event
async def on_ready():
    print("Бип-буп! Запуск успешный!")
    await bot.change_presence(activity=discord.Game(name="Breaking Facility"))

# @client.command
# async def hello(ctx):
#     await ctx.send("Hi!")

server_status = requests.get('195.189.16.224:1212/status')
@bot.event
async def on_message1(message):
    if message.content.startswith("status"):
        await message.channel.send(server_status)

bot.run(bot_token)
