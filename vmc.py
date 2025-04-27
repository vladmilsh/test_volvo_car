#  Copyright (c) 2025, Vladimir <vladmilsh@gmail.com>
"""Это тестовая интеграция автомобиля Volvo.
vmc/VMC - "volvo my car"
"""
import requests
import json
import asyncio
import logging
import time
# from homeassistant.core import HomeAssistant
import pycurl

class VMC:
    def __init__(self):
        pass
    
    def pull_data(self):
        vin = 'YV4952NA4F120DEMO'
        token = input("Введите ваш token: ")
        api='050ccfbfa63143a5900bed0fe3785fd1'

        url = [
            f'https://api.volvocars.com/connected-vehicle/v2/vehicles/{vin}/diagnostics',
            f'https://api.volvocars.com/connected-vehicle/v2/vehicles/{vin}/brakes',
            f'https://api.volvocars.com/connected-vehicle/v2/vehicles/{vin}/windows',
            f'https://api.volvocars.com/location/v1/vehicles/{vin}/location'
            ]

    
        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {token}'
            }

        params= {
            'vcc-api-key': f'{api}'
            }

        json_r4=[]
        with open('out.json', 'w'):
            pass
        for i, r2 in enumerate(url):
            r2 = requests.get(url[i], headers=headers, params=params).json()
            # json_device = json.loads(r2.text)
            # print(r2)
            #Запись данных API в файл:
            json_r4.append(r2)
            with open('out.json', 'w') as outfile:
                json.dump(json_r4, outfile,  indent=4)
        with open('out.json') as f:
            da = json.loads(f.read())
            d1=da[0]
            res = d1["data"]["serviceWarning"]
            print(res)
r5=VMC()
print(r5.pull_data())
