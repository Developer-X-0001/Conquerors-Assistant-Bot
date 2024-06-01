import config
import discord

BunkerEmbed = discord.Embed(
    title="Bunker",
    description="The Bunker is a hostile special location that houses a nuclear/biological weapon in an adjacent missile silo, which is part of the complex. It is only open for a short period of time after specific requirements are met. It is the most heavily fortified location on Ronograd island, even more so than the Fort or Naval Docks.",
    color=discord.Color.blurple()
).set_image(url=config.BUNKER_IMAGE)

BunkerAccessEmbed = discord.Embed(
    title="Bunker -> Access",
    description="The Bunker is sealed by a pair of heavy metal doors. To open the Bunker, players will have to collect Intel items from various locations around the map. Once adequate Intel has been acquired, every player will get a notification informing them that the Bunker will open in five minutes. Once the gate opens, it will stay open for another five minutes. After that, players who didn't make it inside will be unable to enter. Additionally, players who die during the raid will not be able to rejoin.\n\nThe criteria to access the Bunker:\n- 5 or more Intel from **Depot**\n- 8 or more Intel from **Department of Utilities**\n- 8 or more Intel from **Ronograd City**\n- 8 or more Intel from **Quarry**\n- 8 or more Intel from **Village**\n- 10 or more Intel from **Mountain Outpost**\n- 10 or more Intel from **Naval Base**\n- 15 or more Intel from **Fort Ronograd**",
    color=discord.Color.blurple()
).set_image(url=config.INTELBOARD_IMAGE)

BunkerLayoutEmbed = discord.Embed(
    title="Bunker -> Layout",
    description="",
    color=discord.Color.blurple()
).add_field(
    name="__Entrance__",
    value="The entrance to the Bunker is revealed to players upon the Bunker opening. There are a few enemies that appear from the sides.",
    inline=False
).add_field(
    name="__Floor 1__",
    value="Floor 1 consists of four chambers each sealed by massive doors. PoD combatants of all kinds are found inside and occupy multiple floors overseeing the entrance. The doors can be opened by pushing buttons located in each room. The final door must be opened by sabotaging three power consoles.\n\nPast the four chambers is a long corridor. Players can replenish their medical supplies (Bandages and Dressings only) and ammo at the beginning of the corridor. Two trucks present a roadblock which forces the players to abandon their vehicles and continue on foot. At the end of the corridor is a service elevator that takes the players to the next floor. Prior to entering, players can replenish their ammo at the ammo crate located nearby.",
    inline=False
).add_field(
    name="__Floor 2__",
    value="Floor 2 is reached by the service elevator and covers most of the actual missile silo. Enemies on this floor come in greater numbers and more dangerous forms relative to the previous. After clearing all rooms and ascending a staircase, the players will reach two elevators to proceed to the third and final floor.",
    inline=False
).add_field(
    name="__Floor 3__",
    value="Floor 3 is the darkest floor in the raid and is noticeably better maintained than the previous two, featuring proper furniture and clean rooms. Most of the enemies on this floor are PoD Spec Ops, with the remainder being Marksmen. After clearing all of the hallways and rooms, players reach the command center where the missile is launched from. Players must find two launch keys and eliminate all enemies before deactivating the missile. Once both keys are found and the console is used, the missile is deactivated and the raid ends.",
    inline=False
)

BunkerMissionEmbed = discord.Embed(
    title="Bunker -> Mission",
    description="Once the entrance closes, every player present inside the Bunker will be given 30 minutes to stop the missile launch. Players will be tasked with opening several gates which will lead into the deepest parts of the bunker. When the players reach the final area, they will be tasked with finding two keys that will be used to stop the missile launch. Before the keys can be used, all enemies in the area must be eliminated.",
    color=discord.Color.blurple()
).add_field(
    name="__Success__",
    value="If the missile launch is successfully stopped in time, every player alive inside the Bunker will be given the It's **Not Over** badge, $3000, and 1000 EXP and will be shown a cutscene of the silo door opening and closing, followed by a credits roll showing various locations on the map and the names of the development team. Following the cutscene, players will be prompted with the spawn menu and have the option to respawn.",
    inline=False
).add_field(
    name="__Failure__",
    value="If the launch is not stopped in time, every player involved in the event, regardless of whether they're dead or alive, will be given the **Lost Souls** badge. Everyone still alive in the Bunker will be notified that the mission has failed and will be teleported back to their spawns. The badge is not exclusive to the mission failing; the badge can be acquired if the player dies or reset character during the mission.",
    inline=False
)
