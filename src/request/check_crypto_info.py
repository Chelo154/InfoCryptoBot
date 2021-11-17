import requests
from src.dotenv_data import get_nomics_api_key


def check_crypto_info(cryptos: list[str]) -> list[dict]:
    cryptos_data = ','.join(cryptos)

    print(cryptos_data)

    url = "https://api.nomics.com/v1/currencies"

    response = requests.get(url, params={
        'key': get_nomics_api_key(),
        'ids': cryptos_data
    })

    return [
        {
            'id': item['id'],
            'name': item['name'],
            'description': item['description'],
            'logo': item['logo_url'],
            'website': item['website_url'],
            'discord': item['discord_url'],
            'github': item['github_url'],
            'facebook': item['facebook_url'],
            'twitter': item['twitter_url']

        }
        for item in response.json()
    ]

