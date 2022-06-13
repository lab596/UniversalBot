from keep_alive import keep_alive
import discord
import praw
import os
import random
from random import randint
import urllib.parse, urllib.request, re
import json
from datetime import datetime
#import threading
from threading import Timer




intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
  
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

keep_alive()
while True:
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
          json.dump(data,o,indent=4)
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
    #####################################################################################
    if message.content.startswith("$deposit!"):
      command = message.content
      amt = command[9:len(command)]
      author = message.author


      
      users = await get_bank_data()
      vals=[]
      for i in users:
        vals.append(i.keys())
      keys = []
      for j in vals:
        j = str(j)
        j1 = j.split("'")
        j = j1[1]
        j2 = j.split("'")
        j=j2[0]
        keys.append(j)


      
      m = keys.index(str(author.id))
      f=open("bank.json",'r+')
      data = json.load(f)
      count1=0
      for k in data['bank_details']:
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<int(amt):
            await message.channel.send("You lack the required funds to complete this deposit.")
            return
        count1+=1
      
      count1=0
      for k in data['bank_details']:
        if((count1)==m):
          k[str(author.id)]['wallet']-=int(amt)
          k[str(author.id)]['bank']+=int(amt)
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)
        
      await message.channel.send("Deposit successful.")
    ##############################################################################
    if message.content.startswith("$withdraw!"):
      command = message.content
      amt = command[10:len(command)]
      author = message.author
      
      users = await get_bank_data()
      vals=[]
      for i in users:
        vals.append(i.keys())
      keys = []
      for j in vals:
        j = str(j)
        j1 = j.split("'")
        j = j1[1]
        j2 = j.split("'")
        j=j2[0]
        keys.append(j)
      
      m = keys.index(str(author.id))
      f=open("bank.json",'r+')
      data = json.load(f)
      count1=0
      for k in data['bank_details']:
        if((count1)==m):
          if int(k[str(author.id)]['bank'])<int(amt):
            await message.channel.send("You lack the required funds to complete this withdrawl.")
            return
        count1+=1
      
      count1=0
      for k in data['bank_details']:
        if((count1)==m):
          k[str(author.id)]['wallet']+=int(amt)
          k[str(author.id)]['bank']-=int(amt)
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)
  
      await message.channel.send("Withdrawl successfull.")
      
    #########################################################################################
    if "$transfer!" in message.content:
      command = message.content
      author = message.author
      user = command.split("$")
      usera = user[0]
      amt = command.split("!")
      amta = amt[1]
      if not(message.author.guild_permissions.administrator) and int(amta) < 0:
        await message.channel.send("You are not authorized to take money.")
        return
        
      users = await get_bank_data()
      vals=[]
      for i in users:
        vals.append(i.keys())
      #print(vals)
      keys = []
      ppl =[]
      
      for j in vals:
        j = str(j)
        j1 = j.split("'")
        j = j1[1]
        j2 = j.split("'")
        j=j2[0]
        keys.append(j)
      #username = discord.Guild.get_member(int(keys[0]))
      #print(keys)
      #checking if author has funds
      m = keys.index(str(author.id))
      f=open("bank.json",'r+')
      data = json.load(f)
      count1=0
      for k in data['bank_details']:
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<int(amta):
            await message.channel.send("You lack the required funds to complete this transfer.")
            return
        count1+=1
      
      #print(keys)
      #print(usera)
      for u in keys:
        username = client.get_user(int(u))
        username = str(username)
        username = username[0:len(str(username))-5]
        #print(username)
        ppl.append(username)
        if(username == usera):
          a = keys.index(str(u))
          b = keys.index(str(author.id))
          f=open("bank.json",'r+')
          data = json.load(f)
          count = 0
          #print(b)
          #print(a)
          for i in data['bank_details']:
            #print(i)
            if((count)==a):
              i[str(u)]['wallet']+=int(amta)
            if((count)==b):
                i[str(author.id)]['wallet']-=int(amta)
            count+=1
          with open("bank.json",'w') as o:
            json.dump(data,o,indent=4)
  
  
      #checking if user is present
      found = False
      for i in ppl:
        if str(usera) == str(i):
          found = True
  
      if found == False:
        await message.channel.send("Person not in database.")
        await message.channel.send("Make sure you and the person you are transfering money too have an account.")
        await message.channel.send("This can be done by typing '$balance'.")
        return
            
      await message.channel.send("Funds transfered successfully.")



      
  #========================================
  
  


  def intrest():
    #print("Function called.")
    now = datetime.now()
    
    current_time = now.strftime("%H:%M")
    #print("Current Time is :", current_time)
    time = current_time.split(":")
    min = time[1]
    #print(min)
    with open("bank.json","r") as f:
        users = json.load(f)['bank_details']
    #print(users)
        
    vals=[]
    for i in users:
      vals.append(i.keys())
    #print(vals)
    keys = []
    ppl =[]
          
    for j in vals:
      j = str(j)
      j1 = j.split("'")
      j = j1[1]
      j2 = j.split("'")
      j=j2[0]
      keys.append(j)
    
    count = 0
    if(min == "00"):
      #print("Passes if statement.")
      f=open("bank.json",'r+')
      data = json.load(f)
      for i in data['bank_details']:
        a = i[str(keys[count])]['bank']
        i[str(keys[count])]['bank'] = int(a) * 1.01
        count+=1
          
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)
    Timer(60,intrest).start()

  intrest()
  #t1 = threading.Thread(target = intrest)
  #t1.start()


  
  #=======================================================    
      
  
        
  
  
  def write_json(new_data, filename='bank.json'):
      with open(filename,'r+') as file:
          # First we load existing data into a dict.
          file_data = json.load(file)
          # Join new_data with file_data inside emp_details
          file_data["bank_details"].append(new_data)
          # Sets file's current position at offset.
          file.seek(0)
          # convert back to json.
          json.dump(file_data, file,indent=4)
  
  
  
      
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

      
    
    
  
