import discord
from discord.ext import commands

import asyncio

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('client.run'))
        print("general kenobi")

    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Commands does not exist. Try .help to see the available commands')
            



        if isinstance(error, commands.MissingAnyRole):
            msg = await ctx.send(f'Sorry {ctx.message.author.mention}, you do no have the permission for that')

            await asyncio.sleep(3)
            await msg.delete()
            await ctx.message.delete()


def setup(client):
    client.add_cog(Events(client))    
        