import config
import discord

KPsHouseEmbed = discord.Embed(
    title="K.P's House",
    description="K.P.'s House is a house located east of the Village on a small hill. As its name implies, it is the residence of the currently removed, friendly NPC K.P., who could be seen sitting outside. The house does not appear to be affected by the ongoing conflict, despite being in close proximity to the contested Village.\nDue to K.P.'s removal with the Operation Resurgence update, the badge is currently unobtainable. Since Release 6.2, it has become a drop-off area in Collect and Deliver quests along with the Forest House.",
    color=discord.Color.light_gray()
).set_image(url=config.KP_HOUSE_IMAGE)