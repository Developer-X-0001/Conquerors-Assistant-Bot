import config 
import sqlite3
import discord

from discord.ui import Select, View
from Interface.QuestionsView import QuestionModal
from Interface.LOARequestView import LOARequestModal
from Interface.PromotionRequest import PromotionRequestView
from Interface.CallsignChangeView import CallsignChangeModal, CallsignReturnView

database = sqlite3.connect("./Databases/data.sqlite")

class InteractionMenuView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(InteractionSelectMenu())
    
class InteractionSelectMenu(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Send LOA Request", emoji=config.LOA_EMOJI, value=0),
            discord.SelectOption(label="Request Promotion", emoji=config.PROMOTION_EMOJI, value=1),
            discord.SelectOption(label="Ask a Question", emoji=config.QUESTION_EMOJI, value=2),
            discord.SelectOption(label="Check Points", emoji=config.POINTS_EMOJI, value=3),
            discord.SelectOption(label="Request Callsign Change", emoji=config.CALLSIGN_EMOJI, value=4)
        ]

        super().__init__(
            placeholder="Choose an option...",
            min_values=0,
            max_values=1,
            options=options,
            custom_id="interactions_select_menu"
        )
    
    async def callback(self, interaction: discord.Interaction):
        if self.values is None or self.values == []:
            await interaction.response.defer()
            return
        
        value = int(self.values[0])

        if value == 0:
            await interaction.response.send_modal(LOARequestModal())
            await interaction.edit_original_response(view=InteractionMenuView())

        if value == 1:
            await interaction.response.edit_message(view=InteractionMenuView())

            current_rank = interaction.user.nick[:2]
            if current_rank == 'O4' or current_rank == 'O5':
                await interaction.followup.send(embed=discord.Embed(description="{} **You're already at the highest or the 2nd highest rank!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
            
            if current_rank.startswith('E'):
                await interaction.followup.send(embed=discord.Embed(description="{} **Please choose a rank that you want to request.**\nAlso make sure your DMs are open, because the decision on your request will be sent to your DMs.".format(config.PROMOTION_EMOJI), color=config.TFC_GOLD), view=PromotionRequestView(interaction.user), ephemeral=True)
                return
            
            else:
                await interaction.followup.send(embed=discord.Embed(description="{} **You can't create a promotion request.**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
                return
        
        if value == 2:
            await interaction.response.send_modal(QuestionModal())
            await interaction.edit_original_response(view=InteractionMenuView())
            return
    
        if value == 3:
            await interaction.response.edit_message(view=InteractionMenuView())
            data = database.execute("SELECT points FROM UserData WHERE user_id = ?", (interaction.user.id,)).fetchone()
            if data is None:
                database.execute("INSERT INTO UserData (user_id, points) VALUES (?, ?)", (interaction.user.id, 0,)).connection.commit()
                points = 0
            else:
                points = int(data[0])

            await interaction.followup.send(embed=discord.Embed(description="You have {} {} points.".format(config.POINTS_EMOJI, points), color=config.TFC_GOLD), ephemeral=True)
            
        if value == 4:
            data = database.execute("SELECT * FROM CallsignRequests WHERE user_id = ?", (interaction.user.id,)).fetchone()
            if data is None:
                await interaction.response.send_modal(CallsignChangeModal())
                await interaction.edit_original_response(view=InteractionMenuView())
                return
            
            else:
                await interaction.response.send_message(embed=discord.Embed(description="{} **You already have an open callsign update request!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), view=CallsignReturnView(), ephemeral=True)
                return
        