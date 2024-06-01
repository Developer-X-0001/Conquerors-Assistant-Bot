import config
import discord

from discord import ButtonStyle
from discord.ui import View, Button, button, Select
from Interface.Locations.KPsHouse import KPsHouseEmbed

class NeutralLocationsView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(NeutralLocationsSelector())
    
class NeutralLocationsSelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="K.P's House", value=0)
        ]

        super().__init__(
            placeholder="Choose an option to view locations...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="neutral_locations_menu"
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=KPsHouseEmbed, view=GoBackView())
            return
        
class GoBackView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Go Back", style=ButtonStyle.gray)
    async def go_back_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Neutral Locations",
            description="__**Choose a location from the following:**__\n- K.P's House",
            color=discord.Color.light_gray()
        )
        await interaction.response.edit_message(embed=embed, view=NeutralLocationsView())
        return