import config
import discord

from discord.ui import Select, View
from config import RANKS, RANK_LIST

class HierarchyMenuView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(HierarchySelectMenu())
    
class HierarchySelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Private", emoji=RANKS['E1']['emoji'], description="", value="E1"),
            discord.SelectOption(label="Private First Class", emoji=RANKS['E2']['emoji'], description="", value="E2"),
            discord.SelectOption(label="Lance Corporal", emoji=RANKS['E3']['emoji'], description="", value="E3"),
            discord.SelectOption(label="Corporal", emoji=RANKS['N1']['emoji'], description="", value="N1"),
            discord.SelectOption(label="Master Corporal", emoji=RANKS['N2']['emoji'], description="", value="N2"),
            discord.SelectOption(label="Sergeant", emoji=RANKS['N3']['emoji'], description="", value="N3"),
            discord.SelectOption(label="Staff Sergeant", emoji=RANKS['N4']['emoji'], description="", value="N4"),
            discord.SelectOption(label="Master Sergeant", emoji=RANKS['M1']['emoji'], description="", value="M1"),
            discord.SelectOption(label="First Sergeant", emoji=RANKS['M2']['emoji'], description="", value="M2"),
            discord.SelectOption(label="Sergeant Major", emoji=RANKS['M3']['emoji'], description="", value="M3"),
            discord.SelectOption(label="Warrant Officer 1", emoji=RANKS['W1']['emoji'], description="", value="W1"),
            discord.SelectOption(label="Warrant Officer 2", emoji=RANKS['W2']['emoji'], description="", value="W2"),
            discord.SelectOption(label="Warrant Officer 3", emoji=RANKS['W3']['emoji'], description="", value="W3"),
            discord.SelectOption(label="Warrant Officer 4", emoji=RANKS['W4']['emoji'], description="", value="W4"),
            discord.SelectOption(label="Warrant Officer 5", emoji=RANKS['W5']['emoji'], description="", value="W5"),
            discord.SelectOption(label="Overseer", emoji=RANKS['O1']['emoji'], description="", value="O1"),
            discord.SelectOption(label="2nd Lieutenant", emoji=RANKS['O2']['emoji'], description="", value="O2"),
            discord.SelectOption(label="1st Lieutenant", emoji=RANKS['O3']['emoji'], description="", value="O3"),
            discord.SelectOption(label="Captain", emoji=RANKS['O4']['emoji'], description="", value="O4"),
            discord.SelectOption(label="Major", emoji=RANKS['O5']['emoji'], description="", value="O5"),
            discord.SelectOption(label="Lieutenant Colonel", emoji=RANKS['O6']['emoji'], description="", value="O6"),
            discord.SelectOption(label="Colonel", emoji=RANKS['O7']['emoji'], description="", value="O7"),
            discord.SelectOption(label="Brigadier General", emoji=RANKS['O8']['emoji'], description="", value="O8"),
            discord.SelectOption(label="Major General", emoji=RANKS['O9']['emoji'], description="", value="O9")
        ]

        super().__init__(
            placeholder="Choose a rank to view details...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="hierarchy_select_menu"
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return
        
        value = self.values[0]
        rank_index = RANK_LIST.index(value)

        if rank_index < 11:
            requirement = f"{RANKS[value]['points']} Points"
        
        if 22 >= rank_index >= 11:
            requirement = "Merit Required"
        
        if rank_index >= 23:
            requirement = "Not Available"

        embed = discord.Embed(
            title=RANKS[value]['name'],
            description=f"**Requirement:** {requirement}",
            color=config.TFC_GOLD
        )
        embed.set_thumbnail(url=RANKS[value]['icon'])

        await interaction.response.edit_message(view=HierarchyMenuView())
        await interaction.followup.send(embed=embed, ephemeral=True)
