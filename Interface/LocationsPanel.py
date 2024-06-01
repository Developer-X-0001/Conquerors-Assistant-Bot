import config
import discord

from discord import ButtonStyle
from Interface.Locations.FriendlyLocations import FriendlyLocationsView
from Interface.Locations.HostileLocations import HostileLocationsView
from Interface.Locations.NeutralLocations import NeutralLocationsView
from Interface.Locations.SpecialLocations import SpecialLocationsView
from discord.ui import View, Button, button

class LocationsPanelView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Friendly (3)", style=ButtonStyle.green, custom_id="friendly_btn")
    async def friendly_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Friendly Locations",
            description="__**Choose a location from the following:**__\n- Forward Operating Base\n- Sochraina City\n- Shoreline Camp",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed, view=FriendlyLocationsView(), ephemeral=True)
        return
    
    @button(label="Neutral (1)", style=ButtonStyle.gray, custom_id="gray_btn")
    async def gray_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Neutral Locations",
            description="__**Choose a location from the following:**__\n- K.P's House",
            color=discord.Color.light_gray()
        )
        await interaction.response.send_message(embed=embed, view=NeutralLocationsView(), ephemeral=True)
        return

    @button(label="Hostile (11)", style=ButtonStyle.red, custom_id="red_btn")
    async def red_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Hostile Locations",
            description="__**Choose a location from the following:**__\n- Crash Site (Pushkino)\n- Department of Utilities (D.O.U)\n- Depot\n- Depot Outpost\n- Forest House\n- Fort Ronograd\n- Mountain Outpost\n- Naval Base\n- Quarry\n- Ronograd City\n- Village",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, view=HostileLocationsView(), ephemeral=True)
        return

    @button(label="Special (1)", style=ButtonStyle.blurple, custom_id="special_btn")
    async def special_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Special Locations",
            description="__**Choose a location from the following:**__\n- Bunker",
            color=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed, view=SpecialLocationsView(), ephemeral=True)
        return