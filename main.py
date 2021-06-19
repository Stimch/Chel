import os #import
import discord #import
from discord.ext import commands
from random import randint #import

# client = discord.Client() #initialization
client = discord.ext.commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) #console

@client.command()
async def hello(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Hello!')

@client.command()
async def fix(ctx):
    await ctx.send(f'Fixed')

@client.command()
async def developer(ctx):
    await ctx.send("ageykinegor@mail.ru")

@client.command()
async def iq(ctx):
    intel = randint(1, 201)
    await ctx.send('Your iq = ' + str(intel))

@client.command()
async def age(ctx):
    intel = randint(1, 501)
    await ctx.send('Your age = ' + str(intel))

@client.command()
async def case(ctx):
    nums = ['Nothing', '$1', '$2000', '$300', '$100']
    n = randint(0, 4)
    await ctx.send('You won - ' + nums[n])

@client.command()
async def com(ctx):
    await ctx.send("Check text-channel named команды-бота")

@client.command()
async def csgo(ctx):
    weapons = ["AWP Dragon Lore", "M4A4 Howl", "SG553 Perforated Waves", "Five-Seven Monkey business", "USP-S Kill Confirmed"]
    images = ['https://i.imgur.com/RbPTpRl.jpeg', 'https://i.imgur.com/ZfN3zyE.jpg', 'https://i.ytimg.com/vi/7WWbDAVICIU/maxresdefault.jpg', 'https://media.sketchfab.com/models/f1989dc2ff0b4f67a518e7ac46a53c22/thumbnails/d39aaf2f20f242c2a10d52678c649995/1024x576.jpeg', 'https://i.imgur.com/sodFYjd.png']
    le = len(weapons)
    i = randint(0, le-1)
    weapon = weapons[i]
    im = images[i]
    iznos = 0.01 * randint(0, 101)
    if (iznos >= 0 and iznos <= 0.07):
      stepen = "(Factory New)"
    elif (iznos > 0.07 and iznos <= 0.15):
      stepen = "(Minimal Wear)"
    elif (iznos > 0.15 and iznos <= 0.37):
      stepen = "(Field-Tested)"
    elif (iznos > 0.37 and iznos <= 0.44):
      stepen = "(Well-Worn)"
    elif (iznos > 0.44 and iznos <= 1):
      stepen = "(Battle-Scared)"
    else:
      stepen = ""
    await ctx.send("You won: " + weapon + " " + stepen)
    await ctx.send(im)

@client.command()
async def meme(ctx):
    pics = ['https://i.imgur.com/Qpw6j8D.png', 'https://i.imgur.com/bCBt6ga.jpeg', 'https://i.imgur.com/8nLFCVP.png'] #ДОПОЛНЯЙ
    l = len(pics)
    ind = randint(0, l)
    await ctx.send(pics[ind])

@client.command()
async def game(ctx, *, text):
    variants = ['rock', 'paper', 'scissors']
    num = randint(0, 2)
    var = variants[num] 
    if var == "rock" and text == "rock":
      await ctx.send('Draw!')
    elif var == "paper" and text == "rock":
      await ctx.send('Lose!')
    elif var == "scissors" and text == "rock":
      await ctx.send('You won!')
    elif var == "rock" and text == "paper":
      await ctx.send('You won!')
    elif var == "scissors" and text == "paper":
      await ctx.send('Lose!')
    elif var == "paper" and text == "paper":
      await ctx.send('Draw!')
    elif var == "scissors" and text == "scissors":
      await ctx.send('Draw!')
    elif var == "paper" and text == "scissors":
      await ctx.send('you won!')
    elif var == "scissors" and text == "scissors":
      await ctx.send('Draw!')
  
client.run(os.getenv('TOKEN')) #token