import config
import discord

VillageEmbed = discord.Embed(
    title="Village",
    description="The Village is a rural residential area located near the center of Ronograd Island on a dirt road that leads to the Department of Utilities. The Village appears to be a typical sparsely-populated rural village with some parked vehicles, short walls, some dotted watchtowers, and a small military camp to the east of the village.\nThe Village is a raid location, guarded entirely by the RLF with one or two PoD snipers. Enemy soldiers spawned in various locations around the Village guarding roads and looking over the hostages working in the wheat fields. Enemy snipers could occasionally be found in the watchtowers, and it isn't uncommon to find enemies hiding in houses and tents.",
    color=discord.Color.red()
).set_image(url=config.VILLAGE_MAP_IMAGE)