import config
import discord

from discord.ext import commands
from Functions.GenerateRankCard import generate_rank_card

class OnMemberJoinEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        arrivals_channel = member.guild.get_channel(config.ARRIVALS_CHANNEL_ID)
        await arrivals_channel.send(content=f"Welcome {member.mention},\nto **Task Force \"Conquerors\"** {config.TFC_EMOJI}!\nGo check out the applications category so you can fully access the server!".format(member.mention), file=generate_rank_card(user=member))
        for id in config.WELCOME_ROLE_IDS:
            try:
                role = member.guild.get_role(id)
                await member.add_roles(role)
            except:
                pass

async def setup(bot: commands.Bot):
    await bot.add_cog(OnMemberJoinEvent(bot))