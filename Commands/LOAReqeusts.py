import config
import sqlite3
import discord

from discord.ext import commands
from discord import app_commands
from Functions.Webhooks import sql_update, sql_update_confirm
from Interface.LOARequestView import LOARequestModal

class LOARequest(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = sqlite3.connect("./Databases/data.sqlite")

    @app_commands.command(name="request-loa", description="Submit LOA (Leave of Absence) request.")
    async def request_loa(self, interaction: discord.Interaction):
        bot_commands_channel = interaction.guild.get_channel(config.BOT_COMMANDS_CHANNEL_ID)
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if interaction.channel == bot_commands_channel or bot_operator_role in interaction.user.roles:
            loa_role = interaction.guild.get_role(config.LOA_ROLE_ID)
            if loa_role in interaction.user.roles:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You are on LOA already!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
            
            await interaction.response.send_modal(LOARequestModal())
        
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} You can't use commands in this channel. Please go in {}".format(config.ERROR_EMOJI, bot_commands_channel.mention), color=config.TFC_GOLD), ephemeral=True)
            return
    
    @app_commands.command(name="return-loa", description="Return back from LOA (Leave of Absence).")
    async def return_loa(self, interaction: discord.Interaction):
        bot_commands_channel = interaction.guild.get_channel(config.BOT_COMMANDS_CHANNEL_ID)
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if interaction.channel == bot_commands_channel or bot_operator_role in interaction.user.roles:
            loa_role = interaction.guild.get_role(config.LOA_ROLE_ID)
            if loa_role in interaction.user.roles:
                await interaction.response.defer(ephemeral=True)
                on_topic_channel = interaction.guild.get_channel(config.ON_TOPIC_CHANNEL_ID)
                await interaction.user.remove_roles(loa_role)
                await on_topic_channel.send(content=interaction.user.mention, embed=discord.Embed(description="Welcome back! Your return is a delight. We're eager to resume teamwork and make progress together. If you need to catch up or share updates, feel free to connect. Here's to a productive time ahead!", color=config.TFC_GOLD).set_image(url=config.TFC_BANNER))
                await sql_update(
                    reason="User returned LOA",
                    code="DELETE FROM UserLOAs WHERE user_id = ?",
                    queries=[("user_id", interaction.user.id)],
                    color_code=0
                )
                self.database.execute("DELETE FROM UserLOAs WHERE user_id = ?", (interaction.user.id,)).connection.commit()
                await sql_update_confirm()
                await interaction.followup.send(embed=discord.Embed(description="{} Your LOA has been returned.".format(config.DONE_EMOJI), color=config.TFC_GOLD))
                return
            
            else:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't on LOA!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
        
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} You can't use commands in this channel. Please go in {}".format(config.ERROR_EMOJI, bot_commands_channel.mention), color=config.TFC_GOLD), ephemeral=True)
            return

async def setup(bot: commands.Bot):
    await bot.add_cog(LOARequest(bot))