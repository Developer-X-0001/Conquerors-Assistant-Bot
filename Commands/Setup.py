import re
import config
import sqlite3
import discord
import asyncio

from discord.ext import commands
from config import RANKS, RANK_LIST
from Functions.Webhooks import sql_update
from Interface.ArmoryMenu import ArmoryMenuView
from Interface.SelfrolesMenu import SelfrolesMenuView
from Interface.HierarchyMenu import HierarchyMenuView
# from Interface.LocationsPanel import LocationsPanelView
from Interface.InformationButtons import InformationView
from Interface.InteractionMenu import InteractionMenuView
from Interface.InformationPanel import InformationPanelView

class test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = sqlite3.connect("./Databases/data.sqlite")

    @commands.command(name="add")
    @commands.is_owner()
    async def _add(self, ctx: commands.Context, msg_id: int, role_id: int, emoji_id: int):
        msg = await ctx.channel.fetch_message(msg_id)
        role = ctx.guild.get_role(role_id)
        for reaction in msg.reactions:
            if reaction.emoji.id == emoji_id:
                users = [user async for user in reaction.users()]

                for user in users:
                    await user.add_roles(role)
        
        await ctx.reply("Done")
    
    @commands.command(name="setup")
    @commands.is_owner()
    async def _setup(self, ctx: commands.Context, arg: str):
        if arg is None:
            await ctx.message.delete()
            return
            
        if arg == 'applications':
            embed = discord.Embed(
                title="TFC Application Information",
                description="Please use command **</apply:1116494588136398988>** in <#1115985929404944394>. And fill out the form accordingly.",
                color=config.TFC_GOLD
            )
            embed.add_field(
                name="{} Your Roblox username?".format(config.ARROW_EMOJI),
                value="```\nYour ROBLOX username will be filled automatically, you don't have to provide one.\n```",
                inline=False
            )
            embed.add_field(
                name="{} Where did you join from?".format(config.ARROW_EMOJI),
                value="```\nTell us how did you joined? Who invited you?\n```",
                inline=False
            )
            embed.add_field(
                name="{} Desired callsign?".format(config.ARROW_EMOJI),
                value="```\nWhat's your desired callsign? It must start and contain one capital letter. Also shouldn't contain a period/dash/space\n```",
                inline=False
            )
            embed.add_field(
                name="{} Most active time-zone?".format(config.ARROW_EMOJI),
                value="```\nWhat's your timezone in which you are mostly active?\n```",
                inline=False
            )
            embed.add_field(
                name="{} What are your expectations from us?".format(config.ARROW_EMOJI),
                value="```\nWhat do you expect in our faction that you would like to see? Must be 2-3 sentences long.\n```",
                inline=False
            )
            #embed.set_thumbnail(url=config.TFC_ICON)
            embed.set_image(url=config.APPLICATIONS_INFO_BANNER)
            embed.set_footer(text="Please be authentic when filling in the form.")

            await ctx.message.delete()
            await ctx.send(embed=embed, view=InformationView())
            return
        
        if arg == 'interactions':
            embed = discord.Embed(
                title="Task Force \"Conquerors\" Interaction Panel",
                description="""
                            The following services available at the moment:\
                            \n- Send LOA Request (Leave of Absence)\
                            \n- Request Promotion\
                            \n- Ask a Question\
                            \n- Check Points\
                            \n- Request Callsign Update
                            """,
                color=config.TFC_GOLD
            )
            embed.set_image(url=config.INTERACTION_PANEL_BANNER)
            embed.set_thumbnail(url=config.TFC_ICON)

            await ctx.message.delete()
            await ctx.send(embed=embed, view=InteractionMenuView())
            return
    
        if arg == 'armory':
            embed = discord.Embed(
                title="Task Force \"Conquerors\" Armory",
                description=f"""
                            ### __Here you can check your respective loadouts:__\
                            \n- {config.SENTINELS_EMOJI} 1COY | Sentinels Armory\
                            \n- {config.HAILSTORM_EMOJI} 2COY | Hailstorm Armory\
                            \n- {config.ORION_EMOJI} Recruits | Orion Armory\
                            """,
                color=config.TFC_GOLD
            )
            embed.set_image(url=config.ARMORY_BANNER)

            await ctx.message.delete()
            await ctx.send(embed=embed, view=ArmoryMenuView())
            return

        if arg == 'selfroles':
            embed = discord.Embed(
                title="Task Force \"Conquerors\" Self Roles",
                description="Here you can choose self-assignable roles to customize your experience in TFC.",
                color=config.TFC_GOLD
            )
            embed.add_field(
                name="Ping Roles:",
                value=f"""
                    - 🤝 Community Ping\
                    \n- 📢 Minor Announcement Ping\
                    \n- 🎲 Game Night Ping\
                    \n- {config.TFC_EMOJI} Faction Update Ping\
                    \n- 🤖 Bot Update Ping\
                    \n- <:robloxdev:1145404015954370691> ACS Update Ping\
                    """,
                inline=False
            )
            embed.set_image(url=config.SELFROLES_BANNER)

            await ctx.message.delete()
            await ctx.send(embed=embed, view=SelfrolesMenuView())
            return

        if arg == 'information':
            embed = discord.Embed(
                title="Task Force \"Conquerors\" Information Panel",
                description="Here you can get information about specific topics.",
                color=config.TFC_GOLD
            )
            embed.add_field(
                name="Following options are available at the moment:",
                value="- **Ranking Up**\n - Information about how to rank up and what are the requirements for each rank.\n- **Awards**\n - Information about honorary awards for our vigilant operators.\n- **Faction Advertisement:**\n - If you are a server booster at PL5, you can get information about TFC advertisement format.",
                inline=False
            )
            embed.set_image(url=config.INFORMATION_PANEL_BANNER)

            await ctx.message.delete()
            await ctx.send(embed=embed, view=InformationPanelView())
            return
        
        # if arg == 'locations':
        #     embed = discord.Embed(
        #         title="Task Force \"Conquerors\" Locations",
        #         description="# Locations\nLocations are the various points of interests found around Ronograd Island, the setting of the Openworld game mode. Though some locations are safe and quiet, most are controlled by the **Patriots of Democracy** and **Ronograd Liberation Front**, the primary antagonists of BRM5. Open world's gameplay is focused around attacking these locations, liberating them from the **PoD** and **RLF**'s control, and repelling enemy counterattacks.",
        #         color=config.TFC_GOLD
        #     )
        #     embed.add_field(
        #         name="__**Available Location Categories:**__",
        #         value="- Friendly (3)\n- Neutral (1)\n- Hostile (11)\n- Special (1)",
        #         inline=False
        #     )
        #     embed.set_image(url=config.LOCATIONS_BANNER)

        #     await ctx.message.delete()
        #     await ctx.send(embed=embed, view=LocationsPanelView())
        #     return

        if arg == 'hierarchy':
            leader_ranks = ""
            officer_ranks = ""
            wo_ranks = ""
            senior_enlisted_ranks = ""
            enlisted_ranks = ""

            rank_list = [i for i in RANK_LIST]
            rank_list.reverse()

            for rank in rank_list:
                role = ctx.guild.get_role(RANKS[rank]['role'])
                emoji = '' if not RANKS[rank]['emoji'] else RANKS[rank]['emoji']
                                
                if rank == 'O4' or rank == 'O5':
                    leader_ranks += f"{emoji} {role.mention}\n"
                
                if rank.startswith('O') and (rank != 'O4' and rank != 'O5'):
                    officer_ranks += f"{emoji} {role.mention}\n"
                
                if rank.startswith('W') or rank.startswith('C'):
                    wo_ranks += f"{emoji} {role.mention}\n"
                
                if rank.startswith('SE'):
                    senior_enlisted_ranks += f"{emoji} {role.mention}\n"
                                
                if rank.startswith('E'):
                    enlisted_ranks += f"{emoji} {role.mention}\n"

            embed = discord.Embed(
                title="Task Force \"Conquerors\" Hierarchy",
                description=f"### __Leaders:__\n{leader_ranks}### __Officers:__\n{officer_ranks}### __Warrant Officers__:\n{wo_ranks}### __Senior Enlisted:__\n{senior_enlisted_ranks}### __Enlisted:__\n{enlisted_ranks}",
                color=config.TFC_GOLD
            )
            embed.set_image(url=config.HIERARCHY_BANNER)

            await ctx.message.delete()
            await ctx.send(embed=embed, view=HierarchyMenuView())
            return

        else:
            await ctx.message.delete()
            return

    @commands.command(name="return_request")
    async def return_promotion_request(self, ctx: commands.Context, user: discord.Member):
        if user is None:
            return
    
        self.database.execute("DELETE FROM PromotionRequests WHERE user_id = ?", (user.id,)).connection.commit()

        await ctx.reply(f"Promotion request sent by **{user.name}** has been returned.")
        return
    
    @commands.command(name="register")
    @commands.is_owner()
    async def _register(self, ctx: commands.Context):
        # for user in ctx.guild.members:
        #     if user.nick:
        #         if '"' in user.nick:
        #             callsign = user.nick.split('"')[1]
        #             name = user.nick.split('"')[2][1:]
        #         else:
        #             callsign = user.nick.split(' ')[len(user.nick.split(' '))-1]
        #             name = None

        #         self.database.execute(
        #             """
        #                 INSERT INTO UserData (user_id, points, callsign, name)
        #                 VALUES (?, 0, ?, ?)
        #                 ON CONFLICT (user_id) DO UPDATE SET
        #                 callsign = ?, name = ? WHERE user_id = ?
        #             """,
        #             (
        #                 user.id,
        #                 callsign,
        #                 name,
        #                 callsign,
        #                 name,
        #                 user.id,
        #             )
        #         ).connection.commit()
        #         print(user.name, callsign, name)

        # data = self.database.execute("SELECT user_id FROM UserData").fetchall()
        # enlisted_role = ctx.guild.get_role(config.ENLISTED_ROLE_ID)
        # for entry in data:
        #     user = ctx.guild.get_member(int(entry[0]))
        #     if user is None:
        #         self.database.execute("DELETE FROM UserData WHERE user_id = ?", (entry[0],)).connection.commit()
            
        #     else:
        #         if enlisted_role in user.roles:
        #             pass
        #         else:
        #             self.database.execute("DELETE FROM UserData WHERE user_id = ?", (entry[0],)).connection.commit()

        for member in ctx.guild.members:
            for i in config.RANK_LIST:
                role = ctx.guild.get_role(config.RANKS[i]["role"])
                if role in member.roles:
                    self.database.execute("INSERT INTO UserData (user_id, rank) VALUES (?,? ) ON CONFLICT (user_id) DO UPDATE SET rank = ? WHERE user_id = ?", (member.id, i, i, member.id,)).connection.commit()
                    print("Updadted for {}".format(member.display_name))
                    await asyncio.sleep(0.75)

    @commands.command(name="ping")
    @commands.is_owner()
    async def _ping(self, ctx: commands.Context):
        await ctx.reply(content=f"📶 **Latency:** `{round(self.bot.latency * 1000)}`ms")

    @commands.command(name="test")
    @commands.is_owner()
    async def _test(self, ctx: commands.Context):
        await sql_update()
        await ctx.reply("Done")

async def setup(bot: commands.Bot):
    await bot.add_cog(test(bot))