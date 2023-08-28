import config
import sqlite3
import discord
import requests
import datetime

from discord import TextStyle, ButtonStyle
from discord.ui import Modal, TextInput, View, Button, button
from Functions.DateCheck import isDateFormat, isFutureDate, formatDate, isPastDate
from Interface.ErrorReportView import ReportButtonView

class LOARequestModal(Modal, title="LOA Request Form"):
    def __init__(self):
        super().__init__(timeout=None)
    
    reason_of_loa = TextInput(
        label="Reason of LOA",
        placeholder="State why you are requesting LOA",
        style=TextStyle.long,
        required=True
    )
    start_time = TextInput(
        label="Start Time:",
        placeholder="Starting date of your LOA (MM/DD/YYYY)",
        style=TextStyle.short,
        default=datetime.datetime.now().strftime("%m/%d/%Y"),
        max_length=10,
        required=True
    )
    end_time = TextInput(
        label="End Time:",
        placeholder="End date of your LOA (MM/DD/YYYY)",
        style=TextStyle.short,
        max_length=10,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        if not isDateFormat(self.start_time.value):
            await interaction.response.send_message(embed=discord.Embed(description="❌ **Invalid Starting Date Format!**\nCorrect Format: `MM/DD/YYYY`", color=discord.Color.red()), ephemeral=True)
            return
        
        if not isDateFormat(self.end_time.value):
            await interaction.response.send_message(embed=discord.Embed(description="❌ **Invalid Ending Date Format!**\nCorrect Format: `MM/DD/YYYY`", color=discord.Color.red()), ephemeral=True)
            return
    
        if not isFutureDate(self.end_time.value):
            await interaction.response.send_message(embed=discord.Embed(description="❌ **Ending Date must be a date in future!**", color=discord.Color.red()), ephemeral=True)
            return
    
        if isPastDate(self.start_time.value):
            await interaction.response.send_message(embed=discord.Embed(description="❌ **Starting Date must be a date of today or in future!**", color=discord.Color.red()), ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True, thinking=True)

        headers = {
            "Authorization": f"Bearer {config.ROVER_API_KEY}"
        }
        response = requests.get(url="{}/guilds/{}/discord-to-roblox/{}".format(config.ROVER_API_ENDPOINT, interaction.guild.id, interaction.user.id), headers=headers)

        if response.status_code == 200:
            data = response.json()

            loa_embed = discord.Embed(
                title="LOA Request",
                color=config.TFC_GOLD
            )
            loa_embed.add_field(
                name="Discord User:",
                value=f"{interaction.user.name} ({interaction.user.id})",
                inline=False
            )
            loa_embed.add_field(
                name="Roblox User:",
                value=data['cachedUsername'],
                inline=False
            )
            loa_embed.add_field(
                name="Reason of LOA:",
                value=self.reason_of_loa.value,
                inline=False
            )
            loa_embed.add_field(
                name="Start Date:",
                value=formatDate(self.start_time.value),
                inline=False
            )
            loa_embed.add_field(
                name="End Date:",
                value=formatDate(self.end_time.value),
                inline=False
            )
            loa_embed.set_thumbnail(url=config.TFC_ICON)

            loa_requests_channel = interaction.guild.get_channel(config.LOA_REQUESTS_CHANNEL_ID)
            await loa_requests_channel.send(content=interaction.user.mention, embed=loa_embed, view=LOARequestView())
            await interaction.followup.send(embed=discord.Embed(description="{} Your LOA request has been sent.".format(config.DONE_EMOJI), color=config.TFC_GOLD), ephemeral=True)
        
        else:
            await interaction.followup.send(embed=discord.Embed(description="{} **Something went wrong!**\n\n**Error Code:** `{}`".format(config.ERROR_EMOJI, response.status_code), color=config.TFC_GOLD).set_footer(text="Please report the issue along side the error code."), view=ReportButtonView(), ephemeral=True)

class LOARequestView(View):
    def __init__(self):
        self.database = sqlite3.connect("./Databases/data.sqlite")
        super().__init__(timeout=None)
    
    @button(label="Accept", emoji=config.DONE_EMOJI, style=ButtonStyle.gray, custom_id="loa_accept_button")
    async def loa_accept_btn(self, interaction: discord.Interaction, button: Button):
        user = interaction.message.mentions[0]
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:

            if user == interaction.user:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You can't accept your own request!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
            
            loa_role = interaction.guild.get_role(config.LOA_ROLE_ID)
            logs_channel = interaction.guild.get_channel(config.LOA_LOGS_CHANNEL_ID)
            
            await user.add_roles(loa_role)

            loa_embed = interaction.message.embeds[0]
            loa_embed.set_footer(text="Request Accepted by {}".format(interaction.user.display_name))

            self.loa_accept_btn.disabled = True
            self.loa_accept_btn.label = "Accepted"
            self.loa_accept_btn.style = ButtonStyle.green

            self.loa_reject_btn.disabled = True

            reason = interaction.message.embeds[0].fields[2].value

            start_time = interaction.message.embeds[0].fields[3].value
            start_timestamp = round(datetime.datetime.strptime(start_time, '%m/%d/%Y').timestamp())

            end_time = interaction.message.embeds[0].fields[4].value
            end_timestamp = round(datetime.datetime.strptime(end_time, '%m/%d/%Y').timestamp())

            await logs_channel.send(embed=discord.Embed(description="{} has accepted {}'s LOA request.".format(interaction.user.mention, interaction.message.mentions[0].mention), color=config.TFC_GOLD, timestamp=datetime.datetime.now()))
            self.database.execute("INSERT INTO UserLOAs VALUES (?, ?, ?, ?, ?)", (user.id, reason, start_timestamp, end_timestamp, interaction.user.id,)).connection.commit()
            await interaction.response.edit_message(embed=loa_embed, view=self)
        
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return
        
    @button(label="Reject", emoji=config.ERROR_EMOJI, style=ButtonStyle.gray, custom_id="loa_reject_button")
    async def loa_reject_btn(self, interaction: discord.Interaction, button: Button):
        user = interaction.message.mentions[0]
        bot_operator_role = interaction.guild.get_role(config.BOT_OPERATOR_ROLE_ID)
        if bot_operator_role in interaction.user.roles:

            if user == interaction.user:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You can't accept your own request!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
            
            loa_embed = interaction.message.embeds[0]
            logs_channel = interaction.guild.get_channel(config.LOA_LOGS_CHANNEL_ID)
            loa_embed.set_footer(text="Request Rejected by {}".format(interaction.user.display_name))

            self.loa_accept_btn.disabled = True
            
            self.loa_reject_btn.disabled = True
            self.loa_reject_btn.label = "Rejected"
            self.loa_reject_btn.style = ButtonStyle.red

            await logs_channel.send(embed=discord.Embed(description="{} has rejected {}'s LOA request.".format(interaction.user.mention, interaction.message.mentions[0].mention), color=config.TFC_GOLD, timestamp=datetime.datetime.now()))
            await interaction.response.edit_message(embed=loa_embed, view=self)
        
        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return