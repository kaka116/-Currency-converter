import requests


def conversion(initial_currency, final_currency):
    link = f"https://economia.awesomeapi.com.br/json/last/{initial_currency}-{final_currency}"

    response = requests.get(link)
    data = response.json()

    return data[f"{initial_currency}{final_currency}"]["bid"]


