import config
import discord

from discord.ext import commands
from discord import app_commands
from Interface.QuestionsView import QuestionModal

class Questions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="ask-question", description="Ask a question")
    async def ask_question(self, interaction: discord.Interaction):
        bot_commands_channel = interaction.guild.get_channel(config.BOT_COMMANDS_CHANNEL_ID)
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if interaction.channel == bot_commands_channel or bot_operator_role in interaction.user.roles:
            await interaction.response.send_modal(QuestionModal())
            return
        
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} You can't use commands in this channel. Please go in {}".format(config.ERROR_EMOJI, bot_commands_channel.mention), color=config.TFC_GOLD), ephemeral=True)
            return

async def setup(bot: commands.Bot):
    await bot.add_cog(Questions(bot))