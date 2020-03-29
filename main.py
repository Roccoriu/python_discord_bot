import os

from random import *

import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'bin.{extension}')



@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'bin.{extension}')



for filename in os.listdir('./bin'):
    if filename.endswith('.py'):
        client.load_extension(f'bin.{filename[:-3]}')



client.run('')