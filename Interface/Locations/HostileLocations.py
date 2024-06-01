import config
import discord

from discord import ButtonStyle
from discord.ui import View, Button, button, Select
from Interface.Locations.Crashsite import CrashsiteEmbed
from Interface.Locations.DOU import DOUEmbed
from Interface.Locations.Depot import DepotEmbed
from Interface.Locations.DepotOutpost import DepotOutpostEmbed
from Interface.Locations.ForestHouse import ForestHouseEmbed
from Interface.Locations.FortRonograd import FortRonogradEmbed
from Interface.Locations.MountainOutpost import MountainOutpostEmbed
from Interface.Locations.NavalBase import NavalBaseEmbed
from Interface.Locations.Quarry import QuarryEmbed
from Interface.Locations.RonogradCity import RonogradCityEmbed
from Interface.Locations.Village import VillageEmbed

class HostileLocationsView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(HostileLocationsSelector())
    
class HostileLocationsSelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Crash Site (Pushkino)", value=0),
            discord.SelectOption(label="Department of Utilities (D.O.U)", value=1),
            discord.SelectOption(label="Depot", value=2),
            discord.SelectOption(label="Depot Outpost", value=3),
            discord.SelectOption(label="Forest House", value=4),
            discord.SelectOption(label="Fort Ronograd", value=5),
            discord.SelectOption(label="Mountain Outpost", value=6),
            discord.SelectOption(label="Naval Base", value=7),
            discord.SelectOption(label="Quarry", value=8),
            discord.SelectOption(label="Ronograd City", value=9),
            discord.SelectOption(label="Village", value=10)
        ]

        super().__init__(
            placeholder="Choose an option to view locations...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="hostile_locations_menu"
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=CrashsiteEmbed, view=GoBackView())
        
        if value == 1:
            await interaction.response.edit_message(embed=DOUEmbed, view=GoBackView())
        
        if value == 2:
            await interaction.response.edit_message(embed=DepotEmbed, view=GoBackView())

        if value == 3:
            await interaction.response.edit_message(embed=DepotOutpostEmbed, view=GoBackView())
            return

        if value == 4:
            await interaction.response.edit_message(embed=ForestHouseEmbed, view=GoBackView())
            return

        if value == 5:
            await interaction.response.edit_message(embed=FortRonogradEmbed, view=GoBackView())

        if value == 6:
            await interaction.response.edit_message(embed=MountainOutpostEmbed, view=GoBackView())
        
        if value == 7:
            await interaction.response.edit_message(embed=NavalBaseEmbed, view=GoBackView())
        
        if value == 8:
            await interaction.response.edit_message(embed=QuarryEmbed, view=GoBackView())
        
        if value == 9:
            await interaction.response.edit_message(embed=RonogradCityEmbed, view=GoBackView())
        
        if value == 10:
            await interaction.response.edit_message(embed=VillageEmbed, view=GoBackView())
            
class GoBackView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Go Back", style=ButtonStyle.gray)
    async def go_back_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Hostile Locations",
            description="__**Choose a location from the following:**__\n- Crash Site (Pushkino)\n- Department of Utilities (D.O.U)\n- Depot\n- Depot Outpost\n- Forest House\n- Fort Ronograd\n- Mountain Outpost\n- Naval Base\n- Quarry\n- Ronograd City\n- Village",
            color=discord.Color.red()
        )
        await interaction.response.edit_message(embed=embed, view=HostileLocationsView())
        return