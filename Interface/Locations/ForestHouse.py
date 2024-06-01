import config
import discord

ForestHouseEmbed = discord.Embed(
    title="Forest House",
    description="The Forest House is a house located in the forest near the Quarry that serves as a drop-off location in Collect and Deliver quests. Since Release 6.6, RLF insurgents sometimes spawn in and around the location along with hostages.",
    color=discord.Color.red()
).set_image(url=config.FOREST_HOUSE_IMAGE)