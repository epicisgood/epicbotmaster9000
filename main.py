import discord
from discord.ext import bridge

intents = discord.Intents.all()
client = bridge.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
  print(f"{client.user} is working")
  

@client.bridge_command()
async def ping(ctx):
  await ctx.reply(f"Pong! {round(client.latency * 1000)}ms") 



cogs = []
client.load_extension("nitro")

client.run('MTE2NzE5MTAxMjU4NjgxNTYyOA.G8AKYO.mtPHzLs-oIb-4FTLNYPJjE8vNbo6SsSVX_jDFE')
