import discord

from dotenv import load_dotenv

load_dotenv()
import os

from langchain_core.messages import HumanMessage,AIMessage
from agent import  agent
import asyncio



intents = discord.Intents.default() #YE DEFAULT PERMISION DI SARI HAI 

intents.message_content = True #ye ham ish liye use kerte serve jo mesaage ae uska contain pad pae


client = discord.Client(intents=intents)

@client.event #decorater hai 
async def on_message(message): #jo event vale function async tara hi use ho pae ge
  # print(message.content) #server message ae yaha pe print hoga

  if message.author == client.user: #ishka matlb jab bot message bejta vo kudh reply hello na bheje
    return
  async with message.channel.typing(): #jab tak message hi ata ai typing show kare ga
    content = message.content #content jo aya ushe content store ker liya hai

    response = await agent.ainvoke({
      "messages":[HumanMessage(content=content)]},
      config={"configurable":{"message":message,"loop":asyncio.get_event_loop}} #config use agent jite tool use ker raha hai uske under hamko parameter pass kerna hota tab config use kerte hai
      
      )
    
    agent_message = response["messages"][-1].text #-1 matlb hota last wala message
  
  await message.channel.send(agent_message) #yaha se reply deta hai




client.run(token=os.getenv("DISCORD_API_KEY")) #ishko online ker rahe hai