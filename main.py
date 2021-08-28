# Python Currency Converter App
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
import json
import os
from dotenv import load_dotenv
import tkinter as tk

def convert():
    print('Enter the source currency: ')
    cur_from = input()
    print('Enter the amount: ')
    amount_from = input()
    print('Enter the destination currency: ')
    cur_to = input()

    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"
    querystring = {"from":f"{cur_from}","to":f"{cur_to}","amount":f"{amount_from}"}
    load_dotenv()
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        'x-rapidapi-host': "currency-conversion-and-exchange-rates.p.rapidapi.com",
        'x-rapidapi-key': f'{rapid_api_key}'
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = json.loads(result)
    print(result["result"])

def graphics():
    window = tk.Tk()

    window.title('Currency Converter App')
    window.configure(background='#ec6627')

    window.rowconfigure([0, 1], minsize=50, weight=1)
    window.columnconfigure([0, 1, 2, 5], minsize=50, weight=1)

    # Beginning of row 1

    frame_amount = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_amount.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    label_amount = tk.Label(master=frame_amount, text='Amount', font='Helvetica 14 bold', background='#ec6627')
    label_amount.pack(padx=5, pady=5)

    frame_from = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_from.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    label_from = tk.Label(master=frame_from, text='From', font='Helvetica 14 bold', background='#ec6627')
    label_from.pack(padx=5, pady=5)

    frame_swap = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_swap.grid(row=0, column=2, padx=5, pady=5)
    label_swap = tk.Label(master=frame_swap,text='Swap', font='Helvetica 14 bold', background='#ec6627')
    label_swap.pack(padx=5, pady=5)

    frame_to = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_to.grid(row=0, column=5, padx=5, pady=5, sticky='w')
    label_to = tk.Label(master=frame_to,text='To', font='Helvetica 14 bold', background='#ec6627')
    label_to.pack(padx=5, pady=5)

    # End of row 1
    # Beginning of row 2

    frame_amount_entry = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1)
    frame_amount_entry.grid(row=1, column=0, padx=5, pady=5)
    label_amount_entry = tk.Entry(master=frame_amount_entry)
    label_amount_entry.pack(padx=5, pady=5)

    OPTIONS = [
        "USD",
        "EUR",
        "CZK"
    ]

    frame_from_choose = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1)
    frame_from_choose.grid(row=1, column=1, padx=5, pady=5)
    from_entry_variable = tk.StringVar(window)
    from_entry_variable.set(OPTIONS[0])
    w = tk.OptionMenu(frame_from_choose, from_entry_variable, *OPTIONS)
    w.pack()

    frame_swap_button = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1)
    frame_swap_button.grid(row=1, column=2, padx=5, pady=5)
    swap_button = tk.Button(master=frame_swap_button, text="-->\n<--")
    swap_button.pack(padx=5, pady=5)

    frame_convert_button = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1)
    frame_convert_button.grid(row=1, column=5, padx=5, pady=5)
    convert_button = tk.Button(master=frame_convert_button, text="Convert")
    convert_button.pack(padx=5, pady=5)

    # End of row 2


    window.mainloop()

if __name__ == "__main__":
    #convert()
    graphics()