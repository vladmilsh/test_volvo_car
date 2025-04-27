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
        # token = input("Введите ваш token: ")
        token ='eyJhbGciOiJSUzI1NiIsImtpZCI6IlZqaTcyLXdENWFXdTBtdzFRRDU4OTAyNDgwc19SUzI1NiIsInBpLmF0bSI6Ijl0MWYifQ.eyJzY29wZSI6ImNvbnZlOmJyYWtlX3N0YXR1cyBjb252ZTpmdWVsX3N0YXR1cyBjb252ZTpkb29yc19zdGF0dXMgb3BlbmlkIGNvbnZlOmRpYWdub3N0aWNzX3dvcmtzaG9wIGNvbnZlOnRyaXBfc3RhdGlzdGljcyBjb252ZTplbnZpcm9ubWVudCBjb252ZTpvZG9tZXRlcl9zdGF0dXMgY29udmU6ZW5naW5lX3N0YXR1cyBjb252ZTpsb2NrX3N0YXR1cyBjb252ZTp2ZWhpY2xlX3JlbGF0aW9uIGNvbnZlOndpbmRvd3Nfc3RhdHVzIGNvbnZlOnR5cmVfc3RhdHVzIGNvbnZlOmNvbm5lY3Rpdml0eV9zdGF0dXMgY29udmU6ZGlhZ25vc3RpY3NfZW5naW5lX3N0YXR1cyBjb252ZTp3YXJuaW5ncyIsImNsaWVudF9pZCI6Im1vamlwaXhfMTAiLCJncm50aWQiOiJ1dUNBUXNVeEhuR0ZmdHNIWHVEM253SVFpUjBmc3M0TSIsImlzcyI6Imh0dHBzOi8vdm9sdm9pZC5ldS52b2x2b2NhcnMuY29tIiwiaWF0IjoxNzQ1Nzc3MDY5LCJqdGkiOiJKNFAxMnVqS0IybFNqNkhzT1ZobDE0IiwibWFya2V0IjoiR0IiLCJhY3IiOiJ1cm46dm9sdm9pZDphYWw6YnJvbnplOmFueSIsImF1ZCI6Im1vamlwaXhfMTAiLCJmaXJzdE5hbWUiOiJEZXZlbG9wZXIiLCJsYXN0TmFtZSI6IlZvbHZvIENhcnMiLCJzdWIiOiJlM2Y1M2JkYi1iZjUwLTRlMGEtYmU5Ny1kYjkzNmMxMGEzYjQiLCJwaS5zcmkiOiJHRl8tN0ZscXhEOEFnSnoxdlRncG1wTi1TTkUuLnZmQ2IuZkRjSkllM0U0c0N4dWxWWWxSWDhrMFhVMSIsInVzZXJOYW1lIjoiZGV2ZWxvcGVydm9sdm9jYXJzY29tQGdtYWlsLmNvbSIsImVtYWlsIjoiZGV2ZWxvcGVydm9sdm9jYXJzY29tQGdtYWlsLmNvbSIsImV4cCI6MTc0NTc3ODg2OX0.ChY4b37jhkc4a3RSYRZmusw0Mcem_oTQHV-jbe3UeqTcjOhzkXPLD-MZN2W1RojerS0mDujRVi8rVAbxUSvYAxO2VySF_NBxsPf-8KDJ2QG2OkPXU34va_Ynq7lJETgyyMxcq-YbD2uJ6Dfl58gg6SqjTlayz0-TL7XZsFwvPTtvPHlu9mEj1XbcbxaXevnyAI8wzffzFFIGr475_o6kZxZc5CrNII6TuGnJNQlaY9K13Sb7MnDsDkZM80yPAyva5jE4GGQA5huUgv_DovifQtc4Xu0XhNz231B_0Ic-bHFGuzRDtRzI44apKYwMGay8FtUZXW14dqjWxyXf8mDVmQ'
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
