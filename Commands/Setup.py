import re
import discord
import config

from discord.ext import commands
from Interface.InformationPanel import InformationPanelView
from Interface.InteractionMenu import InteractionMenuView
from Interface.InformationButtons import InformationView
from Interface.HierarchyMenu import HierarchyMenuView
from Interface.SelfrolesMenu import SelfrolesMenuView
from Interface.ArmoryMenu import ArmoryMenuView

class test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="get")
    async def get(self, ctx: commands.Context):
        counter = 1
        async for message in ctx.channel.history(limit=None):
            if message.mentions != []:
                pattern = r'Entry: #\d{4}'

                # Search for the pattern in the message content
                match = re.search(pattern, message.content)

                if match:
                    extracted_part = match.group()
                    print(counter, message.author.display_name, extracted_part)
                    counter += 1
    
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
                value="```\nWhat's your desired callsign? It must consists on only one word without any spaces.\n```",
                inline=False
            )
            embed.add_field(
                name="{} Most active time-zone?".format(config.ARROW_EMOJI),
                value="```\nWhat's your timezone in which you are mostly active?\n```",
                inline=False
            )
            embed.add_field(
                name="{} Do you understand the rules that are inplace, and do you understand that breaking them will lead to punishments at the discretion of officers?".format(config.ARROW_EMOJI),
                value="```\nSimply reply with Y or N, no need to put any random alphabets in there.\n```",
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
                            \n- Check Points
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

        if arg == 'information':
            embed = discord.Embed(
                title="Task Force \"Conquerors\" Information Panel",
                description="Here you can get information about specific topics.",
                color=config.TFC_GOLD
            )
            embed.add_field(
                name="Following options are available at the moment:",
                value="- **Awards**\n - Information about honorary awards for our vigilant operators.\n- **Faction Advertisement:**\n - If you are a server booster at PL5, you can get information about TFC advertisement format.",
                inline=False
            )
            # - **Ranking Up**\n - Information about how to rank up and rank requirements.\n
            embed.set_image(url=config.INFORMATION_PANEL_BANNER)

            await ctx.message.delete()
            await ctx.send(embed=embed, view=InformationPanelView())

        if arg == 'hierarchy':
            embed = discord.Embed(
                title="Task Force \"Conquerors\" Hierarchy",
                description="### __Leaders:__\n<:MajorGeneral:1144618939884765325> <@&1115990476575748137> \n<:BrigadierGeneral:1144618902278651994> <@&1115990540618584116> \n### __Officers:__\n<:Colonel:1144618914484072620> <@&1116021943469096970> \n<:LieutenantColonel:1144618933928865932> <@&1116021940537262091> \n<:Major:1144618946021052546> <@&1116021938649837750> \n<:Captain:1144618908578492518> <@&1116021935885783141> \n<:1stLieutenant:1144618888835907675> <@&1116021932844929084> \n<:2ndLieutenant:1144618895492259971> <@&1116021930466758676> \n<:Overseer:1144618963666481222> <@&1116021918663983285>\n### __Warrant Officers__:\n<:WarrantOfficer5:1144748295185506494> <@&1144652427165978755>\n<:WarrantOfficer4:1144748288025833613> <@&1144652412439769149>\n<:WarrantOfficer3:1144748279490433197> <@&1144652398577598545>\n<:WarrantOfficer2:1144748273626796032> <@&1144652373214634004>\n<:WarrantOfficer1:1144748269382160384> <@&1144652314498564268>\n### __SNCOs:__\n<:SergeantMajor:1144618870431305829> <@&1133109108854243408> \n<:FirstSergeant:1144618927423508500> <@&1133108178314330242> \n<:MasterSergeant:1144618957874151535> <@&1116021913303658598>\n### __NCOs:__\n<:StaffSergeant:1144618882519269426> <@&1116021911000973362>\n<:Sergeant:1144618876282339369> <@&1133107162571346021> \n<:MasterCorporal:1144618952564150414> <@&1116021905338662933> \n<:Corporal:1144618920825852064> <@&1116021902465581107>\n### __Enlisted:__\n<:LanceCorporal:1144618969643364392> <@&1144661908037849209>\n<:PrivateFirstClass:1144618856476848289> <@&1116021897822486558>\n<:Private:1144742173389103115> <@&1116021894576099438>\n\n<:Recruit:1144742169060573354> <@&1116062055410180136>",
                color=config.TFC_GOLD
            )
            embed.set_image(url=config.HIERARCHY_BANNER)

            await ctx.message.delete()
            await ctx.send(embed=embed, view=HierarchyMenuView())

        else:
            await ctx.message.delete()
            return

async def setup(bot: commands.Bot):
    await bot.add_cog(test(bot))