import re
import config
import sqlite3
import discord
import datetime

from discord import TextStyle
from discord.ui import Modal, TextInput
from Interface.ApplicationButtons import ApplicationButtons

class ApplicationModal(Modal, title="Task Force Application Form"):
    def __init__(self, username: str):
        self.username = username
        self.database = sqlite3.connect("./Databases/data.sqlite")
        super().__init__(timeout=None)
    
        # self.question_one = TextInput(
        #     label="Your Roblox username?",
        #     style=TextStyle.short,
        #     placeholder="Type your roblox username not displayname...",
        #     required=True
        # )

        self.question_two = TextInput(
            label="Where did you join from?",
            style=TextStyle.short,
            placeholder="e.g PlatinumFive, Developer X#0001, etc",
            required=True
        )

        self.question_three = TextInput(
            label="Desired callsign?",
            style=TextStyle.short,
            placeholder="Type only one word no spaces...",
            required=True
        )

        self.question_four = TextInput(
            label="Most active time-zone?",
            style=TextStyle.short,
            placeholder="e.g GMT, EST, PST, etc",
            required=True
        )

        self.question_five = TextInput(
            label="What are your expectations from us?",
            style=TextStyle.long,
            placeholder="Write atleast 2-3 sentences...",
            required=True,
        )

        # self.add_item(self.question_one)
        self.add_item(self.question_two)
        self.add_item(self.question_three)
        self.add_item(self.question_four)
        self.add_item(self.question_five)

    async def on_submit(self, interaction: discord.Interaction):
        callsign_pattern = r'^[A-Z][a-zA-Z]*$'
        match = re.match(callsign_pattern, self.question_three.value)
        if not match:
            await interaction.response.send_message(embed=discord.Embed(description="{} Unable to process application!\n\n**Reason:** Invalid callsign format.".format(config.ERROR_EMOJI), color=discord.Color.red()).set_footer(text="Callsign must contains alphabets only! Spaces, numbers and symbols aren't allowed."), ephemeral=True)
            return
    
        data = self.database.execute("SELECT callsign FROM UserData WHERE callsign = ?", (self.question_three.value.capitalize(),)).fetchone()
        if data is not None:
            await interaction.response.send_message(content=f"{config.ERROR_EMOJI} Callsign **({self.question_three.value})** is already taken. Please apply again and choose other callsign.", ephemeral=True)
            return

        application_embed = discord.Embed(
            title="Task Force \"Conquerors\" Application",
            description="Thanks for applying for Task Force \"Conquerors\"! Please be patient, one of the HiCOM will review your application shortly.",
            color=config.TFC_GOLD,
            timestamp=datetime.datetime.now()
        )
        application_embed.add_field(
            name="**__Applicant Details:__**",
            value="**Username (ID):** {} ({})\n**Joined At:** <t:{joined_at}:D> (<t:{joined_at}:R>)\n**Created At:** <t:{created_at}:D> (<t:{created_at}:R>)".format(
                interaction.user.name, interaction.user.id, joined_at=round(interaction.user.joined_at.timestamp()), created_at=round(interaction.user.created_at.timestamp())
            ),
            inline=False
        )
        application_embed.add_field(
            name="{} Your Roblox username?".format(config.ARROW_EMOJI),
            value=f"> {self.username}",
            inline=False
        )
        application_embed.add_field(
            name="{} Where did you join from?".format(config.ARROW_EMOJI),
            value=f"> {self.question_two.value}",
            inline=False
        )
        application_embed.add_field(
            name="{} Desired callsign?".format(config.ARROW_EMOJI),
            value=f"> {self.question_three.value}",
            inline=False
        )
        application_embed.add_field(
            name="{} Most active time-zone?".format(config.ARROW_EMOJI),
            value=f"> {self.question_four.value}",
            inline=False
        )
        application_embed.add_field(
            name="{} What are your expectations from us?".format(config.ARROW_EMOJI),
            value=f"> {self.question_five.value}",
            inline=False
        )
        application_embed.set_thumbnail(url=config.TFC_ICON)

        application_channel = interaction.guild.get_channel(config.APPLICATION_CHANNEL_ID)

        msg = await application_channel.send(content=interaction.user.mention, embed=application_embed, view=ApplicationButtons())
        await interaction.response.send_message(content="Thanks for applying!\nYou can see your submitted application here: {}".format(msg.jump_url), ephemeral=True)