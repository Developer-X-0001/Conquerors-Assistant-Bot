import config
import aiohttp
import discord

from discord import Webhook

async def sql_update(reason: str, code, queries: list, color_code: int):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url=config.LOGGING_WEBHOOK_URL, bot_token=config.TOKEN, session=session)

        colors = {
            0: 0xac060c,
            1: 0x89f5a5
        }
        query_data = ""
        for entry in queries:
            query_data += f"- {entry[0]} ({entry[1]})\n"

        if query_data == "":
            query_data = "None"

        embed = discord.Embed(
            title="SQL Database Updated",
            description=f"**Reason:** {reason}\
                        \n\n__**Queries:**__\n{query_data}\
                        \n```diff\n{'+' if color_code == 1 else '-'} {code}\n```",
            color=colors[color_code]
        )

        await webhook.send(
            embed=embed
        )

async def sql_update_confirm():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url=config.LOGGING_WEBHOOK_URL, bot_token=config.TOKEN, session=session)

        embed = discord.Embed(
            description="```diff\n+ SQL update request completed successfully\n```",
            color=0x89f5a5
        )

        await webhook.send(
            embed=embed
        )