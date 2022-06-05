
import discord
import praw
import os
import random
import urllib.parse, urllib.request, re




client = discord.Client()

reddit = praw.Reddit(client_id = "YaPJsXKF1TYThaLys7xnSg",
                     client_secret= os.environ['SEC'],
                     username="DaT1dUdE05",
                     password= os.environ['PASS'],
                     user_agent="pythonmeme",
                     check_for_async=False
                    )

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  print("Hello Sir, I am ready")




@client.event
async def on_message(message):

  from random import randint

  value = randint(0,6)


  if message.author.id == 758509998459977768:
    await message.channel.send("Bro stop talking.")
    await message.channel.send("No one asked.")
  
  if message.author == client.user:
    #print("I have spoken.")
    return

  if message.content.startswith("\hello") and not(message.author.id == 758509998459977768):
    
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

  if message.content.startswith("\dadjoke"):
    subredditd = reddit.subreddit("dadjokes")
    all_subs= []
    top = subredditd.hot(limit = 50)
    
    for submission in top:
      all_subs.append(submission)
    
    random_sub = random.choice(all_subs)
    
    name = random_sub.title
    body = random_sub.selftext
    #em = discord.Embed(title = name)
    #em = discord.Embed(selftext = body)
    
    
    
    await message.channel.send(name)
    await message.channel.send(body)
    

  if message.content.startswith("\meme"):
    all_subred = []
    subreddit1 = reddit.subreddit("dankmemes")
    subreddit2 = reddit.subreddit("meme")
    all_subred.append(subreddit1)
    all_subred.append(subreddit2)
    subreddit = random.choice(all_subred)
    all_subs= []
    top = subreddit.hot(limit = 50)
    
    for submission in top:
      all_subs.append(submission)
    
    random_sub = random.choice(all_subs)
    
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title = name)
    
    em.set_image(url = url)
    
    await message.channel.send(embed = em)

  if message.content.startswith("\yquery!"):
    command = message.content
    search = command[8:len(command)]
    #print(search)
    query_string = urllib.parse.urlencode({
      'search_query': search
    })
    #print(query_string)
    htm_content = urllib.request.urlopen(
      'http://www.youtube.com/results?' + query_string
    )
    #print(htm_content)
    search_content=htm_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+',search_content)
    top_res = []
    for i in search_results:
      top_res.append(i)
    c = 1
    j=5
    await message.channel.send("Top 5 results:")
    while j > 0:
      if c == 1: 
        await message.channel.send(str(c)+") "+'http://www.youtube.com'+top_res[c-1])
      else:
        await message.channel.send(str(c)+") "+'<http://www.youtube.com'+top_res[c-1]+">")
      j-=1
      c+=1
    
    #await message.channel.send('http://www.youtube.com'+search_results[0])
    

      
  
    
    

client.run(os.getenv('TOKEN'))

      
    
    
  
