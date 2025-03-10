import config
import sqlite3
import discord
import datetime

from discord.ext import commands, tasks

class CheckLOAs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = sqlite3.connect("./Databases/data.sqlite")
        self.check_loa.start()

    @tasks.loop(minutes=1)
    async def check_loa(self):
        await self.bot.wait_until_ready()
        data = self.database.execute("SELECT user_id, ending_time FROM UserLOAs").fetchall()
        guild = self.bot.get_guild(config.GUILD_ID)
        loa_role = guild.get_role(config.LOA_ROLE_ID)
        on_topic_channel = guild.get_channel(config.ON_TOPIC_CHANNEL_ID)

        if data != []:
            for entry in data:
                user = guild.get_member(int(entry[0]))
                if user:
                    ending_time = int(entry[1])
                    current_time = round(datetime.datetime.now().timestamp())

                    if current_time > ending_time:
                        await user.remove_roles(loa_role)
                        await on_topic_channel.send(content=user.mention, embed=discord.Embed(description="Welcome back! Your return is a delight. We're eager to resume teamwork and make progress together. If you need to catch up or share updates, feel free to connect. Here's to a productive time ahead!", color=config.TFC_GOLD).set_image(url=config.TFC_BANNER))
                        self.database.execute("DELETE FROM UserLOAs WHERE user_id = ?", (user.id,)).connection.commit()

async def setup(bot: commands.Bot):
    await bot.add_cog(CheckLOAs(bot))