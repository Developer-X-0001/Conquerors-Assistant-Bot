import config
import sqlite3
import discord

from discord import ButtonStyle
from discord.ui import Select, View, Button, button
from Interface.Weapons import Rifles, Secondaries, SubMachineGuns, DMRsAndSnipers

class ArmoryMenuView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ArmorySelectMenu())
        self.add_item(WeaponSelectMenu())
        self.add_item(ExtrasSelectMenu())
    
    @button(label="--------------------------- Weapons ---------------------------", style=ButtonStyle.gray, custom_id="view_weapons_button", disabled=True, row=1)
    async def viewWeaponsBtn(self, interaction: discord.Interaction, button: Button):
        return
    
    @button(label="---------------------------- Extras ----------------------------", style=ButtonStyle.gray, custom_id="view_extras_button", disabled=True, row=3)
    async def viewExtrasBtn(self, interaction: discord.Interaction, button: Button):
        return
    
class ArmorySelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Sentinels", emoji=config.SENTINELS_EMOJI, description="Check 1COY \"Sentinels\" Uniform", value=0),
            discord.SelectOption(label="Hailstorm", emoji=config.HAILSTORM_EMOJI, description="Check 2COY \"Hailstorm\" Uniform", value=1),
            discord.SelectOption(label="Orion", emoji=config.ORION_EMOJI, description="Check Recruits \"Orion\" Uniform", value=2)
        ]

        super().__init__(
            placeholder="Choose an option to view uniforms...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="armory_select_menu",
            row=0
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
            embed.set_thumbnail(url=config.ORION_ICON)
            embed.set_image(url=config.ORION_BANNER)

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=LoadoutImageView(), ephemeral=True)
            return

class WeaponSelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Rifles", value=0),
            discord.SelectOption(label="DMR's & Snipers", description="For marksmen", value=1),
            discord.SelectOption(label="Sub-Machine Guns", description="For pilots only", value=2),
            discord.SelectOption(label="Secondaries", value=3)
        ]

        super().__init__(
            placeholder="Choose an option to view weapons...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="weapon_select_menu",
            row=2
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return
        
        value = int(self.values[0])

        if value == 0:
            embed = discord.Embed(
                description="# Rifles\
                    \n- M4A1\
                    \n- Mk 18\
                    \n- RF416 A5\
                    \n- SCAR-H\
                    \n- SCAR-L",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=RiflesSelectView(), ephemeral=True)
            return

        if value == 1:
            embed = discord.Embed(
                description="# DMR's & Snipers\
                    \n- M110\
                    \n- M2010\
                    \n- M24\
                    \n- AWM",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=DMRsAndSnipersSelectView(), ephemeral=True)
            return

        if value == 2:
            embed = discord.Embed(
                description="# Sub-machine Guns\
                    \n- MP5\
                    \n- MP7\
                    \n- UMP45",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=SubMachineGunsSelectView(), ephemeral=True)
            return

        if value == 3:
            embed = discord.Embed(
                description="# Secondaries\
                    \n- M17\
                    \n- G17\
                    \n- M9",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, view=SecondariesSelectView(), ephemeral=True)
            return

class ExtrasSelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Optics & Scopes", value=0),
            discord.SelectOption(label="Attachments", value=1),
            discord.SelectOption(label="Foregrips", value=2),
            discord.SelectOption(label="Muzzles", value=3)
        ]
    
        super().__init__(
            placeholder="Chose an option to view extras...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="extras_select_menu",
            row=4
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            embed = discord.Embed(
                description="# Optics & Scopes\
                \n- 3.5-10x40mm Mark 4 LR/T M2 (Marksman)\
                \n- 6.5-20x50mm Mark 4 ER/T M5A2 (Marksman)\
                \n- 3-18x44mm ECOS-O (Marksman)\
                \n- 12x56mm PM II/LP (Marksman)\
                \n- 12x56mm M5X1 (Marksman) \
                \n- 1-6x LPVO \
                \n- 4x M150 RCO (ACOG)\
                \n- 4x LDS (ELCAN SPECTRE)\
                \n- 1x EOTech\
                \n- 1x EOTech w/Riser\
                \n- 1x SU231-Peq/A\
                \n- 1x T2 any\
                \n- 1x Canted Sights\
                \n- Any iron sight folded",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, ephemeral=True)
            return

        if value == 1:
            embed = discord.Embed(
                description="# Attachments\
                \n- AN/PEQ15-A (Laser)\
                \n- AN/PEQ15 (Laser)\
                \n- IRONCLAD (Laser)\
                \n- LLM19 (Laser + Flashlight)\
                \n- M952v (Flashlight)\
                \n- WMX200 (Flashlight)\
                \n- M600U (Flashlight)\
                \n- 2D + KR-1U (Flashlight)\
                \n- SR (Pressure Switch)\
                \n- SR-D (Pressure Switch)\
                \n- RMT-400-A8 (Pressure Switch)",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, ephemeral=True)
            return

        if value == 2:
            embed = discord.Embed(
                description="# Foregrips\
                \n- CVG\
                \n- SHIP\
                \n- Angled Foregrip\
                \n- Handbrake\
                \n- INTEGRIP\
                \n- Gunfighter Foregrips\
                \n- BGV-MK46K\
                \n- Assault Foregrip",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, ephemeral=True)
            return

        if value == 3:
            embed = discord.Embed(
                description="# Muzzles\
                \n- Multicaliber (suppressor)\
                \n- SOCOM556-RC\
                \n- SOCOM556-MINI2\
                \n- QDSS-NT4\
                \n- FH556RC\
                \n- A1\
                \n- War Pig",
                color=config.TFC_GOLD
            )

            await interaction.response.edit_message(view=ArmoryMenuView())
            await interaction.followup.send(embed=embed, ephemeral=True)
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
        
class RiflesSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RifleSelector())

class DMRsAndSnipersSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(DMRsAndSniperSelector())

class SubMachineGunsSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SubMachineGunSelector())

class SecondariesSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SecondarySelector())
    
class RifleSelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="M4A1", value=0),
            discord.SelectOption(label="Mk 18", value=1),
            discord.SelectOption(label="RF416 A5", value=2),
            discord.SelectOption(label="SCAR-H", value=3),
            discord.SelectOption(label="SCAR-L", value=4)
        ]

        super().__init__(
            placeholder="Choose an option to view details...",
            min_values=0,
            max_values=1,
            options=options,
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=Rifles.m4a1_embed, view=RiflesSelectView())
            return
    
        if value == 1:
            await interaction.response.edit_message(embed=Rifles.mk18_embed, view=RiflesSelectView())
            return
        
        if value == 2:
            await interaction.response.edit_message(embed=Rifles.rf416a5_embed, view=RiflesSelectView())
            return
        
        if value == 3:
            await interaction.response.edit_message(embed=Rifles.scarh_embed, view=RiflesSelectView())
            return
        
        if value == 4:
            await interaction.response.edit_message(embed=Rifles.scarl_embed, view=RiflesSelectView())
            return

class DMRsAndSniperSelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="M110", value=0),
            discord.SelectOption(label="M2010", value=1),
            discord.SelectOption(label="M24", value=2),
            discord.SelectOption(label="AWM", value=3)
        ]

        super().__init__(
            placeholder="Choose an option to view details...",
            min_values=0,
            max_values=1,
            options=options,
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=DMRsAndSnipers.m110_embed, view=DMRsAndSnipersSelectView())
            return
    
        if value == 1:
            await interaction.response.edit_message(embed=DMRsAndSnipers.m2010_embed, view=DMRsAndSnipersSelectView())
            return
        
        if value == 2:
            await interaction.response.edit_message(embed=DMRsAndSnipers.m24_embed, view=DMRsAndSnipersSelectView())
            return
    
        if value == 3:
            await interaction.response.edit_message(embed=DMRsAndSnipers.awm_embed, view=DMRsAndSnipersSelectView())
            return
        
class SubMachineGunSelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="MP5", value=0),
            discord.SelectOption(label="MP7", value=1),
            discord.SelectOption(label="UMP45", value=2)
        ]

        super().__init__(
            placeholder="Choose an option to view details...",
            min_values=0,
            max_values=1,
            options=options,
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=SubMachineGuns.mp5_embed, view=SubMachineGunsSelectView())
            return
    
        if value == 1:
            await interaction.response.edit_message(embed=SubMachineGuns.mp7_embed, view=SubMachineGunsSelectView())
            return
        
        if value == 2:
            await interaction.response.edit_message(embed=SubMachineGuns.ump45_embed, view=SubMachineGunsSelectView())
            return

class SecondarySelector(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="M17", value=0),
            discord.SelectOption(label="G17", value=1),
            discord.SelectOption(label="M9", value=2)
        ]

        super().__init__(
            placeholder="Choose an option to view details...",
            min_values=0,
            max_values=1,
            options=options,
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return

        value = int(self.values[0])

        if value == 0:
            await interaction.response.edit_message(embed=Secondaries.m17_embed, view=SecondariesSelectView())
            return
    
        if value == 1:
            await interaction.response.edit_message(embed=Secondaries.g17_embed, view=SecondariesSelectView())
            return
        
        if value == 2:
            await interaction.response.edit_message(embed=Secondaries.m9_embed, view=SecondariesSelectView())
            return