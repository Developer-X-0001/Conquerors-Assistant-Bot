import config
import discord
import datetime

from discord import ButtonStyle
from discord.ui import Button, View, button

class ApplicationButtons(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Accept", emoji=config.DONE_EMOJI, style=ButtonStyle.gray, custom_id="accept_button")
    async def accept_button(self, interaction: discord.Interaction, button: Button):
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        logs_channel = interaction.guild.get_channel(config.APPLICATION_LOGS_CHANNEL_ID)
        on_topic_channel = interaction.guild.get_channel(config.ON_TOPIC_CHANNEL_ID)
        armory_channel = interaction.guild.get_channel(config.ARMORY_CHANNEL_ID)
        if bot_operator_role in interaction.user.roles:
            self.accept_button.label = "Please Wait"
            self.accept_button.emoji = config.LOAD_EMOJI
            self.accept_button.disabled = True
            self.reject_button.disabled = True
            await interaction.response.edit_message(view=self)

            application_embed = interaction.message.embeds[0]
            callsign = application_embed.fields[3].value[2:]
            user = interaction.message.mentions[0]

            verified_role = interaction.guild.get_role(config.VERIFIED_ROLE_ID)
            enlisted_role = interaction.guild.get_role(config.ENLISTED_ROLE_ID)
            civilian_role = interaction.guild.get_role(config.CIVILIAN_ROLE_ID)
            recruit_role = interaction.guild.get_role(config.RECRUIT_ROLE_ID)
            clearance_level_0_role = interaction.guild.get_role(config.CLEARANCE_LEVEL_0_ROLE_ID)
            recruitment_element_orion_role = interaction.guild.get_role(config.RECRUITMENT_ELEMENT_ORION_ROLE_ID)

            await user.remove_roles(verified_role)
            await user.remove_roles(civilian_role)
            await user.add_roles(enlisted_role)
            await user.add_roles(recruit_role)
            await user.add_roles(recruitment_element_orion_role)
            await user.add_roles(clearance_level_0_role)
            await user.edit(nick="[E-0] REC. \"{}\"".format(callsign))

            self.accept_button.disabled = True
            self.reject_button.disabled = True

            self.accept_button.label = "Accepted"
            self.accept_button.emoji = config.DONE_EMOJI

            application_embed.set_footer(text="Application accepted!")
            await interaction.message.edit(embed=application_embed, view=self)
            welcome_embed = discord.Embed(
                title="Welcome to Task Force \"Conquerors\"",
                description="Welcome to Task Force Conquerors! Your equipment and gear will be down below in the recruitment category in {}. If you have any questions, please put it in the Help desk. Thank you for joining!".format(armory_channel.mention),
                color=config.TFC_GOLD
            )
            welcome_embed.set_image(url="https://i.imgur.com/XaUgVC6.png")
            await on_topic_channel.send(content=user.mention, embed=welcome_embed)
            await logs_channel.send(embed=discord.Embed(description="{} has accepted {}'s application.".format(interaction.user.mention, interaction.message.mentions[0].mention), color=config.TFC_GOLD, timestamp=datetime.datetime.now()))
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
    
    @button(label="Reject", emoji=config.ERROR_EMOJI, style=ButtonStyle.gray, custom_id="reject_button")
    async def reject_button(self, interaction: discord.Interaction, button: Button):
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        logs_channel = interaction.guild.get_channel(config.APPLICATION_LOGS_CHANNEL_ID)
        if bot_operator_role in interaction.user.roles:
            application_embed = interaction.message.embeds[0]
            self.accept_button.disabled = True
            self.reject_button.disabled = True

            self.reject_button.label = "Rejected"

            application_embed.set_footer(text="Application rejected!")
            await interaction.response.edit_message(embed=application_embed, view=self)
            await logs_channel.send(embed=discord.Embed(description="{} has rejected {}'s application.".format(interaction.user.mention, interaction.message.mentions[0].mention), color=config.TFC_GOLD, timestamp=datetime.datetime.now()))
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return