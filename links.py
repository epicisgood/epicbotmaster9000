import discord
from discord.ext import commands, bridge
import discord.utils


class Link_commands(commands.Cog):

  def __init__(self, client):
    self.client = client

  @bridge.bridge_command(aliases=["links"],
                         description="Link dispenser for interstellar links")
  async def link(self, ctx):
    await ctx.reply(embed=discord.Embed(
        title="Links!",
        description="Click the link button below!",
        color=0x00ff00),
                    view=Interstellar_buttons())


class Interstellar_buttons(discord.ui.View):

  @discord.ui.button(label="Private links", style=discord.ButtonStyle.primary)
  async def link(self, button, interaction: discord.Interaction):
    #if interaction.user.id == 726162926851063919:  #Myself lol
      #await interaction.response.send_message(
          #content="lol this is so cool guys", ephemeral=True)
    if interaction.user.id == 1154785751293247548:  #jackcampbell
      await interaction.response.send_message(
          content="https://british-education.onrender.com/", ephemeral=True)
    elif interaction.user.id == 869697201100714074:  #Mr.Storm
      await interaction.response.send_message(
          content="https://rocky-mountains.onrender.com/", ephemeral=True)
    elif interaction.user.id == 1020747577240588289:  #Bando Jr
      await interaction.response.send_message(
          content=" https://common-language.onrender.com/", ephemeral=True)
    else:
      await interaction.response.send_message(
          content=
          "<@726162926851063919> me for your personal link and ill add it to the link bot",
          ephemeral=True)

  @discord.ui.button(label="Public links", style=discord.ButtonStyle.secondary)
  async def public_links(
      self,
      button,
      interaction: discord.Interaction,
  ):
    links_public = {
        '1st link': "https://royal-king.onrender.com/",
        '2nd link': "https://checkers-jacket.onrender.com/",
        '3rd link': "https://map-education.onrender.com/",
        '4th link': "https://electric-indigo.onrender.com/"
    }
    public_link_embed = discord.Embed(title="Public links",
                                      color=discord.Color.green())
    for key, value in links_public.items():
      public_link_embed.add_field(name=key, value=value, inline=False)
    await interaction.response.send_message(
        content="**You can share these link to anyone**",
        embed=public_link_embed,
        ephemeral=True)


def setup(client):
  client.add_cog(Link_commands(client))
