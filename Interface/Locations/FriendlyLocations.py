import config
import discord

from discord import ButtonStyle
from discord.ui import View, Button, button, Select
from Interface.Locations.FOB import *
from Interface.Locations.SochrainaCity import *
from Interface.Locations.ShorelineCamp import ShorelineCampEmbed

class FriendlyLocationsView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FriendlyLocationsSelector())
    
class FriendlyLocationsSelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Forward Operating Base", value=0),
            discord.SelectOption(label="Sochraina City", value=1),
            discord.SelectOption(label="Shoreline Camp", value=2)
        ]

        super().__init__(
            placeholder="Choose an option to view locations...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="friendly_locations_menu"
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=FOBEmbed, view=DetailedGoBackView())
        
        if value == 1:
            await interaction.response.edit_message(embed=SochrainaEmbed, view=DetailedGoBackView())
        
        if value == 2:
            await interaction.response.edit_message(embed=ShorelineCampEmbed, view=GoBackView())
            return

class GoBackView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Go Back", style=ButtonStyle.gray)
    async def go_back_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Friendly Locations",
            description="__**Choose a location from the following:**__\n- Forward Operating Base\n- Sochraina City\n- Shoreline Camp",
            color=discord.Color.green()
        )
        await interaction.response.edit_message(embed=embed, view=FriendlyLocationsView())
        return
        
class DetailedGoBackView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Go Back", style=ButtonStyle.gray)
    async def go_back_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Friendly Locations",
            description="__**Choose a location from the following:**__\n- Forward Operating Base\n- Sochraina City\n- Shoreline Camp",
            color=discord.Color.green()
        )
        await interaction.response.edit_message(embed=embed, view=FriendlyLocationsView())
        return

    @button(label="Detailed Information", style=ButtonStyle.green)
    async def detailes_btn(self, interaction: discord.Interaction, button: Button):
        embed = interaction.message.embeds[0]

        if embed.title == "Forward Operating Base (FOB)":
            await interaction.response.edit_message(embed=FOBDetailedEmbed, view=FOBDetailsView())

        if embed.title == "Sochraina City":
            await interaction.response.edit_message(embed=SochrainaDetailedEmbed, view=SochrainaCityDetailsView())
            return
    
    @button(label="Switch to Bird\'s Eye View", style=ButtonStyle.green)
    async def switch_img_btn(self, interaction: discord.Interaction, button: Button):
        embed = interaction.message.embeds[0]

        if embed.title == "Forward Operating Base (FOB)":
            if self.switch_img_btn.label == "Switch to Bird\'s Eye View":
                embed.set_image(url=config.FOB_MAP_IMAGE)
                self.switch_img_btn.label = 'Switch to Front View'
                await interaction.response.edit_message(embed=embed, view=self)
                return
            
            if self.switch_img_btn.label == 'Switch to Front View':
                await interaction.response.send_message(embed=discord.Embed(description="Front View isn't available for Forward Operating Base (FOB) yet.", color=discord.Color.red()), ephemeral=True)
                return
            
                embed.set_image(url=config.FOB_IMAGE)
                self.switch_img_btn.label = "Switch to Bird\'s Eye View"
                await interaction.response.edit_message(embed=embed, view=self)
                return

        if embed.title == "Sochraina City":
            if self.switch_img_btn.label == "Switch to Bird\'s Eye View":
                embed.set_image(url=config.SOCHRAINA_CITY_MAP_IMAGE)
                self.switch_img_btn.label = 'Switch to Front View'
                await interaction.response.edit_message(embed=embed, view=self)
                return
            
            if self.switch_img_btn.label == 'Switch to Front View':
                embed.set_image(url=config.SOCHRAINA_CITY_IMAGE)
                self.switch_img_btn.label = "Switch to Bird\'s Eye View"
                await interaction.response.edit_message(embed=embed, view=self)
                return

class FOBDetailsView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FOBPointsOfInterestSelector())
    
    @button(label="Go Back", style=ButtonStyle.gray, row=1)
    async def fob_go_back(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(embed=FOBEmbed, view=DetailedGoBackView())

class FOBPointsOfInterestSelector(Select):
    def __init__(self):
        super().__init__(
            placeholder="Points of Interest...",
            min_values=0,
            max_values=1,
            options=FOBPointOfInterests
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return
        
        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=FOBCommandCenterEmbed)
            return
        
        if value == 1:
            await interaction.response.edit_message(embed=FOBVehicleDepotEmbed),
            return

        if value == 2:
            await interaction.response.edit_message(embed=FOBHelicopterLandingZoneEmbed),
            return
    
        if value == 3:
            await interaction.response.edit_message(embed=FOBHangarsEmbed)
            return
        
        if value == 4:
            await interaction.response.edit_message(embed=FOBKillhouseEmbed),
            return

        if value == 5:
            await interaction.response.edit_message(embed=FOBVehicleWorkshopEmbed),
            return
        
        if value == 6:
            await interaction.response.edit_message(embed=FOBShootingRangeEmbed)
            return
        
        if value == 7:
            await interaction.response.edit_message(embed=FOBRunwayEmbed),
            return

        if value == 8:
            await interaction.response.edit_message(embed=FOBRefugeeProcessingCampEmbed),
            return

class SochrainaCityDetailsView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SochrainaCityPointsOfInterestSelector())
    
    @button(label="Go Back", style=ButtonStyle.gray, row=1)
    async def sochraina_go_back(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(embed=SochrainaEmbed, view=DetailedGoBackView())
    
class SochrainaCityPointsOfInterestSelector(Select):
    def __init__(self):
        super().__init__(
            placeholder="Points of Interest...",
            min_values=0,
            max_values=1,
            options=SochrainaPointOfInterests
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return
        
        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=SochrainaAvenueEmbed)
            return
        
        if value == 1:
            await interaction.response.edit_message(embed=SochrainaCheckpointOneEmbed)
            return
        
        if value == 2:
            await interaction.response.edit_message(embed=SochrainaCheckpointTwoEmbed)
            return
        
        if value == 3:
            await interaction.response.edit_message(embed=SochrainaCoffeeShopEmbed)
            return
        
        if value == 4:
            await interaction.response.edit_message(embed=SochrainaIsabelInnEmbed)
            return
        
        if value == 5:
            await interaction.response.edit_message(embed=SochrainaLighthouseEmbed)
            return
        
        if value == 6:
            await interaction.response.edit_message(embed=SochrainaMarketplaceEmbed)
            return
        
        if value == 7:
            await interaction.response.edit_message(embed=SochrainaPierEmbed)
            return
        
        if value == 8:
            await interaction.response.edit_message(embed=SochrainaWaterfrontEmbed)
            return