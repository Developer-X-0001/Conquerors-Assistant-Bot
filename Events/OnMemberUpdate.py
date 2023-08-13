import config
import discord

from discord.ext import commands

class OnMemberUpdate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        verified_role = after.guild.get_role(config.VERIFIED_ROLE_ID)

        if verified_role not in before.roles and verified_role in after.roles:
            information_channel = after.guild.get_channel(config.INFORMATION_CHANNEL_ID)
            await information_channel.send(content=after.mention, delete_after=0)
        
        else:
            return

async def setup(bot: commands.Bot):
    await bot.add_cog(OnMemberUpdate(bot))