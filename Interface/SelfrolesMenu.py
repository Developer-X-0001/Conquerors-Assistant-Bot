import config
import discord

from discord.ui import Select, View

class SelfrolesMenuView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(PingRolesSelect())
    
class PingRolesSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Community Ping", emoji="🤝", description="This is used for community related stuff", value=1145407805050855424),
            discord.SelectOption(label="Minor Announcement Ping", emoji="📢", description="Low priority announcements", value=1145407806208475369),
            discord.SelectOption(label="Game Night Ping", emoji="🎲", description="Playing games other than BRM5/ACS", value=1145407808179802204),
            discord.SelectOption(label="Faction Update Ping", emoji=config.TFC_EMOJI, description="Used for updates related to the faction", value=1145407809790423041),
            discord.SelectOption(label="Bot Update Ping", emoji="🤖", description="Used by Fox for faction bot updates", value=1145408146098114570),
            discord.SelectOption(label="ACS Update Ping", emoji=config.ROBLOX_DEV_EMOJI, description="This is used for updates for ACS game", value=1145408147599671316)
        ]

        super().__init__(
            placeholder="Choose a ping role...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="ping_role_select_menu"
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return
        
        value = int(self.values[0])
        role = interaction.guild.get_role(value)
        
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.edit_message(view=SelfrolesMenuView())
            await interaction.followup.send(content="{} You dropped {} role.".format(config.ERROR_EMOJI, role.mention), ephemeral=True)
        
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.edit_message(view=SelfrolesMenuView())
            await interaction.followup.send(content="{} You picked {} role.".format(config.DONE_EMOJI, role.mention), ephemeral=True)