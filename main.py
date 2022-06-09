
import discord
import praw
import os
import random
from random import randint
import urllib.parse, urllib.request, re
import json




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


  #if message.author.id == 758509998459977768:
    #await message.channel.send("Bro stop talking.")
    #await message.channel.send("No one asked.")
  
  if message.author == client.user:
    #print("I have spoken.")
    return

  if message.content.startswith("\hello") and not(message.author.id == 758509998459977768):
    value = randint(0,6)
    
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

  if message.content.startswith('*rquery!'):
      command = message.content
      search = command[8:len(command)]
   
      subreddit = reddit.subreddit(search)
  
      all_subs= []
      top = subreddit.hot(limit = 3)
      
      for submission in top:
        all_subs.append(submission)
      
      
      i=0
      await message.channel.send("Top posts:")
      while i < 3: 
        name = all_subs[i].title
        url = all_subs[i].url
        em = discord.Embed(title = name)
        
        em.set_image(url = url)
        
        await message.channel.send(embed = em)
        i+=1
      await message.channel.send("https://www.reddit.com/r/"+search+"/")

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


  if message.content.startswith("*yquery!"):
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

  if message.content.startswith("$balance"):
    author = message.author
    await open_account(author)
    users = await get_bank_data()
    for i in users:
      vals = i.keys()
      for x in vals:
        if x == str(author.id):
          wallet_amt = i[x]["wallet"]
          bank_amt = i[x]["bank"]
    #wallet_amt = users[str(author.id)]["wallet"]
    #bank_amt = users[str(author.id)]["bank"]
    
    em = discord.Embed(title = f"{author.name}'s balance",color = discord.Color.green())
    em.add_field(name = "Wallet balance", value = wallet_amt)
    em.add_field(name = "Bank balance", value = bank_amt)
    await message.channel.send(embed = em)



    
  if message.content.startswith("$funds!"):
    if message.author.guild_permissions.administrator:
      command = message.content
      amt = command[7:len(command)]
      author = message.author
      #await open_account(author)
      #users = await get_bank_data()
      earnings = int(amt)
      count = 0
      f=open("bank.json",'r+')
      data = json.load(f)
      #print(data)
      #print(data['bank_details'])
      for i in data['bank_details']:
        #print(i)
        #print(i[str(author.id)])
        #print(i[str(author.id)]['wallet'])
        if count == 0:
          i[str(author.id)]['wallet']+=earnings
          count+=1

      with open("bank.json",'w') as o:
        json.dump(data,o)
      #json.write(data)
      #print(data)
      #json.dump(data,f)
      
 
      #for i in users:
        #vals = i.keys()
        #for x in vals:
          #if x == str(author.id):
            #print("Passed id check")
            #data[i[x]["wallet"]] = i[x]["wallet"] + earnings
      




              
            
          #users[str(author.id)]["wallet"] += earnings

      #write_json(users)
      
      await message.channel.send("Funds updated.")             
      
    else:
      await message.channel.send("Sorry, you are not authorized to use this command.")

  if "$transfer!" in message.content:
    command = message.content
    user = command.split("$")
    usera = user[0]
    amt = command.split("!")
    amta = amt[1]
    print(usera)
    print(amta)
    

      


def write_json(new_data, filename='bank.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["bank_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file)



    
async def open_account(user):
  with open("bank.json","r") as f:
    users = json.load(f)['bank_details']
  for i in users:
    vals = i.keys()
    for x in vals:
      if x == str(user.id):
        return False
  else:
    users = {}
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"]= 5
    users[str(user.id)]["bank"]= 10
   
    write_json(users)
  
  return True

async def get_bank_data():
  with open("bank.json","r") as f:
    users = json.load(f)['bank_details']
  return users



client.run(os.getenv('TOKEN'))

#{"bank_details": [
  
#]}

      
    
    
  
