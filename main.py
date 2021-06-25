

import discord
from discord.ext import commands

from __config__  import *
from __message__ import __MESSAGES__

files = [ discord.File(SAVE_FILE_PATH + file) for file in FILE_NAMES ]

bot = commands.AutoShardedBot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

@bot.command()
async def help(ctx):
    await ctx.send(embed= __MESSAGES__["helpEmbed"])

@bot.command()
async def connect(ctx):
    await ctx.send(embed= __MESSAGES__["connectEmbed"])

@bot.command()
async def caution(ctx):
    await ctx.send(embed= __MESSAGES__["cautionEmbed"])

@bot.command()
async def site(ctx):
    await ctx.send(embed= __MESSAGES__["siteEmbed"])

@bot.command()
async def getSave(ctx):
    await ctx.send(files=files)

@bot.event
async def on_member_join(member):
    await member.guild.get_channel(__CHANNEL_TOKEN__).send(member.mention + __MESSAGES__["__INIT__"])

bot.run(__TOKEN__)

