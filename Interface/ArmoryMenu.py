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
                description="# 1COY \"Sentinels\" Armory",
                color=config.SENTINELS_RED
            )
            embed.add_field(
                name="__Standard Uniform:__",
                value="1. Marine Raider Regiment (M81 WOODLAND) *$600*\n2. Flannel *Event Achieved*",
                inline=False
            )
            embed.add_field(
                name="__Standard Helmets:__",
                value="1. MICH 2000 *$0*\n2. INTEL BALLISTIC 3.0 *$1200*\n3. MARITIME BALLISTIC *$1400*\n4. BOONIE *$20-30*\n\n- *Helmet must be tan or varicam.*\n- *You may customize your helmet to any realistic degree.*",
                inline=False
            )
            embed.add_field(
                name="__Standard Vests:__",
                value="1. MPC *$1388*\n2. OBAS-QR *$1440*\n3. CVS Vest *$3103*\n\n- *Vest and accessories must be varivam or tan.*\n- *You may customize your vest to any realistic degree.*\n- *You may use the flag of your nationality.*",
                inline=False
            )
            embed.add_field(
                name="__Standard Belts:__",
                value="1. RIGGER'S BELT *$0*\n2. OPERATOR GUN BELT *$810*\n\n- *Belt and accessories must be varicam or tan.*\n- *You may customize your belt to any realistic degree.*",
                inline=False
            )
            embed.add_field(
                name="__Weapon Restrictions:__",
                value="- *Any NATO compliant weapon is permitted.*\n- *All secondary's are permitted except MAKAROV PM, Deagle and BE75 Auto.*\n- *Russian weapons or otherwise AK based weapons are prohibited.*\n- *You may customize your weapon to any realistic degree.*",
                inline=False
            )
            embed.set_thumbnail(url=config.SENTINELS_ICON)
            embed.set_image(url=config.SENTINELS_BANNER)

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=LoadoutImageView(), ephemeral=True)
            return

        if value == 1:
            embed = discord.Embed(
                description="# 2COY \"Hailstorm\" Armory",
                color=config.HAILSTORM_BLUE
            )
            embed.add_field(
                name="__Standard Uniform:__",
                value="1. US PCU Block I L5 *$300*\n2. AC Combat (VariCam) *$600*",
                inline=False
            )
            embed.add_field(
                name="__Standard Helmets:__",
                value="1. HGU-56/P *$3000*\n\n- *Helmet and accessory colors must be vericam.*\n- *You may customize your helmet to any realistic degree.*",
                inline=False
            )
            embed.add_field(
                name="__Standard Vests:__",
                value="1. MPC *$1388*\n2. OBAS-QR *$1440*\n3. CVS Vest *$3103*\n\n- *Vest and accessories must be vericam.*\n- *You may customize your vest to any realistic degree.*\n- *You may use the flag of your nationality.*",
                inline=False
            )
            embed.add_field(
                name="__Standard Belts:__",
                value="1. RIGGER'S BELT *$0*\n2. OPERATOR GUN BELT *$810*\n\n- *Belt and accessories must be vericam.*\n- *You may customize your belt to any realistic degree.*",
                inline=False
            )
            embed.add_field(
                name="__Weapon Restrictions:__",
                value="1. UMP45 *$1700*\n2. MP5 *$2100*\n3. MP7 *$2400*\n\n- *All secondary's are permitted except MAKAROV PM, Deagle and BE75 Auto.*\n- *You may customize your weapon to any realistic degree.*",
                inline=False
            )
            embed.set_thumbnail(url=config.HAILSTORM_ICON)
            embed.set_image(url=config.HAILSTORM_BANNER)

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=LoadoutImageView(), ephemeral=True)
            return

        if value == 2:
            embed = discord.Embed(
                description="# Recruits \"Orion\" Armory",
                color=config.RECRUIT_PURPLE
            )
            embed.add_field(
                name="__Standard Uniform:__",
                value="1. SPECIAL PROJECTS GROUP *$600*",
                inline=False
            )
            embed.add_field(
                name="__Standard Helmets:__",
                value="1. MICH 2000 *$0*\n2. CAP *$20*\n\n- *Helmet must be black.*",
                inline=False
            )
            embed.add_field(
                name="__Standard Vests:__",
                value="- *Prohibited.*\n- RUCKSACK *$660*\n- *Rucksack must be black.*",
                inline=False
            )
            embed.add_field(
                name="__Standard Belts:__",
                value="1. RIGGER'S BELT *$0*\n2. OPERATOR GUN BELT *$810*\n\n- *Belt and accessories must be black.*\n- *You may customize your belt to any realistic degree.*",
                inline=False
            )
            embed.add_field(
                name="__Weapon Restrictions:__",
                value="- *Any NATO compliant weapon is permitted.*\n- *All secondary's are permitted except MAKAROV PM, Deagle and BE75 Auto.*\n- *Russian weapons or otherwise AK based weapons are prohibited.*\n- *You may customize your weapon to any realistic degree.*\n- *Any magazine capacity higher than 30 rounds is prohibited.*",
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
        description = interaction.message.embeds[0].description

        if description == "# 1COY \"Sentinels\" Armory":
            await interaction.response.send_message(embed=discord.Embed(description="#"+description, color=config.SENTINELS_RED).set_image(url=config.SENTINELS_INGAME_IMAGE), ephemeral=True)
            return

        if description == "# 2COY \"Hailstorm\" Armory":
            await interaction.response.send_message(embed=discord.Embed(description="#"+description, color=config.HAILSTORM_BLUE).set_image(url=config.HAILSTORM_INGAME_IMAGE), ephemeral=True)
            return

        if description == "# Recruits \"Orion\" Armory":
            await interaction.response.send_message(embed=discord.Embed(description="#"+description, color=config.RECRUIT_PURPLE).set_image(url=config.ORION_INGAME_IMAGE), ephemeral=True)
            return
        
        else:
            interaction.response.defer()
            return
    
    @button(label="View Menu Image", emoji="📷", style=ButtonStyle.gray)
    async def vieW_menu_image_btn(self, interaction: discord.Interaction, button: Button):
        description = interaction.message.embeds[0].description

        if description == "# 1COY \"Sentinels\" Armory":
            await interaction.response.send_message(embed=discord.Embed(description="#"+description, color=config.SENTINELS_RED).set_image(url=config.SENTINELS_MENU_IMAGE), ephemeral=True)
            return

        if description == "# 2COY \"Hailstorm\" Armory":
            await interaction.response.send_message(embed=discord.Embed(description="#"+description, color=config.HAILSTORM_BLUE).set_image(url=config.HAILSTORM_MENU_IMAGE), ephemeral=True)
            return

        if description == "# Recruits \"Orion\" Armory":
            await interaction.response.send_message(embed=discord.Embed(description="#"+description, color=config.RECRUIT_PURPLE).set_image(url=config.ORION_MENU_IMAGE), ephemeral=True)
            return
        
        else:
            interaction.response.defer()
            return