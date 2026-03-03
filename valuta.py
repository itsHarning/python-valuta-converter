import argparse
import requests
from dotenv import set_key, load_dotenv
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

print('Supported valutas')
print('USD, EUR, GBP, DKK')

firstValuta = input('Input valuta to convert from: ')
secondValuta = input('Input valuta to convert to: ')
amount = input('Input amount to convert: ')

URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/DKK/10'

res = requests.get(URL)

data = res.json()

if str(data['result']) == 'error':
    if str(data['error-type']) == 'invalid-key':
        print('Invalid key')
        print('Make sure to run the program with  \'python3 valuta.py -key VALID_KEY\'')
        exit()
    else:
        print('There was an error')
        print('Make sure the valuta you\'ve given is valid')
        print('such as EUR for euro or DKK for danish kroner')
        exit()

print('Convertion rate: ' + str(data['conversion_rate']))
print('Your convertion is : ' + str(data['conversion_result']) + ' ' + str(data['target_code']))