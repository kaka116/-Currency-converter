import xmltodict

# open and pass the coins file to the dictionary, catch the currencies
def get_currencies():
    with open("static/currency.xml", "rb") as currency_fl:
        dic_currency = xmltodict.parse(currency_fl)

    currencies = dic_currency["xml"]
    return currencies


# open and pass the conversion file to the dictionary, catch the conversions
def get_conversions():
    with open("static/convert.xml", "rb") as convert_fl:
        dic_convert = xmltodict.parse(convert_fl)

    available_conversions = {}

    conversion = dic_convert["xml"]
    for convert_duo in conversion:
        original_currency, final_currency = convert_duo.split("-")
        if original_currency in available_conversions:
            available_conversions[original_currency].append(final_currency)
        else:
            available_conversions[original_currency] = [final_currency]

    return available_conversions


def convert_currency():
    print("convert")

