import requests
from src.dotenv_data import get_nomics_api_key


def check_crypto_values(cryptos: list[str]) -> list[dict]:
    key = get_nomics_api_key()

    crypto_params = ','.join(cryptos)

    print(crypto_params)

    url = 'https://api.nomics.com/v1/currencies/ticker'

    response = requests.get(url, params={
        'key': key,
        'ids': crypto_params,
        'interval': '1h'
    })

    response = response.json()

    return [
        {
            'id': item['id'],
            'name': item['name'],
            'logo': item['logo_url'],
            'status': item['status'],
            'price': item['price'],
            'price_date': item['price_date']
        }
        for item in response
    ]

