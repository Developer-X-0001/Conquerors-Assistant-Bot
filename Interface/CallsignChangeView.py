import re
import config
import sqlite3
import discord
import datetime

from discord import TextStyle, ButtonStyle
from discord.ui import Modal, TextInput, View, Button, button
from Interface.ErrorReportView import ReportButtonView

database = sqlite3.connect("./Databases/data.sqlite")

class CallsignChangeModal(Modal, title="Callsign Update Form"):
    def __init__(self):
        super().__init__(timeout=None)

    reason_of_update = TextInput(
        label="Reason of Callsign Update",
        placeholder="State why you are requesting a callsign update...",
        style=TextStyle.long,
        required=True
    )

    new_callsign = TextInput(
        label="New Callsign",
        placeholder="Type your new callsign...",
        style=TextStyle.short,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        callsign_pattern = r'^[A-Z][a-zA-Z]*$'
        match = re.match(callsign_pattern, self.new_callsign.value)
        if not match:
            await interaction.response.send_message(embed=discord.Embed(description="{} Unable to process application!\n\n**Reason:** Invalid callsign format.".format(config.ERROR_EMOJI), color=discord.Color.red()).set_footer(text="Callsign must contains alphabets only! Spaces, numbers and symbols aren't allowed."), ephemeral=True)
            return
        
        callsign_data = database.execute("SELECT callsign FROM UserData WHERE callsign = ?", (self.new_callsign.value,)).fetchone()
        if callsign_data is not None:
            await interaction.response.send_message(content=f"{config.ERROR_EMOJI} Callsign **({self.new_callsign.value})** is already taken. Please apply again and choose other callsign.", ephemeral=True)
            return
        
        await interaction.response.defer(ephemeral=True, thinking=True)
        data = database.execute("SELECT callsign FROM UserData WHERE user_id = ?", (interaction.user.id,)).fetchone()
        old_callsign = data[0]

        callsign_requests_channel = interaction.guild.get_channel(config.CALLSIGN_REQUESTS_CHANNEL_ID)
        request_embed = discord.Embed(
            title="Callsign Update Request",
            color=config.TFC_GOLD
        ).add_field(
            name="Discord User:",
            value=f"{interaction.user.name} ({interaction.user.id})",
            inline=False
        ).add_field(
            name="Reason of Request:",
            value=self.reason_of_update.value,
            inline=False
        ).add_field(
            name="Old Callsign",
            value=data[0],
            inline=False
        ).add_field(
            name="New Callsign",
            value=self.new_callsign.value,
            inline=False
        )

        database.execute("INSERT INTO CallsignRequests VALUES (?, ?, ?, ?)", (interaction.user.id, self.reason_of_update.value, old_callsign, self.new_callsign.value,)).connection.commit()
        await callsign_requests_channel.send(content=interaction.user.mention, embed=request_embed, view=CallsignUpdateView())
        await interaction.followup.send(embed=discord.Embed(description="{} Your callsign update request has been sent.".format(config.DONE_EMOJI), color=config.TFC_GOLD), ephemeral=True)

class CallsignUpdateView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Accept", style=ButtonStyle.gray, custom_id="callsign_accept")
    async def callsign_accept_btn(self, interaction: discord.Interaction, button: Button):
        user = interaction.message.mentions[0]
        callsign_embed = interaction.message.embeds[0]
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:

            if user == interaction.user:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You can't manage your own request!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
            
            request_data = database.execute("SELECT old_callsign, new_callsign FROM CallsignRequests WHERE user_id = ?", (user.id,)).fetchone()
            if request_data is None:
                await interaction.response.send_message(embed=discord.Embed(description="{} {} has decided to cancel this request.".format(config.ERROR_EMOJI, user.mention), color=config.TFC_GOLD), ephemeral=True)
                callsign_embed.set_footer(text="Request Cancelled")
                await interaction.message.edit(embed=callsign_embed, view=None)
                return

            old_callsign = request_data[0]
            new_callsign = request_data[1]

            user_data = database.execute("SELECT name, rank FROM UserData WHERE user_id = ?", (user.id,)).fetchone()
            name = user_data[0] if user_data[0] else None
            rank = user_data[1]

            rank_nick = config.RANKS[rank]["nick"]
            update_nickname = f"{rank} | {rank_nick}. \"{new_callsign}\" "+ ("" if name is None else name)

            await user.edit(nick=update_nickname)
            
            logs_channel = interaction.guild.get_channel(config.CALLSIGN_LOGS_CHANNEL_ID)
            callsign_embed.set_footer(text="Request Accepted by {}".format(interaction.user.display_name))

            self.callsign_accept_btn.disabled = True
            self.callsign_accept_btn.label = "Accepted"
            self.callsign_accept_btn.style = ButtonStyle.green

            self.callsign_reject_btn.disabled = True

            database.execute("DELETE FROM CallsignRequests WHERE user_id = ?", (user.id,)).connection.commit()
            database.execute("INSERT INTO UserData (user_id, callsign) VALUES (?, ?) ON CONFLICT (user_id) DO UPDATE SET callsign = ? WHERE user_id = ?", (user.id, new_callsign, new_callsign, user.id,)).connection.commit()

            await logs_channel.send(embed=discord.Embed(description="{} has accepted {}'s callsign update request.".format(interaction.user.mention, interaction.message.mentions[0].mention), color=config.TFC_GOLD, timestamp=datetime.datetime.now()).add_field(name="Old Callsign:", value=old_callsign, inline=True).add_field(name="New Callsign:", value=new_callsign, inline=True))
            await interaction.response.edit_message(embed=callsign_embed, view=self)

    
    @button(label="Reject", style=ButtonStyle.gray, custom_id="callsign_reject")
    async def callsign_reject_btn(self, interaction: discord.Interaction, button: Button):
        user = interaction.message.mentions[0]
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:

            if user == interaction.user:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You can't manage your own request!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
            
            callsign_embed = interaction.message.embeds[0]
            logs_channel = interaction.guild.get_channel(config.CALLSIGN_LOGS_CHANNEL_ID)
            callsign_embed.set_footer(text="Request Rejected by {}".format(interaction.user.display_name))

            self.callsign_accept_btn.disabled = True
                
            self.callsign_reject_btn.disabled = True
            self.callsign_reject_btn.label = "Rejected"
            self.callsign_reject_btn.style = ButtonStyle.red

            database.execute("DELETE FROM CallsignRequests WHERE user_id = ?", (user.id,)).connection.commit()

            await logs_channel.send(embed=discord.Embed(description="{} has rejected {}'s callsign update request.".format(interaction.user.mention, interaction.message.mentions[0].mention), color=config.TFC_GOLD, timestamp=datetime.datetime.now()))
            await interaction.response.edit_message(embed=callsign_embed, view=self)

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return

class CallsignReturnView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Return Request", style=ButtonStyle.red)
    async def callsign_return_btn(self, interaction: discord.Interaction, button: Button):
        database.execute("DELETE FROM CallsignRequests WHERE user_id = ?", (interaction.user.id,)).connection.commit()
        self.callsign_return_btn.label = "Request Returned"
        self.callsign_return_btn.disabled = True

        await interaction.response.edit_message(view=self)
