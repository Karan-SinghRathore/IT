import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Apply a themed style
        self.style = ThemedStyle(self.root)
        self.style.set_theme("scidblue")

        self.setup_ui()

    def setup_ui(self):
        # Entry for entering amount
        amount_label = ttk.Label(self.root, text="Enter Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        amount_entry = ttk.Entry(self.root, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Dropdown for selecting 'from' currency
        from_currency_label = ttk.Label(self.root, text="From Currency:")
        from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        from_currency_combobox = ttk.Combobox(self.root, textvariable=self.from_currency_var, values=self.get_currency_codes())
        from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        # Dropdown for selecting 'to' currency
        to_currency_label = ttk.Label(self.root, text="To Currency:")
        to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        to_currency_combobox = ttk.Combobox(self.root, textvariable=self.to_currency_var, values=self.get_currency_codes())
        to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

        # Result label
        result_label = ttk.Label(self.root, text="Result:")
        result_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        result_entry = ttk.Entry(self.root, textvariable=self.result_var, state="readonly")
        result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Convert button
        convert_button = ttk.Button(self.root, text="Convert", command=self.convert_currency)
        convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Get the latest exchange rates from a free API
            api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(api_url)
            data = response.json()
            rate = data["rates"][to_currency]

            result = amount * rate
            self.result_var.set(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        except Exception as e:
            self.result_var.set("Error converting currency. Please check your inputs.")

    def get_currency_codes(self):
        # You can add more currencies to this list
        return ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "INR"]

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
