import config
import discord

QuarryEmbed = discord.Embed(
    title="Quarry",
    description="The Quarry is a mining quarry in east Ronograd Island. The Quarry appears to be a civilian mining operation.\nThe Quarry is a raid location, guarded entirely by the RLF with one or two PoD snipers. Several enemy soldiers spawn on the surface, but the majority can be found underground inside the mines. There are numerous hostages at the Quarry, several of which are mining, digging, or handling ammunition crates.\n\nSince Release 6.0.8.1, an extensive mineshaft has been added to the Quarry, where most enemies and hostages are located. The mineshaft mostly lacks light, especially in the tunnels, and it is too small and tight for vehicles to fit in. The mineshaft can be accessed by entering the hole at the bottom level of the quarry. Unfortunately, the elevator lifts located in and around the quarry are broken and do not move or respond to interactions.",
    color=discord.Color.red()
).set_image(url=config.QUARRY_MAP_IMAGE)