import customtkinter
from currencies import get_conversions, get_currencies
from get_qoute import conversion


def final_currencies_by_key(selected_currency):
    list_final_currency = available_conversions[selected_currency]
    field_final_currency.configure(values=list_final_currency)
    field_final_currency.set(list_final_currency[0])


def convert_currency():
    initial_currency = field_original_currency.get()
    final_currency = field_final_currency.get()

    try:
        amount = float(value.get())
    except ValueError:
        conversion_text.configure(text="Inserts a numeric value!")
        return

    if initial_currency and final_currency:
        rate = float(conversion(initial_currency, final_currency))
        result = round(rate * amount, 2)
        conversion_text.configure(text=f"{amount} {initial_currency} = {result} {final_currency}")

    else:
        conversion_text.configure(text="Select coins correctly")


customtkinter.set_appearance_mode("system")

# window creation and config
window = customtkinter.CTk()
window.geometry("600x600")

available_conversions = get_conversions()

# create all elements
title = customtkinter.CTkLabel(window, text="Currency Converter", font=("Verdana", 26))

original_currency = customtkinter.CTkLabel(window, text="Select original currency", font=("Verdana", 12))
field_original_currency = customtkinter.CTkOptionMenu(window, values=list(available_conversions.keys()),
                                                      command=final_currencies_by_key)

insert_value = customtkinter.CTkLabel(window, text="Value", font=("Verdana", 12))
value = customtkinter.CTkEntry(window)

new_currency = customtkinter.CTkLabel(window, text="Select currency to convert", font=("Verdana", 12))
field_final_currency = customtkinter.CTkOptionMenu(window, values=["Choose original currency!"])

button_convert = customtkinter.CTkButton(window, text="Convert", command=convert_currency)

currency_list = customtkinter.CTkScrollableFrame(window)

conversion_text = customtkinter.CTkLabel(window, text="")

available_currencies = get_currencies()
for currency_code in available_currencies:
    currency_name = available_currencies[currency_code]
    currency_text = customtkinter.CTkLabel(currency_list, text=f"{currency_code} : {currency_name}",
                                           font=("Verdana", 12))
    currency_text.pack()

# elements placement
title.pack(padx=10, pady=10)

original_currency.pack(padx=10, pady=20)
insert_value.pack()
value.pack()
field_original_currency.pack(padx=10, pady=5)

new_currency.pack(padx=10, pady=20)
field_final_currency.pack(padx=10)

button_convert.pack(padx=10, pady=40)
conversion_text.pack(padx=10, pady=10)

currency_list.pack(padx=10, pady=10)
# start the gui event loop
window.mainloop()
