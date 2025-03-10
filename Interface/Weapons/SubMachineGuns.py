import config
import discord

mp5_embed = discord.Embed(
    title="Sub-Machine Guns -> MP5",
    description="*A roller-delayed submachine gun ubiquitous in the hands of CT units. Compact and immensely popular, the MP5 is by all accounts the quintessential submachine gun. How'd a muppet like you pass Selection?*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value="**Class:** Submachine gun\n**Manufacturer:** Deutsche Waffen und Forschung\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 2100",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 9x19mm Parabellum\n**Fire modes:** Auto/Burst/Semi\n**Magazine capacity:** 30 (Magazine)\n**Ammo reserve:** 240 (Magazine)\n**Rate of fire:** 800 rounds/minute\n**Recoil:** 35\n**Ergonomics:** 50\n**Reload (partial):** 1.7 seconds\n**Reload (empty):** 2.83 seconds\n**Mass (unloaded):** 2400 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 1343 studs/second\n**Range:** 606 studs\n**Spread:** 1.59 mrad",
    inline=False
).set_image(
    url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/3/36/Image_firearm_submachinegun_mp5.png"
)

mp7_embed = discord.Embed(
    title="Sub-Machine Guns -> MP7",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value="**Class:** Submachine gun\n**Manufacturer:** Deutsche Waffen und Forschung\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 2400",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 4.6x30mm\n**Fire modes:** Auto/Semi\n**Magazine capacity:** 30, 40 (OEM)\n**Ammo reserve:** 300, 320 (OEM)\n**Rate of fire:** 950 rounds/minute\n**Recoil:** 25\n**Ergonomics:** 62\n**Reload (partial):** 1.92 seconds\n**Reload (empty):** 2.67 seconds\n**Mass (unloaded):** 1150 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2037 studs/second\n**Range:** 1055 studs\n**Spread:** 1.31 mrad",
    inline=False
).set_image(
    url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/1/19/Image_firearm_personaldefenseweapon_mp7.png"
)

ump45_embed = discord.Embed(
    title="Sub-Machine Guns -> UMP45",
    description="*Luck doesn't live on this side of the border. This polymer-bodied submachine gun is optimized for the .45 Auto cartridge. Being a successor to the MP5, someone clearly has a lot to live up to.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value="**Class:** Submachine gun\n**Manufacturer:** Rostungforchung\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 1700",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** .45 Auto\n**Fire modes:** Auto/Semi\n**Magazine capacity:** 25 (Magazine)\n**Ammo reserve:** 200 (Magazine)\n**Rate of fire:** 600 rounds/minute\n**Recoil:** 39\n**Ergonomics:** 51\n**Reload (partial):** 1.85 seconds\n**Reload (empty):** 2.08 seconds\n**Mass (unloaded):** 2325 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 940 studs/second\n**Range:** 822 studs\n**Spread:** 4.79 mrad",
    inline=False
).set_image(
    url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/d/d0/Image_firearm_submachinegun_ump45.png"
).set_footer(
    text="The Ballistics information on the wiki isn't accurate, we had to manually check in the game for values."
)
