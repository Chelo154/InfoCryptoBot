import os


def get_nomics_api_key() -> str:
    return os.getenv('NOMICS_API_KEY')
