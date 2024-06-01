import config
import discord

CrashsiteEmbed = discord.Embed(
    title="Crash Site (Pushkino)",
    description="The Crash Site (referred to as \"Pushkino\" by signs ingame) is an apartment complex occupied by the RLF near Sochraina City. A crashed Black Hawk helicopter is located in the main courtyard. Several RLF riflemen occupy the apartment buildings and the surrounding area, with hostages held inside the buildings.\nDespite having a road sign that leads to it and a flag to signify its occupation by the RLF, it isn't tied with bunker raid progress. None of the RLF and their PoD reinforcements drop intel.",
    color=discord.Color.red()
).set_image(url=config.CRASHSITE_MAP_IMAGE)