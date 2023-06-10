import config
import discord
import datetime

from discord import TextStyle
from discord.ui import Modal, TextInput
from Interface.ApplicationButtons import ApplicationButtons

class ApplicationModal(Modal, title="Task Force Application Form"):
    def __init__(self):
        super().__init__(timeout=None)
    
        self.question_one = TextInput(
            label="What server or member you joined from?",
            style=TextStyle.short,
            placeholder="e.g PlatinumFive, Developer X#0001, etc",
            required=True
        )

        self.question_two = TextInput(
            label="Desired Callsign?",
            style=TextStyle.short,
            placeholder="e.g Fox, Whisp, Pallas, Decryption, etc",
            required=True
        )

        self.question_three = TextInput(
            label="Your Playstyle?",
            style=TextStyle.short,
            placeholder="e.g Marksman, Pilot, CQB, etc",
            required=True
        )

        self.question_four = TextInput(
            label="Timezone?",
            style=TextStyle.short,
            placeholder="e.g GMT, EST, PST, etc",
            required=True
        )

        self.add_item(self.question_one)
        self.add_item(self.question_two)
        self.add_item(self.question_three)
        self.add_item(self.question_four)

    async def on_submit(self, interaction: discord.Interaction):
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
            name="{} What server or member you joined from?".format(config.ARROW_EMOJI),
            value=f"> {self.question_one.value}",
            inline=False
        )
        application_embed.add_field(
            name="{} Desired Callsign?".format(config.ARROW_EMOJI),
            value=f"> {self.question_two.value}",
            inline=False
        )
        application_embed.add_field(
            name="{} Your Playstyle?".format(config.ARROW_EMOJI),
            value=f"> {self.question_three.value}",
            inline=False
        )
        application_embed.add_field(
            name="{} Timezone?".format(config.ARROW_EMOJI),
            value=f"> {self.question_four.value}",
            inline=False
        )
        application_embed.set_thumbnail(url=config.TFC_ICON)

        application_channel = interaction.guild.get_channel(config.APPLICATION_CHANNEL_ID)

        msg = await application_channel.send(content=interaction.user.mention, embed=application_embed, view=ApplicationButtons())
        await interaction.response.send_message(content="Thanks for applying!\nYou can see your submitted application here: {}".format(msg.jump_url), ephemeral=True)