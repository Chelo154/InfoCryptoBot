from discord.ext.commands import Bot
from src.bot.commands import *


def config_bot(bot: Bot):
    __setup_start__(bot)
    load_ping(bot)
    load_check_crypto(bot)
    load_info_crypto(bot)
    load_support(bot)


def __setup_start__(bot:Bot):
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected')


