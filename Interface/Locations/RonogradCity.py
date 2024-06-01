import config
import discord

RonogradCityEmbed = discord.Embed(
    title="Ronograd City",
    description="Ronograd City is a large city located on the eastern side of Ronograd Island. The city consists of an apartment complex currently overrun by the PoD and RLF, a park, and a medical center. The rest of the buildings in Ronograd City are abandoned, although, pockets of resistance can be found within the park and storage areas in the city, with the main stronghold being the multi-level apartment complex.",
    color=discord.Color.red()
).set_image(url=config.RONOGRAD_CITY_MAP_IMAGE)