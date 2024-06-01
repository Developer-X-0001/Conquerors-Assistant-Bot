import config
import discord

DepotOutpostEmbed = discord.Embed(
    title="Depot Outpost",
    description="The Depot Outpost is a camp located on the road leading to the Depot. The outpost appears to be a makeshift military checkpoint. It's used to be an event location where you raid and steal enemy supplies using trucks or helicopters during Operation Viper. Since Release 6.2, it has become a location for the RLF to spawn during Direct Action quests.",
    color=discord.Color.red()
).set_image(url=config.DEPOT_OUTPOST_MAP_IMAGE)