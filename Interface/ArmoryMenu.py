import config
import sqlite3
import discord

from discord import ButtonStyle
from discord.ui import Select, View, Button, button

class ArmoryMenuView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ArmorySelectMenu())
    
class ArmorySelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Sentinels", emoji=config.SENTINELS_EMOJI, description="Check 1COY \"Sentinels\" Armory", value=0),
            discord.SelectOption(label="Hailstorm", emoji=config.HAILSTORM_EMOJI, description="Check 2COY \"Hailstorm\" Armory", value=1),
            discord.SelectOption(label="Orion", emoji=config.ORION_EMOJI, description="Check Recruits \"Orion\" Armory", value=2)
        ]

        super().__init__(
            placeholder="Choose an option to view armory...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="armory_select_menu"
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return
        
        value = int(self.values[0])
    
        if value == 0:
            embed = discord.Embed(
                title="1COY \"Sentinels\" Armory",
                color=config.SENTINELS_RED
            )
            embed.add_field(
                name="Operator Kit:",
                value="AC Combat (OCP / Varicam)\nVaricam Camo Equipment",
                inline=False
            )
            embed.add_field(
                name="Helmets:",
                value="Maritime Ballistic\nIntel Ballistic\nMICH 2000\nSentinel Helmet",
                inline=False
            )
            embed.add_field(
                name="Vests:",
                value="MPC Vest\nCVS Vest\nOBAS-QR\nNATO Country Flags (Asian Flags are an exception)",
                inline=False
            )
            embed.add_field(
                name="Belts:",
                value="Customisation Is Infinite",
                inline=False
            )
            embed.add_field(
                name="Gun Restrictions:",
                value="M4A1\nAUG A3 / AUG A1\nC7A2\nMK18\nHK416A5\nMK 16 / 17 SCAR\nMP5 / MP7\n(Any Gun NATO Compliant)",
                inline=False
            )
            embed.set_thumbnail(url=config.SENTINELS_ICON)
            embed.set_image(url=config.SENTINELS_BANNER)

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=LoadoutImageView(), ephemeral=True)
            return

        if value == 1:
            embed = discord.Embed(
                title="2COY \"Hailstorm\" Armory",
                color=config.HAILSTORM_BLUE
            )
            embed.add_field(
                name="Operator Kit:",
                value="US PCU BLOCK I L5\nBlack Camo Equipment",
                inline=False
            )
            embed.add_field(
                name="Helmets:",
                value="HGU-56P",
                inline=False
            )
            embed.add_field(
                name="Vests:",
                value="OBAS-QR\nCVS Vest\nNATO Country Flags (Asian Flags are an exception)",
                inline=False
            )
            embed.add_field(
                name="Belts:",
                value="Customisation Is Infinite",
                inline=False
            )
            embed.add_field(
                name="Gun Restrictions:",
                value="MP5\nMP7\nUMP45",
                inline=False
            )
            embed.set_thumbnail(url=config.HAILSTORM_ICON)
            embed.set_image(url=config.HAILSTORM_BANNER)

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=LoadoutImageView(), ephemeral=True)
            return

        if value == 2:
            embed = discord.Embed(
                title="Recruits \"Orion\" Armory",
                color=config.RECRUIT_PURPLE
            )
            embed.add_field(
                name="Operator Kit:",
                value="AC Combat (Tan 499)\nTan Camo Equipment",
                inline=False
            )
            embed.add_field(
                name="Helmets:",
                value="Cap",
                inline=False
            )
            embed.add_field(
                name="Vests:",
                value="Shirt\nRucksack",
                inline=False
            )
            embed.add_field(
                name="Belts:",
                value="Customisation Is Infinite",
                inline=False
            )
            embed.add_field(
                name="Gun Restrictions:",
                value="M4A1\nAUG A3 / AUG A1\nC7A2\nMK18\nHK416A5\nMK 16 / 17 SCAR\nMP5 / MP7\n(Any Gun NATO Compliant)",
                inline=False
            )
            embed.set_thumbnail(url=config.ORION_ICON)
            embed.set_image(url=config.ORION_BANNER)

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=LoadoutImageView(), ephemeral=True)
            return
    
class LoadoutImageView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="View In-Game Image", emoji="📸", style=ButtonStyle.gray)
    async def view_ingame_image_btn(self, interaction: discord.Interaction, button: Button):
        title = interaction.message.embeds[0].title

        if title == "1COY \"Sentinels\" Armory":
            await interaction.response.send_message(embed=discord.Embed(title=title, color=config.SENTINELS_RED).set_image(url=config.SENTINELS_INGAME_IMAGE), ephemeral=True)
            return

        if title == "2COY \"Hailstorm\" Armory":
            await interaction.response.send_message(embed=discord.Embed(title=title, color=config.HAILSTORM_BLUE).set_image(url=config.HAILSTORM_INGAME_IMAGE), ephemeral=True)
            return

        if title == "Recruits \"Orion\" Armory":
            await interaction.response.send_message(embed=discord.Embed(title=title, color=config.RECRUIT_PURPLE).set_image(url=config.ORION_INGAME_IMAGE), ephemeral=True)
            return
        
        else:
            interaction.response.defer()
            return
    
    @button(label="View Menu Image", emoji="📷", style=ButtonStyle.gray)
    async def vieW_menu_image_btn(self, interaction: discord.Interaction, button: Button):
        title = interaction.message.embeds[0].title

        if title == "1COY \"Sentinels\" Armory":
            await interaction.response.send_message(embed=discord.Embed(title=title, color=config.SENTINELS_RED).set_image(url=config.SENTINELS_MENU_IMAGE), ephemeral=True)
            return

        if title == "2COY \"Hailstorm\" Armory":
            await interaction.response.send_message(embed=discord.Embed(title=title, color=config.HAILSTORM_BLUE).set_image(url=config.HAILSTORM_MENU_IMAGE), ephemeral=True)
            return

        if title == "Recruits \"Orion\" Armory":
            await interaction.response.send_message(embed=discord.Embed(title=title, color=config.RECRUIT_PURPLE).set_image(url=config.ORION_MENU_IMAGE), ephemeral=True)
            return
        
        else:
            interaction.response.defer()
            return