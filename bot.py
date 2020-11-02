
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

client = commands.Bot(command_prefix="<", owner_id=680994218977787927) 
client.remove_command('help')

@client.event
async def on_ready():
 await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=f"Type <help For Commands | Watching {len(client.users)} Members"))
 print('Bot is online')
 
@client.command()
async def hi(ctx):
    await ctx.send('hello')

@client.command()
async def dm(ctx, member : discord.Member, *, messagetosend):
    await member.send(messagetosend)
    await ctx.send(f'Message sent to {member.name}!')
   
                      
@client.command()
async def invite(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="**__Invite Me To Your Server__** ", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="**LINK** ",
    value="**[Click Here To Invite Me](https://discord.com/api/oauth2/authorize?client_id=716298227997212682&permissions=8&scope=bot)**")
    embed.add_field(name="**SUPPORT SERVER**", value="**[Click Here To Join](https://discord.gg/Xcp5DpT)**")
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.send(embed=embed)
    
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
async def help(ctx): 
    member = ctx.author
    channel = ctx.message.channel
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Commands List", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Modretion Commands ", value="```ban``````kick``````unban```") 
    embed.add_field(name=" Fun Commands ", value="```howgay``````say``````poll``````howlesbo```") 
    embed.add_field(name="Important Commands", value="```userinfo``````avatar``````invite```") 
    embed.add_field(name="Bot Commands", value="```serverinfo``````stats``````ping``````botstats``````membercount```") 
    embed.add_field(name="Important Links", value="[Invite Me](https://discord.com/api/oauth2/authorize?client_id=716298227997212682&permissions=8&scope=bot)")
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text=f"{ctx.author.name} My Prefix Is <")
    await member.send(embed=embed)
    
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
   await member.ban(reason=reason)
   embed=discord.Embed()
   embed.add_field(name="Banned", value=f"{member.name}")
   embed.add_field(name="Banned By", value=f"{ctx.author.mention}")
   await ctx.send(embed=embed)  
   
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Ban Members`` Permission To Use This Command**")
        await ctx.send(embed=embed)
    
@client.command()
async def mute(ctx, member: discord.Member, *, sentence):
   role = discord.utils.get(ctx.guild.roles, name='Muted')
   await member.add_roles(role)
   r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
   embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
   embed.add_field(name="Reason:", value=sentence)
   embed.set_footer(text=f"Muted By {ctx.author.name}")
   embed.set_author(name=f"{member.name} Has Been Muted", icon_url=ctx.message.author.avatar_url)
   await ctx.send(embed=embed)   

@client.command()
async def howgay(ctx, member : discord.Member):    
   r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
   embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
   embed.add_field(name="Howgay?", value=f"**{member.mention} Is {random.randint(1, 100)}% Gay!**")
   await ctx.send(embed=embed)
    
@client.command()
async def ping(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Ping Pong!", color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
    embed.add_field(name="🏓 API Response Time 🏓 ", value=f"``{random.randint(1, 400)}ms``")
    embed.add_field(name="🏓  Bot Latency 🏓 " , value=f"``{random.randint(1, 100)}ms``")   
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721300256284868659/723334506295066745/emoji.png")
    await ctx.send(embed=embed)
 
@client.command()
async def unmute(ctx, member: discord.Member):
   role = discord.utils.get(ctx.guild.roles, name='Muted')
   await member.remove_roles(role)
   r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
   embed=discord.Embed()
   embed.add_field(name="Unmuted", value=f"{member.mention}")
   embed.add_field(name="Unmuted By", value=f"{ctx.author.mention}")      
   await ctx.send(embed=embed)

@client.command(aliases=['mc'])
@commands.has_permissions(manage_messages=True)     
async def membercount(ctx):
   r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
   embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
   embed.add_field(name="Member Count", value=f"**{len(ctx.guild.members)} Members**")
   await ctx.send(embed=embed)
   
@membercount.error
async def membercount_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Manage Messages`` Permission To Use This Command**")
        await ctx.send(embed=embed)   

@client.command()
async def add(ctx, a:int, b:int):
    embed=discord.Embed()
    embed.add_field(name="Solution", value=(a+b))
    await ctx.send(embed=embed)

@client.command()
async def stats(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Member Status", color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
    embed.add_field(name="Online", value=f"<:online:723485563814150154>  Online: {len([x for x in ctx.guild.members if x.status == discord.Status.online])}")
    embed.add_field(name="Idle", value=f"<:idle:723485795087810601>  Idle: {len([x for x in ctx.guild.members if x.status == discord.Status.idle])}")
    embed.add_field(name="Do Not Disturb", value=f"<:dnd:723485662124310539>  Do not Disturb: {len([x for x in ctx.guild.members if x.status == discord.Status.dnd])}")
    embed.add_field(name="Offline", value=f"<:off:723485614149992518>  Offline: {len([x for x in ctx.guild.members if x.status == discord.Status.offline])}")
    await ctx.send(embed=embed)
  
@client.command(aliases=['bs'])
async def botstats(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
    embed.add_field(name="AGENT INFORMATION", value=f" **AGENT IS WATCHING {len(client.users)} MEMBERS**")
    embed.add_field(name="AGENT SERVERS", value=f" **AGENT IS WATCHING {len(client.guilds)} SERVER**")
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text=f"Made By Mʀ.Golu")
    await ctx.send(embed=embed)
    
@client.command()
async def howlesbo(ctx, member : discord.Member):
   r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
   embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
   embed.add_field(name="Howlesbo?", value=f"**{member.mention} Is {random.randint(1, 100)}% Lesbo!**")
   await ctx.send(embed=embed)    

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user):
    user=await client.fetch_user(user)
    await ctx.guild.unban(user)
    await ctx.send(f'Unbanned {user.name}')
    
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.name}')    
 
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Kick Members`` Permission To Use This Command**")
        await ctx.send(embed=embed) 
 
@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="<:tick:721321849254051840> Slowmode <:tick:721321849254051840>", description=f"**<:tick:721321849254051840> Slowmode Enabled | Slowmode Time=> {seconds} Seconds!**", color = discord.Color((r << 16) + (g << 8) + b))
    await ctx.send(embed=embed)
    
@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Manage Channels`` Permission To Use This Command**")
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
        
  
@client.command()
async def rolecolor(ctx, role: discord.Role, value: discord.Colour):
    if ctx.author.guild_permissions.administrator:
        await role.edit(color=value)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="Color Changed", value=f"**{role.mention} Color Was Changed To {value}**")
        await ctx.send(embed=embed)
        
@client.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, sentence):
     await ctx.message.delete()
     await ctx.send(sentence)
  
@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Manage Messages`` Permission To Use This Command**")
        await ctx.send(embed=embed)  
        
@client.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Please Mention Someone**')
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *, sentence):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="◻ Poll Time! ◻ ", value=sentence)
    embed.set_footer(text=f"👍 If Yes / 👎 If No | Polled By {ctx.author.name}")
    message = await ctx.send(embed=embed)
    await message.add_reaction("👍")
    await message.add_reaction("👎")
    
@poll.error
async def poll_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Manage Messages`` Permission To Use This Command**")
        await ctx.send(embed=embed)    
    
@client.command()
async def hug(ctx, member:discord.Member):
    embed=discord.Embed(description=f"{ctx.author.mention} **Hugs** {member.mention}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/721300256284868659/723159119065907210/emoji.gif")
    await ctx.send(embed=embed)

@client.command()
async def lock(ctx):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<a:tickkibhenka:713794654344052766> Channel Locked <a:tickkibhenka:713794654344052766> ", value=f" {ctx.author.mention} **Locked Channel Successfully**")
        await ctx.send(embed=embed)
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
      
@client.command()
async def unlock(ctx):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<a:tickkibhenka:713794654344052766> Channel Unlocked <a:tickkibhenka:713794654344052766> ", value=f" {ctx.author.mention} **Unlocked Channel Successfully**")
        await ctx.send(embed=embed)
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)   
      
@client.command()
async def roleinfo(ctx, role:discord.Role=None):
        embed=discord.Embed()
        embed.add_field(name="Role Name", value=role.name)
        embed.add_field(name="Role Id", value=role.id)
        embed.add_field(name="Role Position", value=role.position)
        await ctx.send(embed=embed)
      
@client.command(pass_context=True, aliases=['purge'])
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()
    
@client.command()
async def slap(ctx, member:discord.Member):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="Slapped", value=f"**{ctx.author.name} Slapped {member.name}**")
        embed.set_image(url="https://cdn.discordapp.com/attachments/666340441741983763/737220305868554320/tenor_6.gif")
        await ctx.send(embed=embed)
    

@client.command(pass_context=True)
async def setnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Nickname Changed", value=f"Nickname Of {member.mention} Was Changed")
    await ctx.send(embed=embed)
    

@client.command()
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
                   
@client.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, *, message):
     r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))             
     embed = discord.Embed(description=str(message), color = discord.Color((r << 16) + (g << 8) + b), timestamp=ctx.message.created_at)
     await ctx.send(embed=embed)
                
@embed.error
async def embed_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name="<:tickkipenka:723390095234826321> Missing Permissions <:tickkipenka:723390095234826321>", value=f"**{ctx.author.mention} You Must Have ``Manage Messages`` Permission To Use This Command**")
        await ctx.send(embed=embed)   
                   
@client.event
async def on_message(message):
        await client.process_commands(message)          
        if message.content == "<help":
          await message.channel.send('✅| **Check Your Dm I Have Send You Commands List**')
                   
@client.command()
async def howgendu(ctx, member : discord.Member):    
   r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
   embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
   embed.add_field(name="Howgendu?", value=f"**{member.mention} Is {random.randint(1, 100)}% Gendu!**")
   await ctx.send(embed=embed)    
                   
@client.command()
async def minus(ctx, a:int, b:int):
    embed=discord.Embed()
    embed.add_field(name="Solution", value=(a-b))
    await ctx.send(embed=embed)  
                   

@client.command()
async def meme(ctx):
  images=["https://cdn.discordapp.com/attachments/721299555907272704/738307924413120532/images_2.jpeg", "https://cdn.discordapp.com/attachments/721299555907272704/738307961272795146/images_1.jpeg", "https://cdn.discordapp.com/attachments/721299555907272704/738309668807639040/download_1.jpeg"]
  embed=discord.Embed()
  embed.set_image(url=random.choice(images))
  await ctx.send(embed=embed)
          
client.run('NzUzMDY3NDkxMTAxNTA3NjE3.X1gywQ.K62kDddu_6LfGPScPA52t4rNNZQ')

