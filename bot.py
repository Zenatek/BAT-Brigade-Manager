from discord import channel
import requests
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import time
import os
from datetime import datetime


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='YOU!'))

async def on_message(message):
    user = message.author
    ch = message.channel.id
    if ch == 905246431298875453:
      # Delete message if they aren't of Invite tracker bot
      if user.id != 720351927581278219:
        await message.delete()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string +" "+ str(user) + " " + str(message.content))
    elif ch == 903398764885200916:
      # Delete message if they aren't of MEE6 bot
      if user.id != 159985870458322944:
        await message.delete()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string +" "+ str(user) + " " + str(message.content))




if __name__ == '__main__':
    print("Running")
    client.run(os.environ.get('BATMANAGER'))