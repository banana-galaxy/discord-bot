#!/usr/bin/python3





'''
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client.run

bot.run('MjU5ODE5OTQwOTE0MTM1MDQw.C5zK6g.m1YjQS1Mhateuo3-xdUSXn83-No')
'''
import discord
from discord.ext import commands
import random
import os, asyncio
#import money

home = os.getenv("HOME")
path = os.path.dirname(os.path.abspath(__file__))

#import bothelp.py

prefix = '-'

description = '''A bot to explore the possibilities of programming'''
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=True)

bot.remove_command("help")

'''@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name=prefix+"help"))
    #print('loading cogs...')
    #bot.load_extension('staff')
    #bot.load_extension('fun')
    #print('cogs loaded')'''


# bot commands

'''@bot.event
async def on_message(message):
    print("The message's content was", message.content)

'''
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("prefix \"-\""))


'''@bot.event
async def on_command(ctx):
    if "mod" in [y.name.lower() for y in ctx.author.roles]:
        print("works")'''

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


@bot.command()
async def invite(ctx):
    await ctx.send("<https://discordapp.com/oauth2/authorize?client_id=646839288188895244&scope=bot&permissions=8>")


@bot.command(pass_context=True)
async def unload(ctx, cog: str):
    '''only available to bot developers'''
    if str(ctx.message.author) == "banana-galaxy#9812":
        bot.unload_extension(cog)
        await ctx.send(f"{str(cog)} unloaded")
    else:
        await ctx.send(f"{ctx.author.mention} this command is only for devs")


@bot.command(pass_context=True)
async def load(ctx, cog: str):
    '''only available to bot developers'''
    if str(ctx.message.author) == "banana-galaxy#9812":
        bot.load_extension(cog)
        await ctx.send(f"{cog} loaded")
    else:
        await ctx.send(f"{ctx.author.mention} this command is only for devs")


@bot.command(pass_context=True)
async def reload(ctx, cog: str):
    '''only available to bot developers'''
    if str(ctx.message.author) == "banana-galaxy#9812":
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await ctx.send(f"{str(cog)} reloaded")
    else:
        await ctx.send(f"{ctx.author.mention} this command is only for devs")


@bot.command()
async def test(ctx):
    msg = await ctx.send("test")
    await asyncio.sleep(2)
    await msg.edit(content="test1")
    #emoji = discord.utils.get(bot.get_all_emojis(), name='arrow_up')
    await msg.add_reaction('\:arrow_up:')

bot.run('NjQ2ODM5Mjg4MTg4ODk1MjQ0.XfF0DA.HOfglXKNZfVxN0Mf737eGY2caFM')
