# Python Currency Converter App
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
import json
import os
from dotenv import load_dotenv
import tkinter as tk
import re
from tkinter.constants import END

# Global variables declarations

frame_amount          = label_amount         = frame_from        = label_from           = None
frame_swap            = label_swap           = frame_to          = label_to             = None
frame_amount_entry    = label_amount_entry   = frame_from_choose = from_entry_variable  = None
w                     = frame_swap_button    = swap_button       = frame_to_choose      = None
to_entry_variable     = frame_convert_button = convert_button    = cur_from             = None
amount_from           = cur_to               = window            = None

# Converts a given amount of one currency to the other, uses external API
def convert(cur_from, amount_from, cur_to):
    global window
    global label_amount_entry
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
    result = result["result"]
    
    # Adds elements containing the result to the window
    frame_result = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_result.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='w')
    # Cleans the entry field as it's no longer needed
    label_amount_entry.delete(0, END)
    label_result = tk.Label(master=frame_result, text=f'''The result of conversion of 
        {amount_from} {cur_from} to {cur_to} is: \n\n{result} {cur_to}''', 
        font='Helvetica 14 bold', background='#ec6627')
    label_result.pack(padx=5, pady=5)

# Validates whether the entry field input is indeed numeric
def only_numeric_input(P):
    if P.isdigit():
        return True
    return False

def graphics():
    global window
    window = tk.Tk()

    window.title('Currency Converter App')
    window.configure(background='#ec6627')
    window.geometry('440x220')

    # Allocates space for 3 rows and 4 columns so the window is responsive
    window.rowconfigure([0, 1, 2], minsize=50, weight=1)
    window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

    global frame_amount; global label_amount; global frame_from; global label_from
    global frame_swap; global label_swap; global frame_to; global label_to
    global frame_amount_entry; global label_amount_entry; global frame_from_choose
    global from_entry_variable; global w; global frame_swap_button    
    global swap_button; global frame_to_choose; global to_entry_variable
    global frame_convert_button; global convert_button

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
    frame_to.grid(row=0, column=3, padx=5, pady=5, sticky='w')
    label_to = tk.Label(master=frame_to,text='To', font='Helvetica 14 bold', background='#ec6627')
    label_to.pack(padx=5, pady=5)

    # End of row 1
    # Beginning of row 2

    frame_amount_entry = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_amount_entry.grid(row=1, column=0, padx=5, pady=5)

    label_amount_entry = tk.Entry(master=frame_amount_entry)
    label_amount_entry.pack(padx=5, pady=5)
    callback = window.register(only_numeric_input)
    label_amount_entry.configure(validate='key', validatecommand=(callback, "%P"))

    OPTIONS = [
        "USD",
        "EUR",
        "CZK"
    ]

    frame_from_choose = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_from_choose.grid(row=1, column=1, padx=5, pady=5)
    from_entry_variable = tk.StringVar(window)
    from_entry_variable.set(OPTIONS[0])
    w = tk.OptionMenu(frame_from_choose, from_entry_variable, *OPTIONS)
    w.pack()

    frame_swap_button = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_swap_button.grid(row=1, column=2, padx=5, pady=5)
    swap_button = tk.Button(master=frame_swap_button, text="-->\n<--", command=swap_currencies)
    swap_button.pack(padx=5, pady=5)

    frame_to_choose = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_to_choose.grid(row=1, column=3, padx=5, pady=5)
    to_entry_variable = tk.StringVar(window)
    to_entry_variable.set(OPTIONS[1])
    w = tk.OptionMenu(frame_to_choose, to_entry_variable, *OPTIONS)
    w.pack()

    # End of row 2
    # Beginning of row 3

    frame_convert_button = tk.Frame(master=window, relief=tk.FLAT, borderwidth=1, background='#ec6627')
    frame_convert_button.grid(row=2, column=3, padx=5, pady=5)
    convert_button = tk.Button(master=frame_convert_button, text="Convert", command = handle_inputs)
    convert_button.pack(padx=5, pady=5)

    # End of row 3
    #window.mainloop()

# The function used when the button is pressed, processes input values
def handle_inputs():
    global cur_from
    global cur_to
    global amount_from

    amount_from = label_amount_entry.get()
    cur_from = from_entry_variable.get()
    cur_to = to_entry_variable.get() 
    convert(cur_from, amount_from, cur_to)

# The function used when the key is pressed, processes input values
def handle_inputs_(event):
    global cur_from
    global cur_to
    global amount_from

    amount_from = label_amount_entry.get()
    cur_from = from_entry_variable.get()
    cur_to = to_entry_variable.get() 
    convert(cur_from, amount_from, cur_to)
    print(event.char)

# Handles button pressed
def swap_currencies():
    global from_entry_variable
    global to_entry_variable
    
    # Dummy variables to exchange the fields
    auxiliary_var1 = from_entry_variable.get()
    auxiliary_var2 = to_entry_variable.get()

    from_entry_variable.set(auxiliary_var2)
    to_entry_variable.set(auxiliary_var1)

# Handles key pressed
def swap_currencies_(event):
    global from_entry_variable
    global to_entry_variable
    global label_amount_entry

    # Dummy variables to exchange the fields
    auxiliary_var1 = from_entry_variable.get()
    auxiliary_var2 = to_entry_variable.get()

    from_entry_variable.set(auxiliary_var2)
    to_entry_variable.set(auxiliary_var1)
    print(event.char)    

if __name__ == "__main__":
    graphics()
    # Binding the Enter key to show output
    window.bind('<Return>', handle_inputs_)
    # Binding the s key to swap sides
    window.bind('s', lambda event: swap_currencies_(event))
    window.mainloop()