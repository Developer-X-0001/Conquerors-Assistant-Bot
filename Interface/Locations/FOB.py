import config
import discord

FOBEmbed = discord.Embed(
    title="Forward Operating Base (FOB)",
    description="The FOB, or Forward Operating Base, is located at the very south of Ronograd Island. It acts as a main hub and is one of three spawn locations where players may spawn in, resupply on ammunition and medical supplies, spawn in vehicles, and bring hostages. This is the only base in which the A-10 can be spawned in, due to it having the only airfield in the map.",
    color=discord.Color.green()
).set_image(url=None)

FOBDetailedEmbed = discord.Embed(
    title="Forward Operating Base (FOB)",
    description="The FOB, or Forward Operating Base, is located at the very south of Ronograd Island. It acts as a main hub and is one of three spawn locations where players may spawn in, resupply on ammunition and medical supplies, spawn in vehicles, and bring hostages. This is the only base in which the A-10 can be spawned in, due to it having the only airfield in the map.",
    color=discord.Color.green()
).add_field(
    name="__Points of Interest:__",
    value="- The Command Center\n2. Vehicle Depot\n3. Helicopter Landing Zone\n4. Hangars\n5. Killhouse\n6. Vehicle Workshop\n7. Shooting Range\n8. Runway\n9. Refugee Processing Camps",
    inline=False
).set_image(url=None)

FOBPointOfInterests = [
    discord.SelectOption(label="The Command Center", value=0),
    discord.SelectOption(label="Vehicle Depot", value=1),
    discord.SelectOption(label="Helicopter Landing Zone", value=2),
    discord.SelectOption(label="Hangars", value=3),
    discord.SelectOption(label="Killhouse", value=4),
    discord.SelectOption(label="Vehicle Workshop", value=5),
    discord.SelectOption(label="Shooting Range", value=6),
    discord.SelectOption(label="Runway", value=7),
    discord.SelectOption(label="Refugee Processing Camps", value=8),
]

FOBCommandCenterEmbed = discord.Embed(
    title="FOB --> The Command Center",
    description="This is where players spawn and can refill their ammunition, utilities, and medical supplies in the Supply Area, as well as access the main menu. It is also home to the Requisitions Area and Briefing Room. The Requisitions Area serves as a place where players can hand in Intel. The Briefing Room has a projector and multiple chairs; groups often use this room to plan missions. The projector is non-interactable.",
    color=discord.Color.green()
)

FOBVehicleDepotEmbed = discord.Embed(
    title="FOB --> Vehicle Depot",
    description="This is where players may spawn their ground vehicles. The Vehicle Depot has 10 sheds, each with an interface that players may interact with to spawn, buy, repair, or sell a ground vehicle.",
    color=discord.Color.green()
)

FOBHelicopterLandingZoneEmbed = discord.Embed(
    title="FOB --> Helicopter Landing Zone",
    description="This is where players may spawn their helicopters. Each pad has an interface that players may interact with to spawn, buy, repair, or sell a helicopter. There are three such pads. An NPC can be seen outside guarding the area.",
    color=discord.Color.green()
)

FOBHangarsEmbed = discord.Embed(
    title="FOB --> Hangars",
    description="This is where fixed wing aircraft, such as the A-10, can be spawned. There are 2 Hangars and both are connected to the runway.",
    color=discord.Color.green()
)

FOBKillhouseEmbed = discord.Embed(
    title="FOB --> Killhouse",
    description="The Killhouse is a training area where players may hone their close-quarter combat skills. It features a series of wooden rooms with targets and a timer which can be operated using a button at the entrance. Multiple metal catwalks overlook the various rooms.",
    color=discord.Color.green()
)

FOBVehicleWorkshopEmbed = discord.Embed(
    title="FOB --> Vehicle Workshop",
    description="The vehicle workshop is a large building with multiple parking spaces for ground vehicles. There is an NPC standing in it. As of now, it has no purpose.",
    color=discord.Color.green()
)

FOBShootingRangeEmbed = discord.Embed(
    title="FOB --> Shooting Range",
    description="The shooting range allows players to practice their accuracy and recoil control. It has several targets with varying ranges.",
    color=discord.Color.green()
)

FOBRunwayEmbed = discord.Embed(
    title="FOB --> Runway",
    description="This is where fixed-wing aircraft, such as the A-10, may take off from or land on. There are 2 runways labeled \"36R\" and \"36L\" and is found respectively to the right and left of each other.",
    color=discord.Color.green()
)

FOBRefugeeProcessingCampEmbed = discord.Embed(
    title="FOB --> Refugee Processing Camps",
    description="This is where players can transport hostages to for Cash rewards and refill ammo and medical supplies. There are multiple NPCs within and around the camps.",
    color=discord.Color.green()
)