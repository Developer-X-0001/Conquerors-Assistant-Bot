import time
import config
import discord
import datetime

from discord.ext import commands
from discord import app_commands

startTime = time.time()

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="info", description="Shows information about Conquerors Assistant.")
    async def _info(self, interaction: discord.Interaction):
        info_embed = discord.Embed(
            title="Conquerors Assistant#9376 Info",
            color=config.TFC_GOLD
        )
        info_embed.add_field(
            name="Developers",
            value=self.bot.application.owner.mention,
            inline=True
        )
        info_embed.add_field(
            name="Testers",
            value="None",
            inline=True
        )
        info_embed.add_field(
            name="Bug Hunters",
            value="None",
            inline=True
        )
        info_embed.add_field(
            name="Graphics Provider",
            value="[FlatIcon](https://www.flaticon.com/)",
            inline=True
        )
        info_embed.add_field(
            name="Graphics Editors",
            value=self.bot.application.owner.mention,
            inline=True
        )
        info_embed.add_field(
            name="Graphics License",
            value="[Free for personal and commercial use with attribution.](https://www.flaticon.com/license/icon/190411)",
            inline=False
        )
        info_embed.add_field(
            name="Uptime",
            value=str(datetime.timedelta(seconds=int(round(time.time()-startTime)))),
            inline=True
        )
        info_embed.add_field(
            name="Latency",
            value=f"{round(self.bot.latency * 1000)} ms",
            inline=True
        )
        info_embed.add_field(
            name="Language",
            value="EN-US",
            inline=True
        )
        info_embed.add_field(
            name="Version",
            value=config.VERSION,
            inline=True
        )
        info_embed.add_field(
            name="Host",
            value="Oracle Cloud VPS",
            inline=True
        )
        info_embed.set_thumbnail(url=config.TFC_ICON)
        info_embed.set_image(url=config.TFC_BANNER)
        info_embed.set_footer(text="Conquerors Assistant is an authorized property of TFC.")

        await interaction.response.send_message(embed=info_embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))