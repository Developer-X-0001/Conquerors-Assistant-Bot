import config
import asyncio
import discord
import requests

from discord import ButtonStyle
from discord.ui import View, Button, button
from Interface.ApplicationModal import ApplicationModal
from Interface.ErrorReportView import ReportButtonView

class InformationView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="If you are a visitor, click on \"I'm a Visitor\" button. Otherwise \"Apply\"", disabled=True, custom_id='info_btn_disabled', row=0)
    async def info_btn(self, interaction: discord.Interaction, button: Button):
        pass

    @button(label="Apply", style=ButtonStyle.green, custom_id="information_apply_button", row=1)
    async def apply(self, interaction: discord.Interaction, button: Button):
        verified_role = interaction.guild.get_role(config.VERIFIED_ROLE_ID)

        if verified_role in interaction.user.roles:
            headers = {
                "Authorization": f"Bearer {config.ROVER_API_KEY}"
            }
            response = requests.get(url="{}/guilds/{}/discord-to-roblox/{}".format(config.ROVER_API_ENDPOINT, interaction.guild.id, interaction.user.id), headers=headers)

            if response.status_code == 200:
                data = response.json()
                await interaction.response.send_modal(ApplicationModal(username=data['cachedUsername']))
                
            else:
                await interaction.response.send_message(embed=discord.Embed(description="{} **Something went wrong!**\n\n**Error Code:** `{}`".format(config.ERROR_EMOJI, response.status_code), color=discord.Color.red()).set_footer(text="Please report the issue along side the error code."), view=ReportButtonView(), ephemeral=True)

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)

    @button(label="I'm a Visitor", style=ButtonStyle.gray, custom_id="information_visitor_button", row=1)
    async def visitor(self, interaction: discord.Interaction, button: Button):
        verified_role = interaction.guild.get_role(config.VERIFIED_ROLE_ID)
        
        if verified_role in interaction.user.roles:
            visitor_role = interaction.guild.get_role(config.VISITOR_ROLE_ID)

            await interaction.response.defer()
            await interaction.user.add_roles(visitor_role)
            await asyncio.sleep(1)
            await interaction.user.remove_roles(verified_role)

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
