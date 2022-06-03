
import discord
import os


client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  print("Hello Sir, I am ready")



@client.event
async def on_message(message):

  from random import randint

  value = randint(0,6)


  if message.author == client.user:
    print("I have spoken.")

  if message.content.startswith("\hello"):
    
    if value == 0:
      await message.channel.send("Hi.")
    
    if value == 1:
      await message.channel.send("Hey.")

    if value == 2:
      await message.channel.send("Greetings.")
      
    if value == 3:
      await message.channel.send("Howdy.")

    if value == 4:
      await message.channel.send("Beep. Boop. Greetings Human.")

    if value == 5:
      await message.channel.send("Hello.")
      
    if value == 6:
      await message.channel.send("Yo.")

client.run(os.environ['TOKEN'])

      
    
    
  
