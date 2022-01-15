import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import youtube_dl
import os
from random import choice
from discord.utils import get

bot = commands.Bot(command_prefix="/")
players  = {}


@bot.event 
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Siendo Yo Mismo'))
    print("Welcome Haruo")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Porfavor usa todos los argumentos.')

@bot.command()
async def HolaHaruo(ctx):
    msg = f'Qué Onda Panita uwu!'
    await ctx.send(msg)

@bot.command()
async def IRL(ctx):
    msg = f'Eh... Sabes, creo que no importa como me vea en la vida real...'
    await ctx.send(msg)

@bot.command()
async def Pareja(ctx):
    msg = f'Mikumi <3, Es ella pero no lo sabe aún uwu (No le digan porfa :c, me pega Caisen).'
    await ctx.send(msg)
@bot.command()
async def Amigos(ctx):
    msg = f'¿Mis amigos?, ¡Ah!, Te refieres a Katashi, Makoto y La bola de pelos.'
    await ctx.send(msg)
@bot.command()
async def Feliz(ctx):
    msg = f'¡FELIZ JUEVES!'
    await ctx.send(msg)
@bot.command()
async def Coder(ctx):
    msg = f'Fuí Programado por M͓̽ ͓̽a͓̽ ͓̽u͓̽#2914, Junto con Hyperia BOT, y si, se que soy una IA owo.'
    await ctx.send(msg)
@bot.command()
async def Spoiler(ctx):
    msg = f'No puedo decirte nada que no sepas ya OwO.'
    await ctx.send(msg)
@bot.command()
async def SrPug(ctx):
    msg = f'¿Otra vez el Perro tonto ese?, ¿No se cansa de que lo mande al otro lado del Distrito?'
    await ctx.send(msg)
@bot.command()
async def Cerveza(ctx):
    msg = f'¿Quién crees que soy? *Susurrando*: Dame una porfa'
    await ctx.send(msg)
@bot.command()
async def FunkyMonkeyFriday(ctx):
    msg = f"IT'S FUNKY MONKEY FRIDAY"
    await ctx.send(msg)

@bot.command()
async def SOS(ctx):
    msg = f'¿Sos Diego o Normal?'
    await ctx.send(msg)

@bot.command()
async def Basado(ctx):
    msg = f'Bastante Basado.'
    await ctx.send(msg)
    
bot.run("Nzg4OTkzNDczNjUwMzYwMzYw.X9rlbg.ikD2wZbtBt5PtoMzHAiWa1Wo1Y8")