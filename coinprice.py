import requests
import pprint

def main():
    dollars = get_bitcoin_ammount()
    converted = convert_bitcoin_to_dollars(dollars)
    display_result(dollars, converted)

def get_bitcoin_ammount():
    while True:
        try:
            return float(input(f'Enter bitcoin to convert: '))
        except:
            print('Enter a number')

def get_exchange_rate():
    # Get exchange rate from bitcoin to USD
    response = request_rates()
    rate = extract_rate(response)
    return rate

def convert_bitcoin_to_dollars(bitcoin):
    exchange_rate = get_exchange_rate()
    return convert(bitcoin, exchange_rate)
    
def request_rates():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    return requests.get(url).json()

def extract_rate(rates):
    return rates['bpi']['USD']['rate_float']

def convert(amount, exchange_rate):
    return amount * exchange_rate

def display_result(bitcoin, converted):
    print(f'{bitcoin:.2f} bitcoin is equivalent to ${converted:.2f} dollars')

if __name__ == '__main__':
    main()