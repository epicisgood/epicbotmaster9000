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

client.remove_command("help")


@client.bridge_command()
async def help(ctx):
  await ctx.reply(f"**Help Menu**\n\n**!help** - Shows this menu\n"
                  f"**!ping** - Shows the bot's latency\n"
                  f"**!link** - Interstellar Link dispesner\n"
                  f"**!Nitro** - Makes channels for nitro giveaways\n"
                  f"**!delete** - deletes the current channel the command was run \n"
                  f"**!epooch** - Converts epooch time to readable time !epooch <number> \n"
                  f"**!remind** - Sets a reminder !remind <2s> <message> \n")



client.load_extensions('cogs.utils',"cogs.setup", "cogs.links")

client.run(my_secret)
