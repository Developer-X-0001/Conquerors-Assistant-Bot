import config
import discord

m4a1_embed = discord.Embed(
    title="Rifles -> M4A1",
    description="*War is ever-changing, right Commander? This venerable American carbine is lightweight and versatile. Features stable firing characteristics and a full-auto trigger group.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value=f"**Class:** Carbine\n**Manufacturer:** Stallion Arms Manufacturing\n**Unlock Requirements:** None\n**Price:** {config.CREDITS_EMOJI} 1200",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 5.56x45mm NATO\n**Fire modes:** Auto/Semi\n**Magazine capacity:** 30, 40 (STANAG/ERMAG)\n**Ammo reserve:** 180, 160 (STANAG/ERMAG)\n**Rate of fire:** 750 rounds/minute\n**Recoil:** 41\n**Ergonomics:** 50\n**Reload (partial):** 1.27 seconds\n**Reload (empty):** 2.9 seconds\n**Mass (unloaded):** 3230 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2861 studs/second\n**Range:** 2472 studs\n**Spread:** 1.16 mrad",
    inline=False
).set_image(url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/8/8c/Image_firearm_carbine_m4a1.png")

mk18_embed = discord.Embed(
    title="Rifles -> Mk 18",
    description="*A shorter iteration of the M4A1 for use in close quarters. The redesigned upper receiver group features a shortened barrel and widened gas ports for reliable cycling.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value=f"**Class:** Carbine\n**Manufacturer:** Stallion Arms Manufacturing\n**Unlock Requirements:** None\n**Price:** {config.CREDITS_EMOJI} 4100",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 5.56x45mm NATO\n**Fire modes:** Auto/Semi\n**Magazine capacity:** 30, 40 (STANAG/ERMAG)\n**Ammo reserve:** 180, 160 (STANAG/ERMAG)\n**Rate of fire:** 820 rounds/minute\n**Recoil:** 41\n**Ergonomics:** 47\n**Reload (partial):** 1.27 seconds\n**Reload (empty):** 2.9 seconds\n**Mass (unloaded):** 3191 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2518 studs/second\n**Range:** 2117 studs\n**Spread:** undefined",
    inline=False
).set_image(url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/1/18/Image_firearm_carbine_mk18.png")

rf416a5_embed = discord.Embed(
    title="Rifles -> RF416 A5",
    description="*A lavish German assault rifle taking after the M4, utilizing a short-stroke gas piston to increase reliability and service life. After all, exceeding perfection is still perfection.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value=f"**Class:** Carbine\n**Manufacturer:** Rüstungsforschung\n**Unlock Requirements:** None\n**Price:** {config.CREDITS_EMOJI} 11000",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 5.56x45mm NATO\n**Fire modes:** Auto/Semi\n**Magazine capacity:** 30 (Maritime/PolyMag)\n**Ammo reserve:** 180 (Maritime/PolyMag)\n**Rate of fire:** 850 rounds/minute\n**Recoil:** 44\n**Ergonomics:** 46\n**Reload (partial):** 1.55 seconds\n**Reload (empty):** 2.37 seconds\n**Mass (unloaded):** 3731 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2523 studs/second\n**Range:** 2128 studs\n**Spread:** undefined",
    inline=False
).set_image(url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/d/d6/Image_firearm_carbine_dwf416a5.png")

scarh_embed = discord.Embed(
    title="Rifles -> SCAR-H",
    description="*An advanced Belgian design, developed in response to USSOCOM's desire for a modular weapons system. This variant is chambered for the full-power 7.62x51mm NATO cartridge, hence its 'heavy' designation.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value=f"**Class:** Battle rifle\n**Manufacturer:** Atelier Armes Légères\n**Unlock Requirements:** None\n**Price:** {config.CREDITS_EMOJI} 3950",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 7.62x51mm NATO\n**Fire modes:** Auto/Semi\n**Magazine capacity:** 20 (Magazine)\n**Ammo reserve:** 120 (Magazine)\n**Rate of fire:** 600 rounds/minute\n**Recoil:** 59\n**Ergonomics:** 38\n**Reload (partial):** 1.62 seconds\n**Reload (empty):** 2.62 seconds\n**Mass (unloaded):** 3775 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2624 studs/second\n**Range:** 2936 studs\n**Spread:** 0.47 mrad",
    inline=False
).set_image(url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/f/f0/Image_firearm_battlerifle_scar-h.png")

scarl_embed = discord.Embed(
    title="Rifles -> SCAR-L",
    description="*A modular assault rifle originally slated to replace various AR-pattern weapons in USSOCOM's inventory. The SCAR-L has since found service worldwide in the hands of several elite units.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value=f"**Class:** Assault rifle\n**Manufacturer:** Atelier Armes Légères\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 3600",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 5.56x45mm NATO\n**Fire modes:** Auto/Semi\n**Magazine capacity:** 30 (Magazine/ERMAG)\n**Ammo reserve:** 180 (Magazine/ERMAG)\n**Rate of fire:** 625 rounds/minute\n**Recoil:** 42\n**Ergonomics:** 45\n**Reload (partial):** 1.62 seconds\n**Reload (empty):** 2.62 seconds\n**Mass (unloaded):** 2909 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2808 studs/second\n**Range:** 2911 studs\n**Spread:** 1.10 mrad",
    inline=False
).set_image(url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/b/bf/Image_firearm_assaultrifle_scar-l.png")

