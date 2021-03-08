import requests
from bs4 import BeautifulSoup
TOKEN = 'bot token' # enter bot token
channel = client.get_channel("Enter channel id") # Enter channel ID for live updates


class Person:
  def __init__(self, name,twitchUrl, css):
    self.name = name
    self.twitchUrl = twitchUrl
    self.css = css

def checkIsLive(css,soup):
    results= soup.select(css)
    #if(len(results) == 0):
    #   return(False)
    for div in results:

      if(div.text == "Live"):
        return True
      else:
        return False    
oldList = []
newList = []
oldList.append("check")
userList = []
URL = 'https://twitch.facepunch.com/'

iRisk = Person("iRisk","https://www.twitch.tv/iRiskpvp","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(1) > div.drop-header > div > div.streamer-item > div")
bnans = Person("bnans","https://www.twitch.tv/bnans","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(2) > div.drop-header > div > div.streamer-item > div")
swales = Person("swales","https://www.twitch.tv/Swales94","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(3) > div.drop-header > div > div.streamer-item > div")

shroud = Person("shroud","https://www.twitch.tv/shroud","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(4) > div.drop-header > div > div.streamer-item > div")
r00t9r = Person("r00t9r","https://www.twitch.tv/r00t9r","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(5) > div.drop-header > div > div.streamer-item > div")
albin = Person("albin","https://www.twitch.tv/Albin","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(6) > div.drop-header > div > div.streamer-item > div")

ricoy=  Person("ricoy","https://www.twitch.tv/ricoy23","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(7) > div.drop-header > div > div.streamer-item > div")
bloo=  Person("bloo","https://www.twitch.tv/Blooprint","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(8) > div.drop-header > div > div.streamer-item > div")
death=  Person("death","https://www.twitch.tv/deathwingua","body > section.section.streamer-drops > div > div.drops-group.is-3 > a:nth-child(9) > div.drop-header > div > div.streamer-item > div")

userList.append(iRisk)
userList.append(bnans)
userList.append(swales)

userList.append(shroud)
userList.append(r00t9r)
userList.append(albin)

userList.append(ricoy)
userList.append(bloo)
userList.append(death)

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(checkIsLive(iRisk.css, soup))
print(checkIsLive(bnans.css, soup))

print("done")

import os

import discord
import time
import asyncio





client = discord.Client()

async def CheckWhoIsLiveLoop(oldList):
    

    while True:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        print (oldList)

        for user in userList:
          if(checkIsLive(user.css, soup)):
            newList.append(user.name)
            if(not user.name in oldList):
              await channel.send( user.name + "is now live at: " + user.twitchUrl )

        oldList.clear()
        oldList = newList.copy()
        print (oldList)
        newList.clear()
        print(oldList)
        await asyncio.sleep(60) # task runs every 60 seconds
        
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Do 'RustDrops'"))
    await CheckWhoIsLiveLoop(oldList)

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if message.content == 'RustDrops':
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        for user in userList:
          if(checkIsLive(user.css, soup)):
            await message.channel.send( user.name + "is now live at: " + user.twitchUrl)
   

client.run(TOKEN)



