import requests


class EUR:
    def get_value(self=''):
        return 4.23

    def calculate(x):
        return EUR.get_value() * x

    def calculate_live(value_user, live):
        return  value_user*live

    def live_currency(self=''):

        response = requests.get(
            'https://api.freecurrencyapi.com/v1/latest?apikey=6HNYZtcqafrbi7GPrHbB2KcxkwEczWI2F8icagLz&currencies=EUR&base_currency=ILS')
        if response.status_code == 200:
            currency_list = (response.json())
            eur = currency_list["data"]["EUR"]
            return eur
        else:
            print("Could not get rate from API using default rate")
