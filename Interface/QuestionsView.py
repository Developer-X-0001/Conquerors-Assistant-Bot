import config
import discord

from discord import TextStyle, ButtonStyle
from discord.ui import Button, Modal, TextInput, View, button

class QuestionModal(Modal, title="Ask a Question"):
    def __init__(self):
        super().__init__(timeout=None)
    
    question = TextInput(
        label="Question:",
        placeholder="Please type your question here...",
        style=TextStyle.long,
        max_length=256,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        questions_channel = interaction.guild.get_channel(config.QUESTIONS_CHANNEL_ID)
        question = self.question.value

        embed = discord.Embed(
            title=question,
            color=config.TFC_GOLD
        )
        embed.set_author(
            name=f"Question by {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar.url
        )
        embed.add_field(
            name="Reply:",
            value="N/A",
            inline=False
        )
        embed.set_thumbnail(url=config.TFC_ICON)

        await questions_channel.send(content=interaction.user.mention, embed=embed, view=QuestionManageView())
        await interaction.response.send_message(embed=discord.Embed(description="{} Your question has been forwarded to {}".format(config.DONE_EMOJI, questions_channel.mention), color=config.TFC_GOLD), ephemeral=True)

class QuestionManageView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Reply", emoji=config.REPLY_EMOJI, style=ButtonStyle.gray, custom_id="question_reply_button")
    async def question_reply_btn(self, interaction: discord.Interaction, button: Button):
        community_management_role = interaction.guild.get_role(config.COMMUNITY_MANAGEMENT_ROLE_ID)
        if community_management_role in interaction.user.roles:
            current_reply = interaction.message.embeds[0].fields[0].value
            await interaction.response.send_modal(ReplyModal(original_view=self, old_reply=current_reply))

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return

    @button(label="Delete", emoji=config.DELETE_EMOJI, style=ButtonStyle.gray, custom_id="question_delete_button")
    async def question_delete_btn(self, interaction: discord.Interaction, button: Button):
        community_management_role = interaction.guild.get_role(config.COMMUNITY_MANAGEMENT_ROLE_ID)
        if community_management_role in interaction.user.roles:
            user = interaction.message.mentions[0]
            embed = interaction.message.embeds[0]
            await interaction.response.defer()
            await interaction.message.delete()

        else:
            await interaction.response.send_message(embed=discord.Embed(description="{} **You aren't authorized to do that!**".format(config.ERROR_EMOJI), color=config.TFC_GOLD), ephemeral=True)
            return

class ReplyModal(Modal, title="Add a Reply"):
    def __init__(self, original_view: QuestionManageView, old_reply: str):
        self.view = original_view
        super().__init__(timeout=None)
    
        self.reply = TextInput(
            label="Reply:",
            placeholder="Type a reply to this question...",
            style=TextStyle.long,
            required=True,
            default=old_reply,
            max_length=1024
        )

        self.add_item(self.reply)

    async def on_submit(self, interaction: discord.Interaction):
        user = interaction.message.mentions[0]
        embed = interaction.message.embeds[0]
        reply = self.reply.value

        embed.set_field_at(
            index=0,
            name="Reply:",
            value=reply,
            inline=False
        )

        self.view.question_reply_btn.label = "Edit Reply"
        self.view.question_reply_btn.emoji = config.EDIT_EMOJI

        await interaction.response.edit_message(embed=embed, view=self.view)

        try:
            dm_embed = discord.Embed(
                title="You have a new reply!",
                description=f"Your question [{embed.title}]({interaction.message.jump_url}) has been replied by {interaction.user.mention}",
                color=config.TFC_GOLD
            )
            dm_embed.set_thumbnail(url=config.TFC_ICON)

            await user.send(embed=dm_embed)
            return
        
        except:
            return
