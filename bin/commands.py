import discord
from discord.ext import commands

import asyncio

from random import *

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency of {round(self.client.latency * 1000)} ms')


    @commands.command(aliases = ['8ball'])
    async def eight_ball(self, ctx, *, question):
        responses = ['it is certain.', 
                    'without a doubt',
                    'perhaps',
                    'not a chance']

        await ctx.send(f'Question: {question} \nAnswer: {choice(responses)}')


    @commands.command()
    @commands.has_any_role('Admin', 'Mods', 'Dev')
    async def clear(self, ctx, message_count = 5):
        await ctx.channel.purge(limit = message_count)
        msg = await ctx.send(f'{message_count} messages cleared')
        
        await asyncio.sleep(3)
        await msg.delete()
        await ctx.message.delete()


    @commands.command()
    @commands.has_any_role('Admin', 'Mods', 'Dev')
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        msg = await ctx.send(f'Kicked {member.mention}')

        await asyncio.sleep(3)
        await msg.delete()
        await ctx.message.delete()


    @commands.command()
    @commands.has_any_role('Admin', 'Mods', 'Dev')
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)
        msg = await ctx.send(f'Banned {member.mention}')

        await asyncio.sleep(3)
        await msg.delete()
        await ctx.message.delete()



    @commands.command()
    @commands.has_any_role('Admin', 'Mods', 'Dev')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for ban in banned_users:
            user = ban.user

            if (user.name, user.discriminator) == (member_name, member_disc):
                await ctx.guild.unban (user)
                msg = await ctx.send(f'Unbanned {user.name}#{user.discriminator}')

                await asyncio.sleep(3)
                await msg.delete()
                await ctx.message.delete()


def setup(client):
    client.add_cog(Commands(client))   