from discord.ext.commands import Bot
from src.dotenv_data import get_discord_token,load_dotenv_data
from src.bot import config_bot


def run_bot():
    load_dotenv_data()

    token = get_discord_token()

    bot = Bot(command_prefix='$')

    config_bot(bot)

    bot.run(token)


