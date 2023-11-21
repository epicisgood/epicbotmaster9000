import pytz, time, datetime, asyncio, re
from dateparser import parse
import discord
from discord.ext.commands import MissingRequiredArgument
from discord.ext import bridge, commands


class Time_commands(commands.Cog):

  def __init__(self, client):
    self.client = client

  @bridge.bridge_command(aliases=["epo"],
                         description="convert epooch time to readable time")
  async def epooch(self, ctx, epooch: str):
    # Remove any non-numeric characters from the input
    epoch_time = ''.join(filter(str.isdigit, epooch))

    try:
      epoch_time = int(epoch_time[:10])
      est = pytz.timezone('US/Eastern')
      est_time = datetime.datetime.utcfromtimestamp(epoch_time).replace(
          tzinfo=pytz.utc).astimezone(est)
      readable_time = est_time.strftime('%Y %b %d, %I:%M:%S %p')
      await ctx.reply(readable_time)
    except ValueError:
      await ctx.reply('Invalid epoch time provided.')

  
  @bridge.bridge_command(aliases=["rem"], description="Set a reminder with 1s,1m,1h,1d")
  async def remind(self, ctx, time: str, *, content: str):
    def convert(time):
      pos = ['s', 'm', 'h', 'd', 'sec', 'min', 'hour', 'day']

      time_dict = {
          "s": 1,
          "m": 60,
          "h": 3600,
          "d": 3600 * 24,
      }

      unit = time[-1]

      if unit not in pos:
        return -1
      try:
        val = int(time[:-1])
      except ValueError:
        return -2
      except MissingRequiredArgument:
        return -2

      return val * time_dict[unit]

    converted_time = convert(time)

    if converted_time == -1:
      await ctx.reply("You didn't answer the time correctly.")
      return
    if converted_time == -2:
      await ctx.reply("The time was not an integer. Example: !remind 1m hello")
      return
    await ctx.reply(
        content=f'Your reminder will activate in {time} content "{content}".', ephemeral=True)
    await asyncio.sleep(converted_time)
    await ctx.reply(f"{ctx.author.mention} {content}")


def setup(client):
  client.add_cog(Time_commands(client))
