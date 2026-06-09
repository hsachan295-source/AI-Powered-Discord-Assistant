from dotenv import load_dotenv
load_dotenv()
import os
import base64
import io
import discord
import asyncio



from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from langchain.tools import tool,ToolRuntime
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

@tool
def generateAndSendImage(prompt:str,runtime:ToolRuntime): #ye tool images generate ker ke deta hai
  """Use this tool generate and send images"""
  llm = ChatOpenAI(model="gpt-5.4-mini")

  config = runtime.config.get("configurable") #config mesaage nikal lege
  message = config.get("message")
  loop = config.get("loop")

 
  tool = {"type": "image_generation", "quality": "low"}

  llm_with_tools = llm.bind_tools([tool])

  ai_message = llm_with_tools.invoke(
      prompt
  )
  image  = ai_message.content_blocks[0]['base64'] #yaha se base64 mile ga fir ham ishko decode kere ge

  base64_string = base64.b64decode(image) #yaha hamne ishko string convert ker liya hai

  image_bytes = io.BytesIO(base64_string) #base64 ushe byte change ker lete hai
  file = discord.File(fp=image_bytes,filename="image_png") #yaha pe bytes se image ko file change kerte hai

  asyncio.run_coroutine_threadsafe(message.channel.send(file=file),loop)

  return "Image generated and send Successfully"


@tool #ek hisab se hamne yaha internet access de diya apne bot search ker ke bataye ga muje 
def surInterNet(query:str): #Docstring string deni padti tool me
  """Use this tool to surf internet get latest information"""
  result = tavily_client.search(query=query)
  return str(result)

agent = create_agent(model=model,tools=[surInterNet,generateAndSendImage],system_prompt="""Provide clean output to the user""")