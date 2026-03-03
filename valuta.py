import argparse
import requests
from dotenv import load_dotenv, set_key
from os import getenv

parser = argparse.ArgumentParser(
    description='set api key'
)

parser.add_argument('-key', action='store', type=str, help='ExchangeRate api key')
args = parser.parse_args()

load_dotenv()
API_KEY = getenv('KEY')

if args.key is None and API_KEY is None:
    print('You need to give an api key')
    exit()

if args.key is not None:
    set_key('.env', 'KEY', args.key)
    API_KEY = args.key

print('Valutas should be written in the IS 4217 standard, such as')
print('USD, EUR, GBP, DKK')

first_currency = input('Input valuta to convert from: ')
second_currency = input('Input valuta to convert to: ')
print('amount is optional, if you just want to see convertion rate')
amount = input('Input amount to convert: ')

URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{first_currency}/{second_currency}/{amount}'

res = requests.get(URL)

data = res.json()

if data['result'] == 'error':
    if data['error-type'] == 'invalid-key':
        print('Invalid key')
        print('Make sure to run the program with  \'python3 valuta.py -key [VALID_KEY]\'')
        exit()
    else:
        print('There was an error')
        print('Make sure the valuta you\'ve given is valid')
        print('such as EUR for euro or DKK for danish kroner')
        exit()

print(f'Convertion rate: {data["conversion_rate"]}')

if amount != '':
    print(f'{amount}{data["base_code"]} is: {data["conversion_result"]:.2f}{str(data["target_code"])}')
