import config
import discord
import sqlite3
import asyncio
import requests

from discord.ui import Select, Modal, TextInput, View, Button, button
from discord import ButtonStyle, TextStyle
from config import RANKS, RANK_LIST

database = sqlite3.connect("./Databases/data.sqlite")

class PromotionRequestView(View):
    def __init__(self, user: discord.Member):
        super().__init__(timeout=None)
        self.add_item(PromotionSelectMenu(user))
    
class PromotionSelectMenu(Select):
    def __init__(self, user: discord.Member):
        options = []

        current_rank = user.nick[:2]
        available_ranks = []
        if current_rank.startswith('E'):
            available_ranks = RANK_LIST[RANK_LIST.index(current_rank)+1:5]

        if current_rank.startswith('N'):
            available_ranks = RANK_LIST[RANK_LIST.index(current_rank)+1:10]

        if current_rank.startswith('M'):
            available_ranks = RANK_LIST[RANK_LIST.index(current_rank)+1:14]

        if current_rank.startswith('W'):
            available_ranks = RANK_LIST[RANK_LIST.index(current_rank)+1:19]
        
        if current_rank.startswith('O'):
            available_ranks = RANK_LIST[RANK_LIST.index(current_rank)+1:26]

        for rank in available_ranks:
            requirement = f"{RANKS[rank]['points']} Points"
            
            options.append(
                discord.SelectOption(label=RANKS[rank]['name'], emoji=None if not RANKS[rank]['emoji'] else RANKS[rank]['emoji'], description=requirement, value=rank)
            )

        super().__init__(
            placeholder="Choose the rank that you want to request for",
            min_values=1,
            max_values=1,
            options=options
        )
    
    async def callback(self, interaction: discord.Interaction):
        request_data = database.execute("SELECT user_id FROM PromotionRequests WHERE user_id = ?", (interaction.user.id,)).fetchone()
        if request_data != None:
            promotion_requests_channel = interaction.guild.get_channel(config.PROMOTION_REQUESTS_CHANNEL_ID)
            await interaction.response.edit_message(embed=discord.Embed(description="{} **You already have an open request in {}**".format(config.WARN_EMOJI, promotion_requests_channel.mention), color=config.TFC_GOLD), view=PromotionReturnView())
            return

        headers = {
            "Authorization": f"Bearer {config.ROVER_API_KEY}"
        }
        response = requests.get(url="{}/guilds/{}/discord-to-roblox/{}".format(config.ROVER_API_ENDPOINT, interaction.guild.id, interaction.user.id), headers=headers)

        if response.status_code == 200:
            data = response.json()
            current_paygrade = interaction.user.nick[:2]
            current_rank = RANKS[current_paygrade]['name']

            requesting_paygrade = self.values[0]
            requesting_rank = RANKS[requesting_paygrade]['name']

            user_data = database.execute("SELECT points FROM UserData WHERE user_id = ?", (interaction.user.id,)).fetchone()
            if user_data is None:
                user_points = 0
            
            else:
                user_points = int(user_data[0])

            embed = discord.Embed(
                title="Promotion Request",
                color=config.TFC_GOLD
            )
            embed.add_field(
                name="Discord User:",
                value=f"{interaction.user.name} ({interaction.user.id})",
                inline=False
            )
            embed.add_field(
                name="Roblox User:",
                value=data['cachedUsername'],
                inline=False
            )
            embed.add_field(
                name="Current Rank:",
                value=f"{current_paygrade} | {current_rank}",
                inline=False
            )
            embed.add_field(
                name="Requesting Rank:",
                value=f"{requesting_paygrade} | {requesting_rank}",
                inline=False
            )
            embed.add_field(
                name="Total Points:",
                value=user_points,
                inline=False
            )

            await interaction.response.edit_message(embed=embed, view=PromotionRequestConfirmView())

class PromotionReturnView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Return Request", style=ButtonStyle.red)
    async def return_req_btn(self, interaction: discord.Interaction, button: Button):
        database.execute("DELETE FROM PromotionRequests WHERE user_id = ?", (interaction.user.id,)).connection.commit()
        await interaction.response.edit_message(embed=discord.Embed(description=f"{config.DONE_EMOJI} Your promotion request has been removed.", color=config.TFC_GOLD))
        return

class PromotionRequestConfirmView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Send", emoji=config.DONE_EMOJI, style=ButtonStyle.gray)
    async def promotion_request_send_button(self, interaction: discord.Interaction, button: Button):
        promotion_requests_channel = interaction.guild.get_channel(config.PROMOTION_REQUESTS_CHANNEL_ID)
        embed = interaction.message.embeds[0]

        current_rank = embed.fields[2].value[:2]
        requesting_rank = embed.fields[3].value[:2]

        database.execute("INSERT INTO PromotionRequests VALUES (?, ?, ?)", (interaction.user.id, current_rank, requesting_rank,)).connection.commit()

        await promotion_requests_channel.send(content=interaction.user.mention, embed=interaction.message.embeds[0], view=PromotionRequestManage())
        await interaction.response.edit_message(embed=discord.Embed(description="{} Your promotion request has been forwarded to {}.".format(config.DONE_EMOJI, promotion_requests_channel.mention), color=config.TFC_GOLD), view=None)
    
    @button(label="Cancel", emoji=config.ERROR_EMOJI, style=ButtonStyle.gray)
    async def promotion_request_cancel_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(embed=discord.Embed(description="{} **Request Cancelled!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), view=None)
    
class PromotionRequestManage(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Approve", emoji=config.DONE_EMOJI, style=ButtonStyle.gray, custom_id="promotion_accept_button")
    async def promotion_accept_btn(self, interaction: discord.Interaction, button: Button):
        user = interaction.message.mentions[0]
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:

            if user == interaction.user:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You can't accept your own request!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return

            RANKS = config.RANKS
            RANK_LIST = config.RANK_LIST

            data = database.execute("SELECT callsign, name, rank FROM UserData WHERE user_id = ?", (user.id,)).fetchone()
            callsign = data[0]
            name = data[1] if data[1] else None
            rank = data[2]

            if user.nick:
                embed = interaction.message.embeds[0]
                current_paygrade = embed.fields[2].value[:2]
                requesting_paygrade = embed.fields[3].value[:2]

                next_rank_position = RANK_LIST.index(requesting_paygrade)

                if next_rank_position > 14:
                    await interaction.response.send_message(embed=discord.Embed(description="{} User is at the highest rank!".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                    return
                
                else:
                    self.promotion_accept_btn.label = "Please Wait"
                    self.promotion_accept_btn.emoji = config.LOAD_EMOJI
                    self.promotion_accept_btn.disabled = True
                    self.promotion_reject_btn.disabled = True
                    await interaction.response.edit_message(view=self)
                    
                    current_rank_role = interaction.guild.get_role(RANKS[current_paygrade]['role'])
                    current_clearance_role = interaction.guild.get_role(RANKS[current_paygrade]['clearance_role'])

                    next_rank_role = interaction.guild.get_role(RANKS[RANK_LIST[next_rank_position]]['role'])
                    next_clearance_role = interaction.guild.get_role(RANKS[RANK_LIST[next_rank_position]]['clearance_role'])
                    next_paygrade = RANK_LIST[next_rank_position]
                    next_nick = RANKS[RANK_LIST[next_rank_position]]['nick']

                    next_rank_emoji = RANKS[RANK_LIST[next_rank_position]]['emoji']
                    next_rank_name = RANKS[RANK_LIST[next_rank_position]]['name']

                    if current_rank_role in user.roles:
                        await user.remove_roles(current_rank_role)
                        await asyncio.sleep(1)
                        await user.add_roles(next_rank_role)
                    
                    if current_clearance_role != next_clearance_role:
                        await user.remove_roles(current_clearance_role)
                        await asyncio.sleep(1)
                        await user.add_roles(next_clearance_role)
                    
                    if name is None:
                        await user.edit(nick=f"{next_paygrade} | {next_nick}. {callsign}")
                    else:
                        await user.edit(nick=f"{next_paygrade} | {next_nick}. \"{callsign}\" {name}")

                    database.execute("UPDATE UserData SET rank = ? WHERE user_id = ?", (next_paygrade, user.id,)).connection.commit()

                    self.promotion_accept_btn.disabled = True
                    self.promotion_accept_btn.label = "Accepted"
                    self.promotion_accept_btn.emoji = config.DONE_EMOJI
                    self.promotion_accept_btn.style = ButtonStyle.green

                    self.promotion_reject_btn.disabled = True
                    promotion_logs_channel = interaction.guild.get_channel(config.PROMOTION_LOGS_CHANNEL_ID)
                    database.execute("DELETE FROM PromotionRequests WHERE user_id = ?", (user.id,)).connection.commit()
                    embed.set_footer(text=f"Request Accepted by {interaction.user.nick}")
                    await promotion_logs_channel.send(embed=discord.Embed(description="{} has accepted {}'s promotion request.".format(interaction.user.mention, user.mention), color=config.TFC_GOLD))
                    await interaction.message.edit(embed=embed, view=self)

                    try:
                        dm_embed = discord.Embed(
                            title="Promotion Request Decision",
                            description="Your request has been reviewed by our board and been approved by {}\nCongratulations for reaching {} **{}**".format(interaction.user.mention, next_rank_emoji, next_rank_name),
                            color=config.TFC_GOLD
                        )
                        await user.send(embed=dm_embed)

                    except:
                        pass


        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return

    @button(label="Reject", emoji=config.ERROR_EMOJI, style=ButtonStyle.gray, custom_id="promotion_reject_button")
    async def promotion_reject_btn(self, interaction: discord.Interaction, button: Button):
        user = interaction.message.mentions[0]
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:

            if user == interaction.user:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You can't reject your own request!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
            
            await interaction.response.send_modal(RequestRejectModal(orignal_view=self))

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return

class RequestRejectModal(Modal, title="Request Reject Modal"):
    def __init__(self, orignal_view: PromotionRequestManage):
        self.view = orignal_view
        super().__init__(timeout=None)

    rejection_reason = TextInput(
        label="Reason:",
        placeholder="Why you rejected this request?",
        style=TextStyle.long,
        required=True
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        promotion_logs_channel = interaction.guild.get_channel(config.PROMOTION_LOGS_CHANNEL_ID)
        user = interaction.message.mentions[0]

        embed = interaction.message.embeds[0]
        embed.set_footer(text=f"Request Rejected by {interaction.user.nick}")

        self.view.promotion_accept_btn.disabled = True

        self.view.promotion_reject_btn.disabled = True
        self.view.promotion_reject_btn.label = "Rejected"
        self.view.promotion_reject_btn.style = ButtonStyle.red

        await promotion_logs_channel.send(embed=discord.Embed(description="{} has rejected {}'s promotion request.".format(interaction.user.mention, user.mention), color=config.TFC_GOLD))
        database.execute("DELETE FROM PromotionRequests WHERE user_id = ?", (user.id,)).connection.commit()
        await interaction.response.edit_message(embed=embed, view=self.view)

        try:
            dm_embed = discord.Embed(
                title="Promotion Request Decision",
                description="Your request has been reviewed by our board and been declined for the following reason:\n```{}```\nTry again next time".format(self.rejection_reason.value),
                color=config.TFC_GOLD
            )
            await user.send(embed=dm_embed)

        except:
            pass
