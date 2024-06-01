import config
import discord

DOUEmbed = discord.Embed(
    title="Department of Utilities (D.O.U)",
    description="The Department of Utilities, also known as the Power Plant, is a facility and complex located on the northwestern end of the temperate portions of Ronograd Island. The Department of Utilities appears to be a government-operated nuclear power plant tasked with power generation for Ronograd Island.\nThe Department of Utilities is a raid location, controlled primarily by the RLF with few PoD Advanced guarding the main building's entrance at the front of the flag. Enemy soldiers spawn scattered around the large complex, with snipers occasionally spawning on the roof of buildings. There are hostages at the main power grid and around the main attraction (the indoor flag). Beware of the maze of catwalks and stairways that hide enemies at every turn.",
    color=discord.Color.red()
).set_image(url=config.DOU_MAP_IMAGE)