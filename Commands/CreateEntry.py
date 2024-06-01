import re
import config
import discord

from discord.ext import commands
from discord import app_commands

class CreateEntry(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    # create_group = app_commands.Group(name="create", description="Commands related to creating an entry")

    # @create_group.command(name="deployment-entry", description="Create a deployment entry.")
    # async def create_deployment_entry(self, interaction: discord.Interaction, serial_no: int, title: str, host: discord.Member, assistant: discord.Member, time: str, attendees: str, after_action_report: str, image: discord.Attachment=None):
    #     if image:
    #         if image.content_type != 'image/jpeg':
    #             await interaction.response.send_message(embed=discord.Embed(description="{} **Only Image attachements are supported!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
    #             return
            
    #     pattern = r'<@(\d+)>'
    #     matches = re.findall(pattern, attendees)
    #     attendees_data = ""

    #     if matches == []:
    #         await interaction.response.send_message(embed=discord.Embed(description="{} **Please mentioned atleast one attendee!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
    #         return

    #     for match in matches:
    #         user = interaction.guild.get_member(int(match))
    #         attendees_data += f"{config.ARROW_EMOJI} {user.mention}\n"

    #     entry = f"""
    #             |▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[{config.TFC_EMOJI}]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬|\
    #             \n[{config.TFC_EMOJI}] **__Entry: #{serial_no:04d}__**\
    #             \n{title}\
    #             \n\
    #             \n*Game Host:*\
    #             \n{config.ARROW_EMOJI} {host.mention}\
    #             \n*Assistant:*\
    #             \n{config.ARROW_EMOJI} {assistant.mention}\
    #             \n*Time:*\
    #             \n{config.ARROW_EMOJI} {time}\
    #             \n|▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[{config.TFC_EMOJI}]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬|\
    #             \n[{config.TFC_EMOJI}] **__Attendees__**\
    #             \n\
    #             \n{attendees_data}\
    #             \n\
    #             \n|▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[{config.TFC_EMOJI}]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬|\
    #             \n{after_action_report}\
    #             """
    #     print(image.content_type)

    #     if image is None:
    #         await interaction.response.send_message(content=entry, ephemeral=True)
    #     else:
    #         await interaction.response.send_message(content=entry, file=image, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(CreateEntry(bot))