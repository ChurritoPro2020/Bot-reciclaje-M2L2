import random
import discord 
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents = intents)

list_memereciclar = os.listdir('memes')
list_reciclar = os.listdir('reciclamos')
consejos = ["Reduce, reutiliza y recicla.", 
            "Usa transporte público, camina o anda en bicicleta.", 
            "Ahorra energía apagando las luces y los electrodomésticos cuando no los uses.", 
            "Planta árboles y otras plantas.", "Compra productos locales y de temporada.", 
            "Apoya a las organizaciones que trabajan para proteger el medio ambiente."]
toturiales = ['https://youtu.be/6JDTVucdSoQ?si=6Ri4S3BO5ZFRhvip','https://youtu.be/YifO4gRbLwA?si=KaAu6NcmZRs5IJm9','https://youtu.be/8onF76oNsWA?si=5DrEWr4h-W6dOlba']
comandosexistentes = ['/meme genera un meme aleatorio sobre reciclaje :)','/reciclar una imagen sobre ideas que hace la gente para reciclar'
            ,'/ayuda consejo aleatorio para ayudar al medio ambiente','/tutorial tutoriales aleatorios sobre ideas de como reciclar y reutilizar cosas de tu casa']

@bot.event
async def on_ready():
    print(f'logeado como {bot.user} (ID: {bot.user.id})')

@bot.command()
async def reciclar(ctx):
    select_reciclar = random.choice(list_reciclar)
    with open(f'reciclamos/{select_reciclar}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(content='aqui una idea para reciclar :D ',file=picture)

@bot.command()
async def ayuda(ctx):
    await ctx.send(random.choice(consejos))

@bot.command()
async def tutorial(ctx):
    await ctx.send(random.choice(toturiales))

@bot.command()
async def meme(ctx):
    select_memereciclar = random.choice(list_memereciclar)
    with open(f'memes/{select_memereciclar}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(content='aqui un meme sobre reciclaje',file=picture)

@bot.command()
async def comandos(ctx):
    await ctx.send(comandosexistentes)

bot.run('')
