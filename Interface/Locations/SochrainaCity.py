import config
import discord

SochrainaEmbed = discord.Embed(
    title="Sochraina City",
    description="Sometimes known as the \"Lighthouse Town\", Sochraina City is the second spawn location available to players. It is a small city located on the eastern end of Ronograd Island. It appears to be a traditional fishing town. Three primary points of interest inside this town are the food market in the center of the town, a lighthouse protruding out the rocky coast, and an enterable house in the southern part of the town, with the only remarkable thing about it being a covered hole in the ground. Sochraina City is the location of several NPCs and all quest giving NPCs.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_CITY_IMAGE)

SochrainaDetailedEmbed = discord.Embed(
    title="Sochraina City",
    description="Sometimes known as the \"Lighthouse Town\", Sochraina City is the second spawn location available to players. It is a small city located on the eastern end of Ronograd Island. It appears to be a traditional fishing town. Three primary points of interest inside this town are the food market in the center of the town, a lighthouse protruding out the rocky coast, and an enterable house in the southern part of the town, with the only remarkable thing about it being a covered hole in the ground. Sochraina City is the location of several NPCs and all quest giving NPCs.",
    color=discord.Color.green()
).add_field(
    name="__Administrative Region:__",
    value="Kamchatka Krai, Russian Federation",
    inline=False
).add_field(
    name="__Geography:__",
    value="**Location:** Bering Sea\n**Area:** 4,59 km²\n**Elevation:** 6,5ft (2m)\n**Timezones:** UTC+10:00",
    inline=False
).add_field(
    name="__Inhabitants:__",
    value="- Civilians\n- Australian Army\n- British Army\n- Delta Force\n- Russian Ground Forces",
    inline=False
).add_field(
    name="__Public Services__",
    value="Sochraina City doesn't have any public services available.",
    inline=False
).add_field(
    name="__Transportation:__",
    value="There is a bus stop in the Avenue; however, no buses are present in the city. This is presumably due to lack of demand as most civilians either use cars or walk.",
    inline=False
).add_field(
    name="__Economy:__",
    value="**1. Fishing:** Various boats can be seen next to the coffee shop. Their existence of the pier implies that the city is a naval hub.\n**2. Lodging:** Sochraina has an aforementioned inn owned by Isabel.\n**3. Trade:** A marketplace is present where most citizens buy or sell various products, mostly food. A coffee shop and a store owned by Zoyas are also present next to it, although the latter is closed indefinitely.",
    inline=False
).set_image(url=config.SOCHRAINA_CITY_IMAGE)

SochrainaPointOfInterests = [
    discord.SelectOption(label="Avenue", value=0),
    discord.SelectOption(label="Checkpoint 1", value=1),
    discord.SelectOption(label="Checkpoint 2", value=2),
    discord.SelectOption(label="Coffee Shop", value=3),
    discord.SelectOption(label="Isabel's Inn", value=4),
    discord.SelectOption(label="Lighthouse", value=5),
    discord.SelectOption(label="Marketplace", value=6),
    discord.SelectOption(label="Pier", value=7),
    discord.SelectOption(label="Waterfront", value=8),
]

SochrainaAvenueEmbed = discord.Embed(
    title="Sochraina City --> Avenue",
    description="The Avenue is located south of the Marketplace. Petro is present to the left of the Expensive Art Store. The Expensive Art Store has paintings in display. These paintings may be fan art.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_AVENUE_IMAGE)

SochrainaCheckpointOneEmbed = discord.Embed(
    title="Sochraina City --> Checkpoint 1",
    description="Checkpoint 1 is one of two locations players can spawn at in Sochraina City. A spawner for ground vehicles is located next to the tent the player spawns in and opposite the main entrance.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_CHECKPOINT_ONE_IMAGE)

SochrainaCheckpointTwoEmbed = discord.Embed(
    title="Sochraina City --> Checkpoint 2",
    description="Checkpoint 2 is one of two locations players can spawn at in Sochraina City. Two spawners for ground vehicles are located next to the Stryker. Corporal Nguyen is present in the tent opposite the one the player spawns in.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_CHECKPOINT_TWO_IMAGE)

SochrainaCoffeeShopEmbed = discord.Embed(
    title="Sochraina City --> Coffee Shop",
    description="The Coffee Shop is located east of the Marketplace. Sergeant Fedorov is present near the table with civilians and Russian soldiers.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_COFFEE_SHOP_IMAGE)

SochrainaIsabelInnEmbed = discord.Embed(
    title="Sochraina City --> Isabel's Inn",
    description="Isabel's Inn is located north of the Marketplace. Isabel is present near the table with the cash register and laptop.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_ISABELLS_INN_IMAGE)

SochrainaLighthouseEmbed = discord.Embed(
    title="Sochraina City --> Lighthouse",
    description="The Lighthouse is located east of the city atop a hill. It contains no interactable NPCs.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_LIGHTHOUSE_IMAGE)

SochrainaMarketplaceEmbed = discord.Embed(
    title="Sochraina City --> Marketplace",
    description="The Marketplace is located in the center of the city. It contains no interactable NPCs.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_MARKETPLACE_IMAGE)

SochrainaPierEmbed = discord.Embed(
    title="Sochraina City --> Pier",
    description="The Pier is located adjacent to the Waterfront. Captain Graham is present at the end of the jetty.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_PIER_IMAGE)

SochrainaWaterfrontEmbed = discord.Embed(
    title="Sochraina City --> Waterfront",
    description="The Waterfront encompasses most of the city's developed coastal areas. Two spawners for helicopters are located on the helipads. Major Quill is present under a green shelter past the line of refugees.",
    color=discord.Color.green()
).set_image(url=config.SOCHRAINA_WATERFRONT_IMAGE)