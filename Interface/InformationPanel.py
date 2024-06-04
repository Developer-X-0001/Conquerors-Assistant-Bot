import config
import discord

from discord import ButtonStyle
from config import RANKS, RANK_LIST
from discord.ui import View, Button, button

class InformationPanelView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Ranking Up", emoji=config.PROMOTION_EMOJI, style=ButtonStyle.gray, custom_id="ranking_up_btn")
    async def ranking_up_btn(self, interaction: discord.Interaction, button: Button):
        enlisted_ranks = "### __Enlisted__\n"
        senior_enlisted_ranks = "### __Senior Enlisted__\n"
        wo_ranks = "### __Warrant Officers__\n"
        officer_ranks = "### __Commissioned Officers__\n"

        for rank in RANK_LIST:
            if rank.startswith('E'):
                rank_name = RANKS[rank]['name']
                requirement = RANKS[rank]['requirement']
                enlisted_ranks += f"- **{rank}** | {rank_name} = {requirement}\n"
                
                
            if rank.startswith('SE'):
                rank_name = RANKS[rank]['name']
                requirement = RANKS[rank]['requirement']
                senior_enlisted_ranks += f"- **{rank}** | {rank_name} = {requirement}\n"
                
            if rank.startswith('W') or rank.startswith('CW'):
                rank_name = RANKS[rank]['name']
                requirement = RANKS[rank]['requirement']

                wo_ranks += f"- **{rank}** | {rank_name} = {requirement}\n"
            
            if rank.startswith('O'):
                rank_name = RANKS[rank]['name']
                requirement = RANKS[rank]['requirement']

                officer_ranks += f"- **{rank}** | {rank_name} = {requirement}\n"

        embed = discord.Embed(
            title="Task Force \"Conquerors\" Rank-Up Conditions",
            description=f"## Points System\n\n**__Operations:__**\n2 points = 1 hour\n3 points = 2 hours\n4 points = 3 hours\n\n**__Planned/Joint Operations:__**\n4 points = 1 hour\n6 points = 2 hours\n8 points = 3 hours\n\n**__Board Process (Steps):__**\n1. Receive Recommendations from NCO's (ranks SE4 - SE6).\n2. An SE6 will determine Yes or No.\n3. A board of SE8's and SE9's will interview you and vote. 2/3 majority 'yes' means you get to proceed.\n4. Evaluation and or Enrollment into NCOA.\n\n{enlisted_ranks}{senior_enlisted_ranks}{wo_ranks}{officer_ranks}",
            color=config.TFC_GOLD
        )
        embed.set_image(url=config.RANKING_UP_BANNER)

        await interaction.response.send_message(embed=embed, ephemeral=True)

    @button(label="Awards", emoji=config.POINTS_EMOJI, style=ButtonStyle.gray, custom_id="awards_btn")
    async def awards_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Task Force \"Conquerors\" Honorary Awards",
            description="## **Medals:**\n- **[ Fallen Angel Medal ]**\nAwarded to those who sacrificed themselves and stayed behind to make sure the rest of the team could make it out alive from a hot zone and get evacuated safely.\n\n- **[ Spotlight Medal ]**\nAwarded to those who disobeyed orders from their squad leader even when they were told to do what they ordered to make sure the right thing was done instead of following the act of an order that may cause a fatal casualty loss of innocent people or comrades when they can be saved.\n\n- **[ Guardian Angel Medal ]**\nAwarded to those who put their lives on the line to go and save their comrades and innocent people that were in immediate danger and at risk of dying. \n\n- **[ All or Nothing Medal ]**\nAwarded to squad leaders that had to make a difficult decision that could risk losing a lot of men to complete the operation and making sure to pick the best option to lose the least amount of soldiers in their team.\n\n- **[ No Challenge Medal ]**\nAwarded to squad leaders that commanded and kept the team under control with perfection, not losing a single man, and completed operations with no problem at all.\n\n- **[ Team Player Medal ]**\nAwarded to those that have exceptional skills out on the field and performing the best out of the whole team without getting downed or dying in any of the operations.\n\n- **[ Still Standing Medal ]**\nAwarded to those that make it through very difficult operations alive that had a high casualty rating on the location they were operating in\n\n- **[ Chosen One Medal ]**\nAwarded to those as the last one alive in an operation, completed the mission, and was the only one that returned home safely\n## **Ribbons:**\n- **[ Rising Star Ribbon]**\nGiven to members who have been very active in both discord and in-game for a few days\n\n- **[ Problem Solved Ribbon]**\nGiven to members who have helped out around the server by reporting errors in role commands, making bots for us, organizing the server better, and helping with documents\n\n- **[ Family Ribbon ]**\nGiven to members who helped us gain more members by going in-game and advertising or going to the BRM5 server and advertising for us",
            color=config.TFC_GOLD
        )
        embed.set_image(url=config.HONORARY_AWARDS_BANNER)

        await interaction.response.send_message(embed=embed, ephemeral=True)

    @button(label="Advertisement", emoji=config.ADVERT_EMOJI, style=ButtonStyle.gray, custom_id="advert_btn")
    async def advert_btn(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Task Force \"Conquerors\" Advertisement",
            description=f"**[Nitro Subscribers Only]** By posting our ad in <#594055313024483329> , you'll be helping us become a more bigger faction.\n\n\
                        **Google Document:**\n\
                        [Nitro Subscribers Advertisement Text](https://docs.google.com/document/d/1iHZfRJfsjofVvA9NvVAptJepzUVoJk51MHA4RzLLL2g/edit?usp=sharing)\n\n\
                        **Copyable Message:**\n\
                        ```\n{config.TFC_ADVERT}\n```",
            color=config.TFC_GOLD
        )
        embed.set_image(url=config.ADVERTISEMENT_BANNER)

        await interaction.response.send_message(embed=embed, ephemeral=True)