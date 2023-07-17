import requests
class ILS:
    def get_value(self=''):
        return 0.28
    def calculate(x):
        return ILS.get_value() * x
    def calculate_live(value_user,live):
        return  value_user*live

    def live_currency(self=''):

        response = requests.get(
            'https://api.freecurrencyapi.com/v1/latest?apikey=6HNYZtcqafrbi7GPrHbB2KcxkwEczWI2F8icagLz&currencies=EUR%2CUSD&base_currency=ILS')
        if response.status_code == 200:
            currency_list = (response.json())
            usd = currency_list["data"]["USD"]
            return usd
        else:
            print("Could not get rate from API using default rate")