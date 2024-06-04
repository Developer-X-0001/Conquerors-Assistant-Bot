import re
import config
import sqlite3
import discord

from discord.ext import commands
from discord import app_commands

class Points(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = sqlite3.connect("./Databases/data.sqlite")
    
    points_group = app_commands.Group(name="points", description="Commands related to points system.")

    @points_group.command(name="add", description="Add points to the mentioned users.")
    @app_commands.choices(hidden=[
        app_commands.Choice(name="True", value=0),
        app_commands.Choice(name="False", value=1)
    ])
    @app_commands.describe(
        amount="Amount of points to add",
        users="List of users to add points to"
    )
    @app_commands.checks.has_role(config.POINTS_DISTRIBUTOR_ROLE_ID)
    async def add_points(self, interaction: discord.Interaction, amount: int, users: str, hidden: app_commands.Choice[int]=None):
        if amount < 0:
            await interaction.response.send_message(embed=discord.Embed(description="{} **Amount can't be lower than or equal to zero!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
        
        if users:
            ephemeral = True if hidden is None or hidden.value == 0 else False
            pattern = r'<@(\d+)>'
            matches = re.findall(pattern, users)
            data = ""
            counter = 1
            await interaction.response.send_message(embed=discord.Embed(description="{} Adding points to {} users.".format(config.LOAD_EMOJI, len(matches)), color=config.TFC_GOLD), ephemeral=ephemeral)
            for match in matches:
                user = interaction.guild.get_member(int(match))
                if user:
                    self.database.execute("INSERT INTO UserData (user_id, points) VALUES (?, ?) ON CONFLICT (user_id) DO UPDATE SET points = points + ? WHERE user_id = ?", (user.id, amount, amount, user.id,)).connection.commit()
                    data += "{}. {}\n".format(counter, user.mention)
                    counter += 1
                
            await interaction.edit_original_response(embed=discord.Embed(description="**Added `{}` points to the following users:**\n{}".format(amount, data), color=config.TFC_GOLD))

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **Please mention atleast one user!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
        
    @add_points.error
    async def add_points_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.MissingRole):
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
    
    @points_group.command(name="remove", description="Remove points from the mentioned users.")
    @app_commands.choices(hidden=[
        app_commands.Choice(name="True", value=0),
        app_commands.Choice(name="False", value=1)
    ])
    @app_commands.describe(
        amount="Amount of points to remove",
        users="List of users to remove points from"
    )
    @app_commands.checks.has_role(config.POINTS_DISTRIBUTOR_ROLE_ID)
    async def remove_points(self, interaction: discord.Interaction, amount: int, users: str, hidden: app_commands.Choice[int]=None):
        if amount < 0:
            await interaction.response.send_message(embed=discord.Embed(description="{} **Amount can't be lower than or equal to zero!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
        
        if users:
            ephemeral = True if hidden is None or hidden.value == 0 else False
            pattern = r'<@(\d+)>'
            matches = re.findall(pattern, users)
            data = ""
            counter = 1
            await interaction.response.send_message(embed=discord.Embed(description="{} Removing points from {} users.".format(config.LOAD_EMOJI, len(matches)), color=config.TFC_GOLD), ephemeral=ephemeral)
            for match in matches:
                user = interaction.guild.get_member(int(match))
                if user:
                    current_points_data = self.database.execute("SELECT points FROM UserData WHERE user_id = ?", (user.id,)).fetchone()
                    if current_points_data is None:
                        current_points = 0
                    else:
                        current_points = int(current_points_data[0])

                    if (current_points - amount) < 0:
                        updated_amount = 0
                    else:
                        updated_amount = current_points - amount

                    self.database.execute("INSERT INTO UserData (user_id, points) VALUES (?, ?) ON CONFLICT (user_id) DO UPDATE SET points = ? WHERE user_id = ?", (user.id, 0, updated_amount, user.id,)).connection.commit()
                    data += "{}. {}\n".format(counter, user.mention)
                    counter += 1
                
                await interaction.edit_original_response(embed=discord.Embed(description="**Removed `{}` points from the following users:**\n{}".format(amount, data), color=config.TFC_GOLD))

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **Please mention atleast one user!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
        
    @add_points.error
    async def remove_points_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.MissingRole):
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
    
    @points_group.command(name="check", description="Check yours or someone else's points.")
    @app_commands.choices(hidden=[
        app_commands.Choice(name="True", value=0),
        app_commands.Choice(name="False", value=1)
    ])
    @app_commands.describe(
        user="User whose points you want to check"
    )
    async def check_points(self, interaction: discord.Interaction, user: discord.Member=None, hidden: app_commands.Choice[int]=None):
        ephemeral = True if hidden is None or hidden.value == 0 else False
        bot_commands_channel = interaction.guild.get_channel(config.BOT_COMMANDS_CHANNEL_ID)
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if interaction.channel == bot_commands_channel or bot_operator_role in interaction.user.roles:
            if user is None:
                user = interaction.user
            
            possesive_pronoun = "You" if user is None or user == interaction.user else user.display_name

            data = self.database.execute("SELECT points FROM UserData WHERE user_id = ?", (user.id,)).fetchone()
            if data is None:
                self.database.execute("INSERT INTO UserData (user_id, points) VALUES (?, ?)", (user.id, 0,)).connection.commit()
                points = 0
            else:
                points = int(data[0])

            await interaction.response.send_message(embed=discord.Embed(description="{} have {} {} points.".format(possesive_pronoun, config.POINTS_EMOJI, points), color=config.TFC_GOLD), ephemeral=ephemeral)

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} You can't use commands in this channel. Please go in {}".format(config.ERROR_EMOJI, bot_commands_channel.mention), color=config.TFC_GOLD), ephemeral=True)
            return

    @points_group.command(name="leaderboard", description="Check points leaderboard")
    @app_commands.choices(hidden=[
        app_commands.Choice(name="True", value=0),
        app_commands.Choice(name="False", value=1)
    ])
    async def leaderboard(self, interaction: discord.Interaction, hidden: app_commands.Choice[int]=None):
        ephemeral = True if hidden is None or hidden.value == 0 else False
        bot_commands_channel = interaction.guild.get_channel(config.BOT_COMMANDS_CHANNEL_ID)
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if interaction.channel == bot_commands_channel or bot_operator_role in interaction.user.roles:
            data = self.database.execute("SELECT user_id, points FROM UserData ORDER BY points DESC").fetchall()
            if data is None or data == []:
                await interaction.response.send_message(embed=discord.Embed(description="{} No leaderboard data found.".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=ephemeral)
                return
            
            await interaction.response.send_message(embed=discord.Embed(description="{} Fetching leaderboard data...".format(config.LOAD_EMOJI), color=config.TFC_GOLD), ephemeral=ephemeral)
            formatted_data = ""
            counter = 1
            for entry in data:
                user = interaction.guild.get_member(int(entry[0]))
                if user:
                    formatted_data += "{}. {} | {} {}\n".format(counter, user.display_name, config.POINTS_EMOJI, entry[1])
                    counter += 1
                    if counter == 11:
                        break
            
            await interaction.edit_original_response(embed=discord.Embed(title="TFC Points Leaderboard", description=formatted_data, color=config.TFC_GOLD))
        
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} You can't use commands in this channel. Please go in {}".format(config.ERROR_EMOJI, bot_commands_channel.mention), color=config.TFC_GOLD), ephemeral=True)
            return

async def setup(bot: commands.Bot):
    await bot.add_cog(Points(bot))