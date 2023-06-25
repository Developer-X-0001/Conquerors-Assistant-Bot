import config
import discord

from discord import ButtonStyle, TextStyle
from discord.ui import View, Button, TextInput, Modal, button

class ReportButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Report", style=ButtonStyle.red)
    async def report_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(ReportModal())

class ReportModal(Modal, title="Error Report Modal"):
    def __init__(self):
        super().__init__(timeout=None)

        self.error_code = TextInput(
            label="Error Code:",
            placeholder="Please provide the error code...",
            style=TextStyle.short,
            required=True
        )

        self.error_details = TextInput(
            label="Error Details:",
            placeholder="Please describe the issue...",
            style=TextStyle.long,
            required=False
        )

    async def on_submit(self, interaction: discord.Interaction):
        error_logs_channel = interaction.guild.get_channel(config.ERROR_LOGS_CHANNEL_ID)
        error_embed = discord.Embed(
            title="Error Report",
            color=config.TFC_GOLD
        )
        error_embed.add_field(
            name="__Reporter Details:__",
            value="**Username (ID):** {} ({})\n**Joined At:** <t:{joined_at}:D> (<t:{joined_at}:R>)\n**Created At:** <t:{created_at}:D> (<t:{created_at}:R>)".format(
                interaction.user.name, interaction.user.id, joined_at=round(interaction.user.joined_at.timestamp()), created_at=round(interaction.user.created_at.timestamp())
            ),
            inline=False
        )
        error_embed.add_field(
            name="__Error Details:__",
            value="**Error Code:** {}\n**Details:** {}".format(
                self.error_code.value, 'Not provided' if self.error_details.value is None else self.error_details.value
            )
        )

        await error_logs_channel.send(content=interaction.client.application.owner.mention, embed=error_embed)