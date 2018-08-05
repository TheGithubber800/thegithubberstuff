import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="in Aguyuser's Community"))
    print ("k")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")
    print ("user has pinged")


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embid = discord.Embed(colour = discord.Colour.red())
    embid.set_author(name="List of available commands")
    embid.add_field(name="!ping" , value="Pong!", inline=False)
    embid.add_field(name="!kick", value= "Kicks a member.", inline=False)
    embid.add_field(name="!gay", value= "This is the big gay!", inline=False)
    embid.add_field(name="!warn", value="Work in process!", inline=False)
    await bot.say(embed=embid)


@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member, *, reason="No reason given"):
    if ctx.message.author.server_permissions.kick_members:
        em3 = discord.Embed(title= "KICK" , description= ("You have been kicked from Aguyuser's Community by ``{}``.".format(ctx.message.author)), colour=0x329FDB)
        em3.add_field(name="Reason", value=("{}".format(reason)))
        await bot.send_message(user, embed=em3)
        em1 = discord.Embed(title= 'Member kicked', description= ("Member ``{}`` has been kicked by ``{}``. Reason: {}".format(user.name, ctx.message.author, reason)) , colour=0x329FDB)
        await bot.say(embed=em1)
        await bot.kick(user)
    else:
            em2 = discord.Embed(title = 'Permissions missing', description= 'You are not allowed to do this', colour=0x329FDB)
            await bot.say(embed=em2)


@bot.command(pass_context=True)
async def fact():
    await bot.say("Your mom gay")



@bot.command(pass_context=True)
async def gay(ctx, user: discord.Member):
    await bot.say("{} is big gay".format(user.name))

@bot.command(pass_context=True)
async def pm(ctx, member: discord.Member, *, thing):
        await bot.send_message(member, thing)
        await bot.say("Message sent!")




    
bot.run("NDc0OTc4MzI2NzQ2NzU5MTc4.DkiRHA.D_pI6Q82hRQaLngtoWAIGk_3_wY")
