# Python Currency Converter App
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
import json
import os
from dotenv import load_dotenv

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

if __name__ == "__main__":
    convert()