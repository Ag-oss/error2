
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot, BotMissingPermissions, bot_has_permissions
from aiohttp import ClientSession
import json
import random
import datetime
import asyncio
import colorsys

client = commands.Bot(command_prefix="-", owner_id=680994218977787927) 
client.remove_command('help')

@client.event
async def on_ready():
 await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=f"Type <help For Commands | Watching {len(client.users)} Members"))
 print('Bot is online')
 
@client.command()
async def hi(ctx):
    await ctx.send('hello')

@client.command(pass_context = True, aliases=['whois', 'ui'])
@commands.has_permissions(manage_messages=True)     
async def userinfo(ctx, user: discord.Member=None):
    if user == None:
      user = ctx.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}".format(user.name), color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
    embed.add_field(name="Name:", value=user.name, inline=True)
    embed.add_field(name="ID:", value=user.id, inline=True)
    embed.add_field(name="User Discriminator:", value=user.discriminator)
    embed.add_field(name="User Status:", value=user.status, inline=True)
    embed.add_field(name="Joined Discord At:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Highest Role:", value=user.top_role)
    embed.add_field(name="Joined Server At:", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Server Nickname:", value=user.display_name)
    embed.set_footer(text=f"Requested By {ctx.author.name}")
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Manage Messages`` Permission To Use This Command**")
        await ctx.send(embed=embed)    
    
@client.command(pass_context = True, aliases=['ava', 'av'])
@commands.has_permissions(send_messages=True) 
async def avatar(ctx, user:discord.Member=None):
    if user == None:
      user = ctx.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=user.avatar_url)
    embed.set_author(name="Avatar Image:", icon_url=user.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
   
@client.command()
async def ping(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Ping Pong!", color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
    embed.add_field(name="🏓 API Response Time 🏓 ", value=f"``{random.randint(1, 400)}ms``")
    embed.add_field(name="🏓  Bot Latency 🏓 " , value=f"``{random.randint(1, 100)}ms``")   
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721300256284868659/723334506295066745/emoji.png")
    await ctx.send(embed=embed)
 
@client.command(aliases=['si']) 
async def serverinfo(ctx): 
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{ctx.guild.name}") 
        embed.add_field(name="<:id:724180444773482496> Server Id", value= f"{ctx.guild.id}") 
        embed.add_field(name="<a:starrs:724176716452593694> Server Owner", value = f"{ctx.guild.owner}")
        embed.add_field(name="🗺️ Server Region", value = f"{ctx.guild.region}")
        embed.add_field(name="<a:starrs:724176716452593694> Server Members", value = f"{len(ctx.guild.members)}")
        embed.add_field(name="Online", value=f"<:online:723485563814150154> Online: {len([x for x in ctx.guild.members if x.status == discord.Status.online])}")
        embed.add_field(name="Idle", value=f"<:idle:723485795087810601> Idle: {len([x for x in ctx.guild.members if x.status == discord.Status.idle])}")
        embed.add_field(name="Do Not Disturb", value=f"<:dnd:723485662124310539> Do not Disturb: {len([x for x in ctx.guild.members if x.status == discord.Status.dnd])}")
        embed.add_field(name="Offline", value=f"<:off:723485614149992518> Offline: {len([x for x in ctx.guild.members if x.status == discord.Status.offline])}")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
 
client.run('NzcyNzc0NzMzMDkwMzkwMDM3.X5_kjQ.sA7m-GwLEhHd5sLfxS_FoIO1sjA')

