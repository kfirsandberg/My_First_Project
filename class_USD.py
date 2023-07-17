import requests

class USD:

    def get_value(self=''):
        return 3.52
    def calculate(x):
        return USD.get_value() * x

    def calculate_live(value_user,live):
        return  value_user*live
    def live_currency(self=''):

        response = requests.get(
            'https://api.freecurrencyapi.com/v1/latest?apikey=6HNYZtcqafrbi7GPrHbB2KcxkwEczWI2F8icagLz&currencies=EUR%2CUSD%2CILS')
        if response.status_code == 200:
            currency_list = (response.json())
            ils = currency_list["data"]["ILS"]
            return ils
        else:
            print("Could not get rate from API using default rate")

