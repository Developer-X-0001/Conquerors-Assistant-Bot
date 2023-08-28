import config
import discord
import asyncio

from discord.ext import commands
from discord import app_commands

class UserContextMenu(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.promote_cmd = app_commands.ContextMenu(
            name="Promote",
            callback=self.promote
        )
        self.demote_cmd = app_commands.ContextMenu(
            name="Demote",
            callback=self.demote
        )
        self.bot.tree.add_command(self.promote_cmd)
        self.bot.tree.add_command(self.demote_cmd)

    async def promote(self, interaction: discord.Interaction, user: discord.Member):
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:
            if user.bot:
                await interaction.response.send_message(embed=discord.Embed(description="{} You can't promote a bot!".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return

            RANKS = config.RANKS
            RANK_LIST = config.RANK_LIST

            if user.nick:
                paygrade = user.nick[:2]

                current_rank_position = RANK_LIST.index(paygrade)
                next_rank_position = current_rank_position + 1

                if next_rank_position > 26:
                    await interaction.response.send_message(embed=discord.Embed(description="{} User is at the highest rank!".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                    return
                
                else:
                    await interaction.response.defer(ephemeral=True)
                    current_rank_role = interaction.guild.get_role(RANKS[paygrade]['role'])
                    current_clearance_role = interaction.guild.get_role(RANKS[paygrade]['clearance_role'])
                    current_rank = RANKS[paygrade]['name']

                    next_rank_role = interaction.guild.get_role(RANKS[RANK_LIST[next_rank_position]]['role'])
                    next_clearance_role = interaction.guild.get_role(RANKS[RANK_LIST[next_rank_position]]['clearance_role'])
                    next_paygrade = RANK_LIST[next_rank_position]
                    next_nick = RANKS[RANK_LIST[next_rank_position]]['nick']
                    next_rank = RANKS[RANK_LIST[next_rank_position]]['name']

                    callsign = user.nick.split(' | ')[1].split('. ')[1]

                    if current_rank_role in user.roles:
                        await user.remove_roles(current_rank_role)
                        await asyncio.sleep(1)
                        await user.add_roles(next_rank_role)
                    
                    if current_clearance_role != next_clearance_role:
                        await user.remove_roles(current_clearance_role)
                        await asyncio.sleep(1)
                        await user.add_roles(next_clearance_role)
                    
                    await user.edit(nick=f"{next_paygrade} | {next_nick}. {callsign}")
                    await interaction.followup.send(embed=discord.Embed(description=f"**{callsign}** has been promoted!\nPrevious Rank: {current_rank}\nCurrent Rank: {next_rank}", color=config.TFC_GOLD))
    
            else:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return

    async def demote(self, interaction: discord.Interaction, user: discord.Member):
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:
            if user.bot:
                await interaction.response.send_message(embed=discord.Embed(description="{} You can't demote a bot!".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return

            RANKS = config.RANKS
            RANK_LIST = config.RANK_LIST

            if user.nick:
                paygrade = user.nick[:2]
                if paygrade == 'N0':
                    paygrade = 'N1'
                
                if paygrade == 'M0':
                    paygrade = 'M1'

                current_rank_position = RANK_LIST.index(paygrade)
                print(current_rank_position)
                next_rank_position = current_rank_position - 1

                if next_rank_position < 0:
                    await interaction.response.send_message(embed=discord.Embed(description="{} User is at the lowest rank!".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                    return
                
                else:
                    await interaction.response.defer(ephemeral=True)
                    current_rank_role = interaction.guild.get_role(RANKS[paygrade]['role'])
                    current_clearance_role = interaction.guild.get_role(RANKS[paygrade]['clearance_role'])
                    current_rank = RANKS[paygrade]['name']

                    next_rank_role = interaction.guild.get_role(RANKS[RANK_LIST[next_rank_position]]['role'])
                    next_clearance_role = interaction.guild.get_role(RANKS[RANK_LIST[next_rank_position]]['clearance_role'])
                    next_paygrade = RANK_LIST[next_rank_position]
                    next_nick = RANKS[RANK_LIST[next_rank_position]]['nick']
                    next_rank = RANKS[RANK_LIST[next_rank_position]]['name']

                    callsign = user.nick.split(' | ')[1].split('. ')[1]

                    if current_rank_role in user.roles:
                        await user.remove_roles(current_rank_role)
                        await asyncio.sleep(1)
                        await user.add_roles(next_rank_role)
                    
                    if current_clearance_role != next_clearance_role:
                        await user.remove_roles(current_clearance_role)
                        await asyncio.sleep(1)
                        await user.add_roles(next_clearance_role)
                    
                    await user.edit(nick=f"{next_paygrade} | {next_nick}. {callsign}")
                    await interaction.followup.send(embed=discord.Embed(description=f"**{callsign}** has been demoted!\nPrevious Rank: {current_rank}\nCurrent Rank: {next_rank}", color=config.TFC_GOLD))
    
            else:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
        
async def setup(bot: commands.Bot):
    await bot.add_cog(UserContextMenu(bot))