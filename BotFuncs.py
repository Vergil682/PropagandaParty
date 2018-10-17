import random
import asyncio
import json
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("PZ!", "pz!", "Pz!", "!pz", "!Pz!", "!PZ")
client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball', description="Answers a yes/no question", brief="Answers from the beyond!", aliases=['eight-ball','eightball','8-ball','8Ball','8BALL'], pass_context=True)
async def eightball(context):
  possible_responses = [
    'That is a resounding no',
    'It is not looking likely',
    'Its is too hard to tell',
    'It is quite possible',
    'Definitely'
  ]
  await client.say(random.choice(possible_responses) + ", ")
  
  
@client.command()
  async def square(number):
   squared-value = int(number) * int(number)
   await client.say(str(number) + " squared is " +str(squared-value))
    
  
@client.event
async def on-message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith(client + 'info'):
    msg = "Hello {0.author.mention}! I'm PropagandaParty, a bot built by The Real Vergil#1492".format(message)
    await client.send_message(message.channel, msg)
  
  if message.content.startswith(client + 'help'):
    msg3 = 'No Problem {0.author.mention}, The functions are:
    msg4 = '**Help**: Prints this, '
    msg5 = '**8ball**: plays a yes or no question game, '
    msg6 = '**info**: Gives information about the bot, '
    msg7 = '**square**: Squares the given number, '
    msg8 = '**add**: Adds the two numbers given, '
    msg9 = '**Bitcoin**: Gives the current Bitcoin value.'
    msg2 = msg3 + msg4 + msg5 + msg6 + msg7 + msg8 + msg9
    await client.send_message(message.channel, msg2.format(message))
    
@client.event()
async def on_ready():
  await client.chang_presence(game=Game(name="with the media"))
  print("Logged in as " + client.user.name)
   
@client.command()
async def Bitcoin():
  url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
  async with aiohttp.ClientSession() as session:
    raw_response = await session.get(url)
    response = await raw_response.text()
    response = json.loads(response)
    await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
    
client.run(TOKEN)
