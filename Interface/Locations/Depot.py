import config
import discord

DepotEmbed = discord.Embed(
    title="Depot",
    description="The Depot is a facility located on the southwestern side of Ronograd Island. It appears to be a complex of warehouses storing a variety of items, from crates to old tanks.\nThe Depot is a raid location, controlled primarily by the RLF with few PoD soldiers scattered around the complex. There are hostages kept inside the warehouses.",
    color=discord.Color.red()
).set_image(url=config.DEPOT_MAP_IMAGE)