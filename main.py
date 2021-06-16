import os #import
import discord #import
from random import randint #import

client = discord.Client() #initialization

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  

  if message.content.startswith('!hello'): #greeting
    await message.channel.send('Hello!')

  elif message.content.startswith('!iq'): #random iq
    intel = randint(1, 201)
    await message.channel.send('Your iq = ' + str(intel))

  elif message.content.startswith('!age'): #random age
    age = randint(1, 501)
    await message.channel.send('Your age = ' + str(age))

  elif message.content.startswith('!case'): #case
    nums = ['Nothing', '$1', '$2000', '$300', '$100']
    n = randint(0, 4)
    await message.channel.send('You won - ' + nums[n])

  elif message.content.startswith('!rank'):
    await message.channel.send("You noob!")

  elif message.content.startswith('!csgo'):
    weapons = ["AWP Dragon Lore", "M4A4 Howl", "SG553 Perforated Waves", "Five-Seven Monkey business", "USP-S Kill Confirmed"]
    images = ['https://i.imgur.com/RbPTpRl.jpeg', 'https://i.imgur.com/ZfN3zyE.jpg', 'https://i.ytimg.com/vi/7WWbDAVICIU/maxresdefault.jpg', 'https://media.sketchfab.com/models/f1989dc2ff0b4f67a518e7ac46a53c22/thumbnails/d39aaf2f20f242c2a10d52678c649995/1024x576.jpeg', 'https://i.imgur.com/sodFYjd.png']
    le = len(weapons)
    i = randint(0, le-1)
    weapon = weapons[i]
    im = images[i]
    iznos = 0.01 * randint(0, 101)
    if (iznos >= 0 and iznos <= 0.07):
      stepen = "Factory New"
    elif (iznos > 0.07 and iznos <= 0.15):
      stepen = "Minimal Wear"
    elif (iznos > 0.15 and iznos <= 0.37):
      stepen = "Field-Tested"
    elif (iznos > 0.37 and iznos <= 0.44):
      stepen = "Well-Worn"
    elif (iznos > 0.44 and iznos <= 1):
      stepen = "Battle-Scared"
    else:
      stepen = ""
    await message.channel.send("You won: " + weapon + " " + stepen)
    await message.channel.send(im)

  elif message.content.startswith('!meme'): #random meme picture
    pics = ['https://i.imgur.com/Qpw6j8D.png', 'https://i.imgur.com/bCBt6ga.jpeg', 'https://i.imgur.com/8nLFCVP.png'] #ДОПОЛНЯЙ
    l = len(pics)
    ind = randint(0, l)
    await message.channel.send(pics[ind])
  
client.run(os.getenv('TOKEN')) #token