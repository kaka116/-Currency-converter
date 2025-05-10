import customtkinter
import functions as func

customtkinter.set_appearance_mode("system")

# window creation and config
window = customtkinter.CTk()
window.geometry("600x600")

# create all elements
title = customtkinter.CTkLabel(window, text="Currency Converter", font=("Verdana", 26))

original_currency = customtkinter.CTkLabel(window, text="Select original currency", font=("Verdana", 12))
field_original_currency = customtkinter.CTkOptionMenu(window, values=["USD", "BRL", "EUR", "BTC"])
insert_value = customtkinter.CTkLabel(window, text="Value", font=("Verdana", 12))
value = customtkinter.CTkEntry(window)

new_currency = customtkinter.CTkLabel(window, text="Select currency to convert", font=("Verdana", 12))
field_new_currency = customtkinter.CTkOptionMenu(window, values=["USD", "BRL", "EUR", "BTC"])

button_convert = customtkinter.CTkButton(window, text="Convert", command=func.convert_currency)

currency_list = customtkinter.CTkScrollableFrame(window)

available_currency = ["Euro", "Dollar", "Real", "BitCoin"]
for currency in available_currency:
    currency_text = customtkinter.CTkLabel(currency_list, text=currency, font=("Verdana", 12))
    currency_text.pack()

# elements placement
title.pack(padx=10, pady=10)

original_currency.pack(padx=10, pady=20)
insert_value.pack()
value.pack()
field_original_currency.pack(padx=10, pady=5)


new_currency.pack(padx=10, pady=20)
field_new_currency.pack(padx=10)

button_convert.pack(padx=10, pady=40)

currency_list.pack(padx=10, pady=10)
# start the gui event loop
window.mainloop()
