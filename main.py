import os
import config
import discord
import sqlite3

from discord.ext import commands
from Interface.PromotionRequest import PromotionRequestManage
from Interface.CallsignChangeView import CallsignUpdateView
from Interface.ApplicationButtons import ApplicationButtons
from Interface.InformationPanel import InformationPanelView
from Interface.InteractionMenu import InteractionMenuView
from Interface.InformationButtons import InformationView
from Interface.LocationsPanel import LocationsPanelView
from Interface.QuestionsView import QuestionManageView
from Interface.SelfrolesMenu import SelfrolesMenuView
from Interface.HierarchyMenu import HierarchyMenuView
from Interface.LOARequestView import LOARequestView
from Interface.ArmoryMenu import ArmoryMenuView

intents = discord.Intents.all()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config.PREFIX,
            intents=intents,
            application_id=config.APPLICATION_ID,
            activity=discord.Game(name="under development")
        )

    async def setup_hook(self):
        
        self.add_view(PromotionRequestManage())
        self.add_view(InformationPanelView())
        self.add_view(InteractionMenuView())
        self.add_view(ApplicationButtons())
        self.add_view(CallsignUpdateView())
        self.add_view(QuestionManageView())
        self.add_view(LocationsPanelView())
        self.add_view(SelfrolesMenuView())
        self.add_view(HierarchyMenuView())
        self.add_view(InformationView())
        self.add_view(LOARequestView())
        self.add_view(ArmoryMenuView())

        sqlite3.connect("./Databases/data.sqlite").execute(
            '''
                CREATE TABLE IF NOT EXISTS UserLOAs (
                    user_id INTEGER,
                    reason TEXT,
                    starting_time INTEGER,
                    ending_time INTEGER,
                    accepted_by INTEGER,
                    PRIMARY KEY (user_id)
                )
            '''
        ).execute(
            '''
                CREATE TABLE IF NOT EXISTS CallsignRequests (
                    user_id INTEGER,
                    reason TEXT,
                    old_callsign TEXT,
                    new_callsign TEXT,
                    PRIMARY KEY (user_id)
                )
            '''
        ).execute(
            '''
                CREATE TABLE IF NOT EXISTS UserData (
                    user_id INTEGER,
                    points INTEGER DEFAULT 0,
                    callsign TEXT,
                    name TEXT,
                    PRIMARY KEY (user_id)
                )
            '''
        ).execute(
            '''
                CREATE TABLE IF NOT EXISTS PromotionRequests (
                    user_id INTEGER,
                    current_rank INTEGER,
                    requesting_rank INTEGER,
                    PRIMARY KEY (user_id)
                )
            '''
        )

        for filename in os.listdir("./Commands"):
            if filename.endswith('.py'):
                await self.load_extension('Commands.{}'.format(filename[:-3]))
                print("Loaded {}".format(filename))

            if filename.startswith('__'):
                pass

        for filename in os.listdir("./Events"):
            if filename.endswith('.py'):
                await self.load_extension('Events.{}'.format(filename[:-3]))
                print("Loaded {}".format(filename))

            if filename.startswith('__'):
                pass
        
        for filename in os.listdir("./Tasks"):
            if filename.endswith('.py'):
                await self.load_extension('Tasks.{}'.format(filename[:-3]))
                print("Loaded {}".format(filename))

            if filename.startswith('__'):
                pass

        await bot.tree.sync()

bot = Bot()

@bot.event
async def on_ready():
    print("{} is online! Latency: {}ms".format(bot.user.name, round(bot.latency * 1000)))

@bot.command(name="reload")
async def _reload(ctx: commands.Context, folder: str, cog: str):
    await ctx.message.delete()
    try:
        await bot.reload_extension(f"{folder}.{cog}")
        await ctx.send("🔁 **{}.py** successfully reloaded!".format(cog))
    except:
        await ctx.send("⚠ Unable to reload **{}**".format(cog))


bot.run(config.TOKEN)