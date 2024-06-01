import config
import discord

from discord import ButtonStyle
from Interface.Locations.Bunker import *
from discord.ui import View, Button, button, Select

class SpecialLocationsView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SpecialLocationsSelector())
    
class SpecialLocationsSelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Bunker", value=0)
        ]

        super().__init__(
            placeholder="Choose an option to view locations...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="special_locations_menu"
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=BunkerEmbed, view=GoBackView())
            return
        
class GoBackView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Bunker", style=ButtonStyle.blurple)
    async def bunker_btn(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(embed=BunkerEmbed)
        return

    @button(label="Access", style=ButtonStyle.blurple)
    async def access_btn(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(embed=BunkerAccessEmbed)
        return

    @button(label="Layout", style=ButtonStyle.blurple)
    async def layout_btn(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(embed=BunkerLayoutEmbed)
        return

    @button(label="Mission", style=ButtonStyle.blurple)
    async def mission_btn(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(embed=BunkerMissionEmbed)
        return

    @button(label="Go Back", style=ButtonStyle.gray, row=1)
    async def go_back_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Special Locations",
            description="__**Choose a location from the following:**__\n- Bunker",
            color=discord.Color.blurple()
        )
        await interaction.response.edit_message(embed=embed, view=SpecialLocationsView())
        return
    