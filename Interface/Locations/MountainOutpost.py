import config
import discord

MountainOutpostEmbed = discord.Embed(
    title="Mountain Outpost",
    description="The Mountain Outpost, more commonly known as the Mountain, is a base on the peak of the western mountain on Ronograd Island. The Communications Tower appears to be a military communications center, distinguished by the radar domes and many tents dotting the base.\nThe Mountain Outpost is a raid location, controlled entirely by the PoD. Enemy soldiers spawn across the compound. There are no hostages at this location.\n\nPrevious renditions of the Communications Tower included a garage containing four enemy soldiers and a table holding four grey duffel bags. The garage opened once the Communications Tower was secured. The duffel bags were removed from the game at some point before Release 6.0.9; the only remnants of the system are the garage building which no longer opens, and the item exchange desk in the FOB, where the bags would be exchanged for money. This system will be revamped and is expected to return in later releases.",
    color=discord.Color.red()
).set_image(url=config.MOUNTAIN_OUTPOST_MAP_IMAGE)