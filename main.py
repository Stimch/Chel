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
  

  if message.content.startswith('!privet'): #greeting
    await message.channel.send('Привет!')

  elif message.content.startswith('!iq'): #random iq
    intel = randint(1, 201)
    await message.channel.send('Ваш iq = ' + str(intel))

  elif message.content.startswith('!age'): #random age
    age = randint(1, 501)
    await message.channel.send('Ваш возраст = ' + str(age))

  elif message.content.startswith('!case'): #case
    nums = ['Ничего', '$1', '$2000', '$300', '$100']
    n = randint(0, 4)
    await message.channel.send('Вы выиграли в кейсе - ' + nums[n])

  elif message.content.startswith('!rank'):
    await message.channel.send("You noob!")

  elif message.content.startswith('!csgo'):
    weapons = {"AWP Dragon Lore": 'https://i.imgur.com/RbPTpRl.jpeg'}
    le = len(weapons)
    i = randint(0, le)
    weapon = weapons(i)
    im = weapons.get(weapon)
    await message.channel.send("You won: " + weapon)
    await message.channel.send(im)

  elif message.content.startswith('!meme'): #random meme picture
    pics = ['https://i.imgur.com/Qpw6j8D.png', 'https://i.imgur.com/bCBt6ga.jpeg', 'https://i.imgur.com/8nLFCVP.png'] #ДОПОЛНЯЙ
    l = len(pics)
    ind = randint(0, l)
    await message.channel.send(pics[ind])
  
client.run(os.getenv('TOKEN')) #token