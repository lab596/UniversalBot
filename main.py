from keep_alive import keep_alive
import discord
import praw
import os
import random
from random import randint
import urllib.parse, urllib.request, re
import json
#from datetime import datetime
#import threading
from threading import Timer
#from discord import Color
from discord.utils import get




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


@client.event
async def on_guild_join(guild):
  f=open("bank.json",'r+')
  data = json.load(f)
  
  guild_db = data.get(str(guild.id))
  if not guild_db:  # If the guild hasn't been visited yet
      data[str(guild.id)] = [ ]
        # Do your stuff to create a new economic system
  else:
        # In case the guild already exists in the database
        # Do stuff here
    print("ok")
  
  with open("bank.json",'w') as o:
    json.dump(data,o,indent=4)

  await guild.create_role(name="Bronze",color=discord.Color.from_rgb(255,153,51))
  await guild.create_role(name="Silver",color=discord.Color.from_rgb(96,96,96))
  await guild.create_role(name="Gold",color=discord.Color.from_rgb(204,204,0))
  await guild.create_role(name="Platinum",color=discord.Color.from_rgb(0,76,153))
  await guild.create_role(name="Diamond",color=discord.Color.from_rgb(0,255,255))
  await guild.create_role(name="Master",color=discord.Color.from_rgb(127,0,255))
  await guild.create_role(name="Grand Master",color=discord.Color.from_rgb(204,0,0))

people = []
keep_alive()
while True:

    

  
  
  
  
  
  
  @client.event
  async def on_message(message):

    current_guild = str(message.guild.id)
    #print(current_guild)
  
  
    #if message.author.id == 758509998459977768:
      #await message.channel.send("Bro stop talking.")
      #await message.channel.send("No one asked.")
    
    
    if message.author == client.user:
      #print("I have spoken.")
      return

    if message.content.startswith("+daily"):
      #print(people)
      author = message.author
      used = True
      for x in people:
        if x == str(author.id):
          used = False
      if used == True:
        await message.channel.send("You have already used you 1 daily from Universal Bot.")
      else:
        value = randint(0,1500)

        users = await get_bank_data(current_guild)
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
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+= value
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)

        for x in people:
          if x == str(author.id):
            people.remove(x)
        #print(people)
        await message.channel.send("You have gained " + str(value) + " from your daily today!" )

        
        

    #########################################################################################
    #                               HELP METHODS
    #########################################################################################

    #General Help
    #=========================================
    if message.content.startswith("+help"):
      em = discord.Embed(title = "Universal Bot Actions",description="In order to use Universal Bot make sure to use `+` before each command.", color = discord.Color.red())
      em.add_field(name = "👋 Greeting", value= "`hello`")
      em.add_field(name = "🤣 Jokes", value= "`meme`  ``\ndadjoke``")
      em.add_field(name = "❓ Query", value= "`yquery!(search)`  ``\nrquery!(search)``")
      em.add_field(name = "💵 Economy (for Ranks)", value= "``balance``  ``\nfunds!(amount)`` ``\ndeposit!(amount)`` ``\nwithdraw!(amount)`` ``\n(user)transfer!(amount)`` ``\nchance`` ``\ndaily``",inline=False)
      

      
      em.add_field(name="Hub",value="[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=982335220701356072&permissions=292527568960&scope=bot) • [Support Server](https://discord.gg/dYxG8BgZ) • [Commands](https://github.com/lab596/UniversalBot/blob/main/README.md)")

      em.set_footer(text="For detailed info about each command please visit the 'Commands' link above. Use `rhelp` to have the ranks explained.")

      await message.channel.send(embed=em)

    #Rank Help
    #=========================================
    if message.content.startswith("+rhelp"):
      emb = discord.Embed(title = "Ranks", description="These are the prestige ranks within the economy system. These ranks can be purchased with economy money.", color = discord.Color.blue())
      emb.add_field(name = "Bronze ~ Cost: 1500", value= "`bbronze`",inline = True)
      emb.add_field(name = "Silver ~ Cost: 3000", value= "`bsilver`",inline = True)
      emb.add_field(name = "Gold ~ Cost: 6000", value= "`bgold`",inline = True)
      emb.add_field(name = "Platinum ~ Cost: 12000", value= "`bplat`",inline = True)
      emb.add_field(name = "Diamond ~ Cost: 12000", value= "`bdia`",inline = True)
      emb.add_field(name = "Master ~ Cost: 24000", value= "`bmas`",inline = True)
      emb.add_field(name = "Grand Master ~ Cost: 50000", value= "`bgmas`",inline = True)
      emb.add_field(name = "Lottery Command", value= "`chance`",inline = True)
      emb.set_footer(text="You gain money everyday through interest. You can also gain or lose money using the chance command.")
      
      await message.channel.send(embed=emb)

    #########################################################################################
    #                               HELLO METHOD
    #########################################################################################
       
    if message.content.startswith("+hello"):
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

    #########################################################################################
    #                               QUERY METHODS
    #########################################################################################

    #Reddit Search
    #=========================================
    if message.content.startswith('+rquery!'):
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

    #Youtube Search
    #=========================================
    if message.content.startswith("+yquery!"):
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
      a=0;
      for i in search_results:
        if(a>0):
          #print(i)
          #print(search_results[a])
          if(i != search_results[a-1]):            
            top_res.append(i)
        else:
          top_res.append(i)
        a+=1
      #print(top_res)  
      c = 1
      j=5
      #print(top_res)
      await message.channel.send("Top 5 results:")
      while j > 0:
        if c == 1: 
          await message.channel.send(str(c)+") "+'http://www.youtube.com'+top_res[c-1])
        else:
          await message.channel.send(str(c)+") "+'<http://www.youtube.com'+top_res[c-1]+">")
        j-=1
        c+=1

    #########################################################################################
    #                               JOKE METHODS
    #########################################################################################

    #Dad Jokes
    #=========================================
    if message.content.startswith("+dadjoke"):
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
      
    #Memes
    #=========================================
    if message.content.startswith("+meme"):
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
  
  
    #########################################################################################
    #                               ECONOMY METHODS
    #########################################################################################

    #Balance
    #=========================================
    if message.content.startswith("+balance"):
      author = message.author
      await open_account(author,current_guild)
      users = await get_bank_data(current_guild)
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
  
    #Funds
    #=========================================
    if message.content.startswith("+funds!"):
      if message.author.guild_permissions.administrator:
        command = message.content
        amt = command[7:len(command)]
        author = message.author
        #await open_account(author)
        #users = await get_bank_data()
        earnings = int(amt)

        users = await get_bank_data(current_guild)
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

        count = 0
        f=open("bank.json",'r+')
        data = json.load(f)
        #print(data)
        #print(data['bank_details'])
        for a in data[current_guild]: ###
          #print(i)
          #print(i[str(author.id)])
          #print(i[str(author.id)]['wallet'])
          if count == m:
            a[str(author.id)]['wallet']+=earnings
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
    
    #Deposit
    #=========================================
    if message.content.startswith("+deposit!"):
      command = message.content
      amt = command[9:len(command)]
      author = message.author


      
      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<int(amt):
            await message.channel.send("You lack the required funds to complete this deposit.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          k[str(author.id)]['wallet']-=int(amt)
          k[str(author.id)]['bank']+=int(amt)
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)
        
      await message.channel.send("Deposit successful.")

    #Withdraw
    #=========================================
    if message.content.startswith("+withdraw!"):
      command = message.content
      amt = command[10:len(command)]
      author = message.author
      
      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['bank'])<int(amt):
            await message.channel.send("You lack the required funds to complete this withdrawl.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          k[str(author.id)]['wallet']+=int(amt)
          k[str(author.id)]['bank']-=int(amt)
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)
  
      await message.channel.send("Withdrawl successfull.")
      
    #Transfer
    #=========================================
    if "+transfer!" in message.content:
      command = message.content
      author = message.author
      user = command.split("+")
      usera = user[0]
      amt = command.split("!")
      amta = amt[1]
      if not(message.author.guild_permissions.administrator) and int(amta) < 0:
        await message.channel.send("You are not authorized to take money.")
        return
        
      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]:
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
          for i in data[current_guild]:
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
        await message.channel.send("This can be done by typing '+balance'.")
        return
            
      await message.channel.send("Funds transfered successfully.")

    #########################################################################################
    #                               RANK METHODS
    #########################################################################################

    #Bronze Purchase
    #=========================================
    if message.content.startswith("+bbronze"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<1500:
            await message.channel.send("You lack the required funds to complete this purchase.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          if k[str(author.id)]['prestige']== 'unranked':
            k[str(author.id)]['prestige']= 'BRONZE'
            k[str(author.id)]['wallet']-= 1500
            author1 = str(author)
            authorn1 = author1.split("#")
            authorn = authorn1[0]
            await author.edit(nick=str(authorn)+"🟫")
            role = get(message.guild.roles, name='Bronze')
            await author.add_roles(role)
          else:
             await message.channel.send("Must be unranked to purchase this rank.")
             return
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)

      await message.channel.send(str(author) + " has been promoted to bronze!")
      await message.channel.send("You have been renamed to "+ str(authorn)+"🟫")
    #Silver Purchase
    #=========================================
    if message.content.startswith("+bsilver"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<3000:
            await message.channel.send("You lack the required funds to complete this purchase.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          if k[str(author.id)]['prestige']== 'BRONZE':
            k[str(author.id)]['prestige']= 'SILVER'
            k[str(author.id)]['wallet']-= 3000
            author1 = str(author)
            authorn1 = author1.split("#")
            authorn = authorn1[0]
            await author.edit(nick=str(authorn)+"⬜")
            role1 = get(message.guild.roles, name='Bronze')
            await author.remove_roles(role1)
            role = get(message.guild.roles, name='Silver')
            await author.add_roles(role)
          else:
             await message.channel.send("Must be bronze to purchase this rank.")
             return
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)

      await message.channel.send(str(author) + " has been promoted to silver!")
      await message.channel.send("You have been renamed to "+ str(authorn)+"⬜")

    #Gold Purchase
    #=========================================
    if message.content.startswith("+bgold"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<6000:
            await message.channel.send("You lack the required funds to complete this purchase.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          if k[str(author.id)]['prestige']== 'SILVER':
            k[str(author.id)]['prestige']= 'GOLD'
            k[str(author.id)]['wallet']-= 6000
            author1 = str(author)
            authorn1 = author1.split("#")
            authorn = authorn1[0]
            await author.edit(nick=str(authorn)+"🟨")
            role1 = get(message.guild.roles, name='Silver')
            await author.remove_roles(role1)
            role = get(message.guild.roles, name='Gold')
            await author.add_roles(role)
          else:
             await message.channel.send("Must be silver to purchase this rank.")
             return
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)

      await message.channel.send(str(author) + " has been promoted to gold!")
      await message.channel.send("You have been renamed to "+ str(authorn)+"🟨")
    
    #Plat Purchase
    #=========================================
    if message.content.startswith("+bplat"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<12000:
            await message.channel.send("You lack the required funds to complete this purchase.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          if k[str(author.id)]['prestige']== 'GOLD':
            k[str(author.id)]['prestige']= 'PLAT'
            k[str(author.id)]['wallet']-= 12000
            author1 = str(author)
            authorn1 = author1.split("#")
            authorn = authorn1[0]
            await author.edit(nick=str(authorn)+"⬛")
            role1 = get(message.guild.roles, name='Gold')
            await author.remove_roles(role1)
            role = get(message.guild.roles, name='Platinum')
            await author.add_roles(role)
          else:
             await message.channel.send("Must be gold to purchase this rank.")
             return
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)

      await message.channel.send(str(author) + " has been promoted to platinum!")
      await message.channel.send("You have been renamed to "+ str(authorn)+"⬛")
    
    #Dia Purchase
    #=========================================
    if message.content.startswith("+bdia"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<12000:
            await message.channel.send("You lack the required funds to complete this purchase.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          if k[str(author.id)]['prestige']== 'PLAT':
            k[str(author.id)]['prestige']= 'DIA'
            k[str(author.id)]['wallet']-= 12000
            author1 = str(author)
            authorn1 = author1.split("#")
            authorn = authorn1[0]
            await author.edit(nick=str(authorn)+"🟦")
            role1 = get(message.guild.roles, name='Platinum')
            await author.remove_roles(role1)
            role = get(message.guild.roles, name='Diamond')
            await author.add_roles(role)
          else:
             await message.channel.send("Must be platinum to purchase this rank.")
             return
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)

      await message.channel.send(str(author) + " has been promoted to diamond!")
      await message.channel.send("You have been renamed to "+ str(authorn)+"🟦")
    
    #Master Purchase
    #=========================================
    if message.content.startswith("+bmas"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<24000:
            await message.channel.send("You lack the required funds to complete this purchase.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          if k[str(author.id)]['prestige']== 'DIA':
            k[str(author.id)]['prestige']= 'MAST'
            k[str(author.id)]['wallet']-= 24000
            author1 = str(author)
            authorn1 = author1.split("#")
            authorn = authorn1[0]
            await author.edit(nick=str(authorn)+"🟪")
            role1 = get(message.guild.roles, name='Diamond')
            await author.remove_roles(role1)
            role = get(message.guild.roles, name='Master')
            await author.add_roles(role)
          else:
             await message.channel.send("Must be diamond to purchase this rank.")
             return
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)

      await message.channel.send(str(author) + " has been promoted to master!")
      await message.channel.send("You have been renamed to "+ str(authorn)+"🟪")

    #GMaster Purchase
    #=========================================
    if message.content.startswith("+bgmas"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<50000:
            await message.channel.send("You lack the required funds to complete this purchase.")
            return
        count1+=1
      
      count1=0
      for k in data[current_guild]: ###
        if((count1)==m):
          if k[str(author.id)]['prestige']== 'MAST':
            k[str(author.id)]['prestige']= 'GMAST'
            k[str(author.id)]['wallet']-= 50000
            author1 = str(author)
            authorn1 = author1.split("#")
            authorn = authorn1[0]
            await author.edit(nick=str(authorn)+"🟥")
            role1 = get(message.guild.roles, name='Master')
            await author.remove_roles(role1)
            role = get(message.guild.roles, name='Grand Master')
            await author.add_roles(role)
          else:
             await message.channel.send("Must be master to purchase this rank.")
             return
        count1+=1
      with open("bank.json",'w') as o:
        json.dump(data,o,indent=4)

      await message.channel.send(str(author) + " has been promoted to grand master!")
      await message.channel.send("You have been renamed to "+ str(authorn)+"🟥")

    #########################################################################################
    #                               Chance METHODS
    #########################################################################################

    #Chance
    #=========================================
    if message.content.startswith("+chance"):
      author = message.author

      users = await get_bank_data(current_guild)
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
      for k in data[current_guild]: ###
        if((count1)==m):
          if int(k[str(author.id)]['wallet'])<=100:
            await message.channel.send("You lack the required funds to play chance.")
            return
        count1+=1
      
      value = randint(0,43)
      #print(value)
      if (value == 0):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Advance to Boardwalk.")
        await message.channel.send("You and your family enjoy a nice treat. You spend $50")
        await message.channel.send("$50 dollars ; loss")
      
      if (value == 1):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=200
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Advance to Go (Collect $200)")
        await message.channel.send("$200 dollars ; gain")

      if (value == 2):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=100
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled")
        await message.channel.send("Unfortunately for you, I own that railroad. You owe me $100.")
        await message.channel.send("$100 dollars ; loss")

      if (value == 3):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Bank pays you dividend of $50")
        await message.channel.send("$50 dollars ; gain")

      if (value == 4):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Go to Jail. Go directly to Jail, do not pass Go, do not collect $200")
        await message.channel.send("Bail from jail costs $50.")
        await message.channel.send("$50 dollars ; loss")

      if (value == 5):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=150
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Your building loan matures. Collect $150")
        await message.channel.send("$150 dollars ; gain")

      if (value == 6):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=15
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Speeding fine $15")
        await message.channel.send("$15 dollars ; loss")

      if (value == 7):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=195
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You are assessed for street repair. $40 per house. $115 per hotel")
        await message.channel.send("As a buisnessman, you own 2 houses and 1 hotel.")
        await message.channel.send("$195 dollars ; loss")

      if (value == 8):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=10
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You have won second prize in a beauty contest. Collect $10")
        await message.channel.send("$10 dollars ; gain")

      if (value == 9):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=100
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Get Out of Jail Free")
        await message.channel.send("You sell it to an inmate for $100")
        await message.channel.send("$100 dollars ; gain")

      if (value == 10):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=20
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You buy minecraft.")
        await message.channel.send("$20 dollars ; loss")

      if (value == 11):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=10
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Emotional Damage.")
        await message.channel.send("$10 dollars ; loss")

      if (value == 12):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=15
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Pay poor tax of $15")
        await message.channel.send("$15 dollars ; loss")

      if (value == 13):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=15
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Life insurance matures.")
        await message.channel.send("$50 dollars ; gain")

      if (value == 14):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=10
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You donate your birthday money to a community center. Keep a little for yourself. COLLECT $10.")
        await message.channel.send("$10 dollars ; gain")

      if (value == 15):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=10
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You volunteered at a blood drive. There were free cookies! COLLECT $10.")
        await message.channel.send("$10 dollars ; gain")

      if (value == 16):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=100
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You spend the day playing games with kids at a local children’s hospital. COLLECT $100.")
        await message.channel.send("$100 dollars ; gain")

      if (value == 17):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You buy a few bags of cookies from that school bake sale. Yum! PAY $50.")
        await message.channel.send("$50 dollars ; loss")

      if (value == 18):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You didn’t shop local! PAY $50")
        await message.channel.send("$50 dollars ; loss")

      if (value == 19):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Your cousin forgot their wallet! You happily pay for dinner. PAY $50.")
        await message.channel.send("$50 dollars ; loss")

      if (value == 20):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=15
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You do someones homework for them. They pay you.")
        await message.channel.send("$15 dollars ; gain")

      if (value == 21):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You set aside time every week to hang out with your elderly neighbor – you’ve heard some amazing stories! COLLECT $100")
        await message.channel.send("$100 dollars ; gain")

      if (value == 22):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=20
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Meow! You knit cozy sweaters for the hairless cats at your local animal shelter. COLLECT $20.")
        await message.channel.send("$20 dollars ; gain")

      if (value == 23):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=100
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You volunteer to run the social media accounts for a non-profit art center, and you meet some pretty talented people! COLLECT $100.")
        await message.channel.send("$100 dollars ; gain")

      if (value == 24):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=25
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You organize a bake sale for your local school. COLLECT $25.")
        await message.channel.send("$25 dollars ; gain")

      if (value == 25):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=100
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Your mom throws her slipper at you. You incur emotional damage.")
        await message.channel.send("$100 dollars ; loss")
           
      if (value == 26):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You decide to gamble. The luck never favors you!")
        await message.channel.send("$50 dollars ; loss")

      if (value == 27):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Fortune favors the brave. Luckily you seem brave.")
        await message.channel.send("$50 dollars ; gain")

      if (value == 28):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=1000
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You win the lottery!")
        await message.channel.send("$1000 dollars ; gain")

      if (value == 29):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=150
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("A monster eats your fammily. They cost $50 each.")
        await message.channel.send("$150 dollars ; loss")

      if (value == 30):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=20
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You smell.")
        await message.channel.send("$20 dollars ; loss")

      if (value == 31):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You get promoted to boss. But the party costs some mola.")
        await message.channel.send("$50 dollars ; loss")

      if (value == 32):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Mario appears and hands you a crisp $50.")
        await message.channel.send("$50 dollars ; gain")

      if (value == 33):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=20
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You get eaten.")
        await message.channel.send("$20 dollars ; loss")

      if (value == 34):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You rob a bank.")
        await message.channel.send("$50 dollars ; gain")

      if (value == 35):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=25
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("I rob you.")
        await message.channel.send("$25 dollars ; loss")

      if (value == 36):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=150
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("The pope himself blesses your dog water and turns it into holy water. You sell it.")
        await message.channel.send("$150 dollars ; gain")

      if (value == 37):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Lebron James dunks on you.")
        await message.channel.send("$50 dollars ; loss")

      if (value == 38):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=25
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Why do you look like that?")
        await message.channel.send("$25 dollars ; loss")

      if (value == 39):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=100
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("A seagull drops a gold brick on your head")
        await message.channel.send("$100 dollars ; gain")

      if (value == 40):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("Lazerbeam hits you with his lazer beam.")
        await message.channel.send("$50 dollars ; loss")

      if (value == 41):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']+=50
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You like cheese curds.")
        await message.channel.send("$50 dollars ; gain")

      if (value == 42):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=100
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You play Fortnite?")
        await message.channel.send("$100 dollars ; loss")

      if (value == 43):
        count1=0
        for k in data[current_guild]: ###
          if((count1)==m):
            k[str(author.id)]['wallet']-=1000
          count1+=1
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
        await message.channel.send("You looked at me weird.")
        await message.channel.send("$1000 dollars ; loss")

      
      
    
        
  #Other Methods
  #==================================================================================
  def write_json(new_data,id, filename='bank.json'):
      with open(filename,'r+') as file:
          # First we load existing data into a dict.
          file_data = json.load(file)
          # Join new_data with file_data inside emp_details
          file_data[id].append(new_data)
          # Sets file's current position at offset.
          file.seek(0)
          # convert back to json.
          json.dump(file_data, file,indent=4)
  
  
  
      
  async def open_account(user,id):
    #print(id)
    with open("bank.json","r") as f:
      users = json.load(f)[id]
    for i in users:
      vals = i.keys()
      for x in vals:
        if x == str(user.id):
          return False
    else:
      users = {}
      users[str(user.id)] = {}
      users[str(user.id)]["wallet"]= 5
      users[str(user.id)]["bank"]= 0
      users[str(user.id)]["prestige"]= "unranked"
     
      write_json(users,id)
    
    return True
  
  async def get_bank_data(id):
    with open("bank.json","r") as f:
      users = json.load(f)[id]
    return users



  #Bank Interest
  #==================================================================================
  def interest():
    #print("Bank updated.")
      
    Timer(60,interest).start()
    with open("bank.json","r+") as f:
      guilds = json.load(f)
      #print("I am here")
      guild = []
      for i in guilds.keys():
        guild.append(i)
  
      for j in guild:
        pkeys = []
        with open("bank.json","r+") as f:
          users = json.load(f)[str(j)]
        for l in users:
          pkeys.append(l.keys())
          #print(j)
          keys = []
          for k in pkeys:
            k = str(k)
            k1 = k.split("'")
            k = k1[1]
            k2 = k.split("'")
            k=k2[0]
            keys.append(k)
          #print(keys)
  
        count = 0
        f=open("bank.json",'r+')
        data = json.load(f)
        #print(j)
        for i in data[str(j)]:
          a = 0.0 + i[str(keys[count])]['bank']
          #print(a)
          i[str(keys[count])]['bank'] = a + 0.25
          count+=1
  
        with open("bank.json",'w') as o:
          json.dump(data,o,indent=4)
  
  interest()

  #########################################################################################
  #                               Daily METHODS
  #########################################################################################
  def daily():
    Timer(86400,daily).start()
    with open("bank.json","r+") as f:
      guilds = json.load(f)
    #print("I am here")
    guild = []
    for i in guilds.keys():
      guild.append(i)
    
    for j in guild:
      pkeys = []
      with open("bank.json","r+") as f:
        users = json.load(f)[str(j)]
      for l in users:
        pkeys.append(l.keys())
        #print(j)
        keys = []
        for k in pkeys:
          k = str(k)
          k1 = k.split("'")
          k = k1[1]
          k2 = k.split("'")
          k=k2[0]
          keys.append(k)
  
        for i in keys:
          if(not(i in people)):
            people.append(i)
  daily()

  #Bot Running
  #==================================================================================
  client.run(os.getenv('TOKEN'))



      
    
    
  
