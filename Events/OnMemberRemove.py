import config
import discord

from discord.ext import commands

class OnMemberRemoveEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        resignations_channel = member.guild.get_channel(config.RESIGNATIONS_CHANNEL_ID)
        await resignations_channel.send(content="{}#{} we hope you enjoyed your stay with us!".format(member.name, member.discriminator))

async def setup(bot: commands.Bot):
    await bot.add_cog(OnMemberRemoveEvent(bot))