from base64 import decode
import shutil
import uuid
from cv2 import QRCodeDetector
import discord
from discord import *
from discord.ext import commands
import time
import platform
import os
from PyPDF2 import *
import cv2 
from pyzbar.pyzbar import decode    
from PIL import Image
import requests

'''
import glob
import cv2
import pandas as pd
import pathlib
'''


Bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

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

#Clear
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
async def save(ctx):
        if ctx.message.attachments[0].url.endswith(".pdf"):
            await ctx.message.attachments[0].save('ogrencibelge.pdf')
            time.sleep(1)
            ogrencibelgeqr= PdfFileReader("ogrencibelge.pdf")
            pageogrenci = ogrencibelgeqr.pages[0]
            sayma = 0

            for image_file_object in pageogrenci.images:
                with open(str(sayma) + image_file_object.name, "wb") as fp:
                    fp.write(image_file_object.data)
                    sayma += 1
            time.sleep(1)
            qrkod = decode(Image.open('0img2.jpg'))
            print(type(qrkod))
            print(qrkod)
            qrkodelist= str(qrkod)
            liste=qrkodelist.split(";")
            b = "https://www.turkiye.gov.tr/belge-dogrulama?mobile'"
            if any(b in s for s in liste):
                print("hahahaha")
                await ctx.send("Okul ogrencisiniz")
                print("Basardin")
            else:
                pass

            
        else:
            await ctx.send('Pdf olarak gönderiniz')










Bot.run('MTAyMzg3MjI5ODIwMzIxNzkyMA.Gb5LEj.zqVgsJC3lnhIYKE0f3pbLy9z58r2AV6nMhOO7k')

