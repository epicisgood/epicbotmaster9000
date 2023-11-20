import pytz, time, datetime, asyncio
from dateparser import parse
import discord
from discord.ext import bridge, commands


class Epooch_command(commands.Cog):
  def __init__(self, client):
      self.client = client
  @bridge.bridge_command(aliases=["epo"],description="convert epooch time to readable time")
  async def epooch(self,ctx, epooch: str):
      # Remove any non-numeric characters from the input
      epoch_time = ''.join(filter(str.isdigit, epooch))

      try:
          epoch_time = int(epoch_time[:10])
          est = pytz.timezone('US/Eastern') 
          est_time = datetime.datetime.utcfromtimestamp(epoch_time).replace(tzinfo=pytz.utc).astimezone(est) 
          readable_time = est_time.strftime('%Y %b %d, %I:%M:%S %p')
          await ctx.reply(readable_time)
      except ValueError:
          await ctx.reply('Invalid epoch time provided.')

  @bridge.bridge_command(description="Set a reminder")
  async def remind(self, ctx, time: str, *, reminder: str):
    specified_time = parse(time)
    self.local_timezone = pytz.timezone('America/New_York')

    if specified_time is None:
        await ctx.reply("Invalid time format. Please use a valid time expression.")
        return

    current_time = datetime.datetime.now()
    time_difference = specified_time - current_time
    time_in_seconds = max(0, int(time_difference.total_seconds()))

    if time_in_seconds == 0:
        await ctx.reply("The specified time has already passed. Please provide a future time.")
        return

    await ctx.reply(f"Reminder set for {time_in_seconds} seconds.")
    await asyncio.sleep(time_in_seconds)
    await ctx.send(reminder)
    
    
  
    


def setup(client):
  client.add_cog(Epooch_command(client))