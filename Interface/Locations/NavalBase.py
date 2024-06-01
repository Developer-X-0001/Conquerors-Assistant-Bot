import config
import discord

NavalBaseEmbed = discord.Embed(
    title="Naval Base",
    description="The Naval Base is located in the northeast Island. It appears to have been a former military base or port that was taken over by the PoD, as the base has two docking stations for ships (one of which is occupied by a Steregushchiy-class corvette), several shipping containers, and two cranes that supposedly load these containers onto ships.\nThe Naval Docks are a raid location, controlled entirely by the PoD. Dozens of enemy soldiers spawn within the base, with the majority on the uppermost level, stationed at either the tent zone near the entrance or at the containers. Enemies are also found guarding/patrolling the lower levels around the corvette and near the lower-level containers. Additionally, snipers can sometimes be found standing on the cranes or on the small watchtowers around the docks. There are no hostages at this location.\n\nThe Naval Docks are one of two locations that contain SAM Humvees. Two SAM Humvees are located in the tent area near the entrance, with multiple machine gun Humvees guarding the entrance.",
    color=discord.Color.red()
).set_image(url=config.NAVAL_BASE_MAP_IMAGE)