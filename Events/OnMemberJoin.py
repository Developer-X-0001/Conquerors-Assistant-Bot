import config
import discord

from discord.ext import commands

class OnMemberJoinEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        for id in config.WELCOME_ROLE_IDS:
            role = member.guild.get_role(id)
            await member.add_roles(role)

async def setup(bot: commands.Bot):
    await bot.add_cog(OnMemberJoinEvent(bot))