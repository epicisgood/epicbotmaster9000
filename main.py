import discord
from discord.ext import bridge
import os

my_secret = os.environ['TOKEN']

intents = discord.Intents.all()
client = bridge.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
  print(f"{client.user} is working")
  

@client.bridge_command()
async def ping(ctx):
  await ctx.reply(f"Pong! {round(client.latency * 1000)}ms") 



client.load_extensions('utils',"setup", "links")

client.run(my_secret)
