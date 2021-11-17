import os


def get_discord_token() -> str:
    return os.getenv('DISCORD_CRYPTO_BOT_TOKEN')
