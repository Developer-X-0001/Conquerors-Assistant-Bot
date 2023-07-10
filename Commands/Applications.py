import re
import config
import discord
import requests

from discord.ext import commands
from discord import app_commands
from Interface.ApplicationModal import ApplicationModal
from Interface.ErrorReportView import ReportButtonView

class Application(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="apply", description="Apply to become a personnel in Task Force 'Conquerors'")
    @app_commands.checks.has_role(config.VERIFIED_ROLE_ID)
    async def apply(self, interaction: discord.Interaction):
        headers = {
            "Authorization": f"Bearer {config.ROVER_API_KEY}"
        }
        response = requests.get(url="{}/guilds/{}/discord-to-roblox/{}".format(config.ROVER_API_ENDPOINT, interaction.guild.id, interaction.user.id), headers=headers)

        if response.status_code == 200:
            data = response.json()
            await interaction.response.send_modal(ApplicationModal(username=data['cachedUsername']))
            
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **Something went wrong!**\n\n**Error Code:** `{}`".format(config.ERROR_EMOJI, response.status_code), color=discord.Color.red()).set_footer(text="Please report the issue along side the error code."), view=ReportButtonView(), ephemeral=True)
    
    @apply.error
    async def apply_error(self, interaction: discord.Interaction, error: app_commands.errors):
        if isinstance(error, app_commands.errors.MissingRole):
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
        else:
            raise Exception

async def setup(bot: commands.Bot):
    await bot.add_cog(Application(bot))