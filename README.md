# 🤖 UniversalBot 🤖
Using python to make a discord bot that can respond to a variety of commands.

Coded in *replit.com*

Bot invite code: https://discord.com/api/oauth2/authorize?client_id=982335220701356072&permissions=17381259328&scope=bot

# 📨 Commands 📨
* ❓ Help ❓
   - Keyword: "+help"
   - Action: Will provide a list of all supported commands and their purpose - similiar to this page that outlines commands.
 
* 👋 Hello 👋
   - Keyword: "+hello"
   - Action: Will respond with a variety of seven unique responses - one is randomly selected.

* 👨 Dad Jokes 👨
   - Keyword: "+dadjoke"
   - Action: Uses reddit api and refrences *dadjokes (r/dadjokes)* subreddit to randomly pull one of the fifty popular posts.
 
* 🤣 Memes 🤣
   - Keyword: "+meme"
   - Action: Uses reddit api and refrences *dankmemes (r/dankmemes)* or *meme (r/meme)* (randomly chooses one each time) subreddit to randomly pull one of the fifty popular posts.
  
* 🎞 Youtube Search 🎞
   - Keyword: "+yquery!(search)"
   - Action: Refrences youtube.com and searches what is inputed. Outputs top five videos that show up as a result of that search.

* 👹 Reddit Search 👹
   - Keyword: "+rquery!(search)"
   - Action: Refrences reddit.com and searches what is inputed. Outputs top three of the top posts that show up as a result of that search. Additionally it provides a link to that subreddit.

---
# 💲 Economy 💲 #

* ⚖️ Balance ⚖️
   - Keyword: "+balance"
   - Action: First, it checks if the user typing the command has a balance at all, if not it creates an account for them and provides starting money. It then prints their money in an embed that displays money in the wallent and in the bank.

* 💸 Funds 💸
   - Keyword: "+funds!(amount)"
   - Action: *This is an admin action only* - transfers amount provided to the wallet of the author of the command.

* 🎁 Transfer 🎁
   - Keyword: "(user)+transfer!(amount)"
   - Action: It transfers money between two accounts
       - *Admin* - can transfer negative money (taking money out of someones account and adding it to their own)

* 🏦 Deposit 🏦
   - Keyword: "+deposit!(amount)"
   - Action: Moves money from ones wallet to their bank
 
 * 💵 Withdraw 💵
   - Keyword: "+withdraw!(amount)"
   - Action: Moves money from bank to wallet in orfer to allow for purchases 
 
  * 🃏 Chance 🃏
   - Keyword: "+chance"
   - Action: Calls a random action that can either give or take money from one's account 

 * 💰 Daily 💰
   - Keyword: "+daily"
   - Action: Gives a random amount of money. This action call only be called once everyday from every user. (*Can only use 1 even within muiltiple servers) 
