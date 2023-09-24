import discord
from discord.ext import commands
import requests

import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices)) 

@bot.command()
async def tokenn(ctx):
    idk = input("so you got the token?")
    if idk == "yes":
        print("congrats :D")
    else:
        print("=)")
    await ctx.send("_____________")

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def music(ctx):
    music = ["https://youtu.be/L5q4uYj-gyg?feature=shared","https://youtu.be/pDxrBAfNU2I?feature=shared","https://youtu.be/C9PFVo1FEwU?feature=shared","https://youtu.be/BR97p0bzEYo?feature=shared"]
    await ctx.send(random.choice(music))    

@bot.command()
async def roll(ctx):
    await ctx.send(str(random.randint(1,100)))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    iimagess = os.listdir('images')
    img_name = random.choice(iimagess)
    with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)        

@bot.command()
async def roll_dice(ctx):
    dice = os.listdir('zar')
    rolldice = random.choice(dice)
    with open(f'zar/{rolldice}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)   

@bot.command()
async def tema(ctx):
    await ctx.send(f'https://www.tema.org.tr/')
    
@bot.command()
async def sifiratik(ctx):
    await ctx.send(f'https://sifiratik.gov.tr/')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def help_(ctx):
    await ctx.send(f'avalible commands: !roll_dice, !roll, !mem, !music, !cool, !choose, !hello, !tema, !sifiratik, !add(ex:''!add 2 3'' or any number you want)')
        
        
bot.run([insert token])
