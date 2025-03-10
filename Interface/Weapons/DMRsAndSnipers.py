import config
import discord

m110_embed = discord.Embed(
    title="DMR's & Snipers -> M110",
    description="*Employed primarily by the U.S. Army, the M110's semi-automatic precision fire increases opportunities for snipers in urban environments. Sports ambidextrous controls and a tan color scheme.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value="**Class:** \nDesignated marksman rifle\n**Manufacturer:** \nSword & Shield Armament\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 8500",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 7.62X51mm NATO\n**Fire modes:** Semi\n**Magazine capacity:** 10, 20 (OEM/ERMAG)\n**Ammo reserve:** 130, 120 (OEM/ERMAG)\n**Rate of fire:** 600 rounds/minute\n**Recoil:** 75\n**Ergonomics:** Undefined\n**Reload (partial):** 3.20 seconds\n**Reload (empty):** 4.11 seconds\n**Mass (unloaded):** 5100 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2695 studs/second\n**Range:** 2167 studs\n**Spread:** Undefined",
    inline=False
).set_image(
    url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/1/13/Image_firearm_designatedmarksmanrifle_m110sass.png"
)

m2010_embed = discord.Embed(
    title="DMR's & Snipers -> M2010",
    description="*The M24's inexorable successor, adopted by the United States Army. Capable rifle cartridges grant superior performance through increased precision and effective range.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value="**Class:** Sniper rifle\n**Manufacturer:** American Arms Factory\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 17000",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** .300 Winchester Magnum\n**Fire modes:** Semi (bolt-action)\n**Magazine capacity:** 5, 7 (Magazine)\n**Ammo reserve:** 40, 35 (Magazine)\n**Rate of fire:** 40 rounds/minute\n**Recoil:** 70\n**Ergonomics:** 26\n**Reload (partial):** 2.63 seconds\n**Reload (empty):** 4.63 seconds\n**Mass (unloaded):** 5425 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2844 studs/second\n**Range:** 3951 studs\n**Spread:** 0.26 mrad",
    inline=False
).set_image(
    url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/9/92/Image_firearm_sniperrifle_m2010.png"
)

m24_embed = discord.Embed(
    title="DMR's & Snipers -> M24",
    description="*A straightforward bolt-action sniper rifle. Chambered in the full-power 7.62x51mm NATO cartridge, the M24 exhibits competitive ballistic performance at extended ranges.*",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value="**Class:** Sniper rifle\n**Manufacturer:** American Arms Factory\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 3600",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** 7.62x51mm NATO\n**Fire modes:** Semi (bolt-action)\n**Magazine capacity:** 5 (Internal/External)\n**Ammo reserve:** 40 (Internal/External)\n**Rate of fire:** 45 rounds/minute\n**Recoil:** 50\n**Ergonomics:** 25\n**Reload (partial):**\n- 2.53 seconds (Internal)\n - +0.76 seconds/round\n- 1.52 seconds (External)\n**Reload (empty):**\n- 6.33 seconds (Internal)\n- 2.57 seconds (External)\n**Mass (unloaded):** 5384 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2733 studs/second\n**Range:** 3055 studs\n**Spread:** 0.11 mrad",
    inline=False
).set_image(
    url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/a/ab/Image_firearm_sniperrifle_m24.png"
)

awm_embed = discord.Embed(
    title="DMR's & Snipers -> AWM",
    color=config.TFC_GOLD
).add_field(
    name="__Overview:__",
    value="**Class:** Sniper rifle\n**Manufacturer:** Portsmouth Practical Precision Instruments\n**Unlock Requirements:** None\n**Price:** <:credits:1289334042763853887> 7500",
    inline=False
).add_field(
    name="__Specifications:__",
    value="**Cartridge:** .338 LM\n**Fire modes:** Semi (bolt-action)\n**Magazine capacity:** 5 (OEM)\n**Ammo reserve:** 40 (OEM)\n**Rate of fire:** 34.4 rounds/minute\n**Recoil:** 78\n**Ergonomics:** 24\n**Reload (partial):** 3.54 seconds\n**Reload (empty):** 5.53 seconds\n**Mass (unloaded):** 5470 grams",
    inline=False
).add_field(
    name="__Ballistics:__",
    value="**Projectiles:** 1\n**Muzzle velocity:** 2876.4 studs/second\n**Range:** 4759 studs\n**Spread:** 0.22 mrad",
    inline=False
).set_image(
    url="https://static.wikia.nocookie.net/roblox-blackhawk-rescue-mission-5/images/2/21/Image_firearm_sniperrifle_awm.png"
)