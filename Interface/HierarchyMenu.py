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
        options = []

        for rank in RANK_LIST:
            if not rank.endswith('0'):
                name = RANKS[rank]['name']
                emoji = None if not RANKS[rank]['emoji'] else RANKS[rank]['emoji']

                options.append(
                    discord.SelectOption(label=name, emoji=emoji, description="", value=rank)
                )

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
        requirement = RANKS[value]['requirement']
        
        embed = discord.Embed(
            title=RANKS[value]['name'],
            description=f"**Requirements:** {requirement}",
            color=config.TFC_GOLD
        )
        embed.set_thumbnail(url=RANKS[value]['icon'])

        await interaction.response.edit_message(view=HierarchyMenuView())
        await interaction.followup.send(embed=embed, ephemeral=True)
