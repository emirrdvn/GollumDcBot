import os

import discord
from discord.ext import commands
import time
import platform
from botgames import *
import os
Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
game = Game()

#Hello
@Bot.command()
async def selam(ctx):
    await ctx.send("Selam!")

#Ready
@Bot.event
async def on_ready():
    print("Giriş yapıldı " + Bot.user.name)
    print("Bot ID = " + str(Bot.user.id))

#Stop
@Bot.command(aliases=['kapa','dur'])
async def kapat(ctx):
    await ctx.send("Bot sizlere ömür")
    await  Bot.close()

#User Info
@Bot.command(aliases=['kimo'])
async  def kiminnesi(ctx,member:discord.Member=None):
    if member == None:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(title="Kullanıcı Bilgisi", description=f"İşte kullanıcı bilgisi {member.mention}", color = discord.Color.green(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="ID", value = member.id)
    embed.add_field(name="Ad", value = f"{member.name}#{member.discriminator}")
    embed.add_field(name="Takma Ad ", value = member.display_name)
    embed.add_field(name="Durum", value = member.status)
    embed.add_field(name="Oluşturulma Tarihi", value = member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
    embed.add_field(name="Katılma Tarihi", value=member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
    embed.add_field(name="Roller",value = " ".join([role.mention for role in roles]))
    embed.add_field(name="Üstün Yetki", value = member.top_role)


    await ctx.send(embed=embed)

#Server Info
@Bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title="Sunucu Bilgisi", description=f"İşte sunucu bilgisi, {ctx.guild.name}", color = discord.Color.red(), timestamp = ctx.message.created_at)
    await ctx.send(embed=embed)

@Bot.command()
async def clear(ctx, amaount = 5):
    await ctx.channel.purge(limit=amaount)

@Bot.command()
async def kick(ctx, member:discord.Member, *args, reason="Yok"):
    await member.kick(reason=reason)

@Bot.command()
async def ban(ctx, member:discord.Member, *args, reason="Yok"):
    await member.ban(reason=reason)

@Bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Banı Kaldırıldı {user.mention}')
            return

@Bot.command()
async def load(ctx, extension):
    Bot.load_extension(f'cogs.{extension}')

@Bot.command()
async def unload(ctx, extension):
    Bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        Bot.load_extension(f'cogs.{filename[:-3]}')









Bot.run('MTAyMzg3MjI5ODIwMzIxNzkyMA.GiioHr.kWyAE7wtcLoh0OAqzNsqEonnqdmSbwjmPQdYSQ')