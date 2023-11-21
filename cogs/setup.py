import discord
from discord.ext import bridge, commands
import asyncio

class Nitro_commands(commands.Cog):
  def __init__(self, client):
    self.client = client

  @bridge.bridge_command(description="Create nitro channels")
  async def nitro(self, ctx):
      await ctx.reply(embed=discord.Embed(title="Create channels", description="click a button bellow to create a text channel", color=0x00ffe1), view=Channel_button())
      asyncio.TimeoutError(3600*10)
    
  @bridge.bridge_command(aliases=['del'], description="delete current channnel", manage_channels=True)
  async def delete(self, ctx):      
    await ctx.channel.delete()
    
  


class Channel_button(discord.ui.View):
  @discord.ui.button(label="Nitro Boost", style=discord.ButtonStyle.grey, emoji="🟣")
  async def boost_callback(self,button, interaction: discord.Interaction):
    channel = await interaction.guild.create_text_channel("🟣nitro-boost🟣",topic="nitro boost gw currently going on", category=interaction.channel.category)
    await channel.send(embed=discord.Embed(title="Remove", description="Delete this channel", color=0xff0000),view=delete_button())
    await interaction.response.send_message(content= f" Created Nitro boost channel {channel.mention}", ephemeral=True)


  
  @discord.ui.button(label="Nitro Basic", style=discord.ButtonStyle.secondary, emoji="🔵")
  async def basic_callback(self, button, interaction: discord.Interaction):
    channel = await interaction.guild.create_text_channel("🔵nitro-boost🔵",topic="nitro basic gw currently going on", category=interaction.channel.category)
    await channel.send(embed=discord.Embed(title="Remove", description="Delete this channel", color=0xff0000),view=delete_button())
    await interaction.response.send_message(content= f"Created Nitro basic channel {channel.mention}", ephemeral=True)




class delete_button(discord.ui.View):
  @discord.ui.button(label="delete", style=discord.ButtonStyle.red)
  async def delete_callback(self, button, interaction: discord.Interaction):
    await interaction.channel.delete()




def setup(client):
  client.add_cog(Nitro_commands(client))