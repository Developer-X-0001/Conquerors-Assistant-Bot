import config
import discord

ShorelineCampEmbed = discord.Embed(
    title="Shoreline Camp",
    description="The Shoreline Camp is a camp located on the east coast of Ronograd Island. The camp consists of two houses and a church. It houses multiple NPCs from the Russian Ground Forces and the Australian Army. It is the destination for a collect and deliver quest from Lieutenant Fedorov.",
    color=discord.Color.green()
).set_image(url=config.SHORELINE_CAMP_IMAGE)