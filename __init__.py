import requests
import json
# import pycurl


url='https://api.volvocars.com/connected-vehicle/v2/vehicles'
#Указываем токен
token ='eyJhbGciOiJSUzI1NiIsImtpZCI6IklDbi1wUW1pZTJkOTFtWWM5XzlIQ2t1OERJQV9SUzI1NiIsInBpLmF0bSI6Ijl0MWYifQ.eyJzY29wZSI6ImNvbnZlOmJyYWtlX3N0YXR1cyBjb252ZTpmdWVsX3N0YXR1cyBjb252ZTpkb29yc19zdGF0dXMgb3BlbmlkIGNvbnZlOmRpYWdub3N0aWNzX3dvcmtzaG9wIGNvbnZlOnRyaXBfc3RhdGlzdGljcyBjb252ZTplbnZpcm9ubWVudCBjb252ZTpvZG9tZXRlcl9zdGF0dXMgY29udmU6ZW5naW5lX3N0YXR1cyBjb252ZTpsb2NrX3N0YXR1cyBjb252ZTp2ZWhpY2xlX3JlbGF0aW9uIGNvbnZlOndpbmRvd3Nfc3RhdHVzIGNvbnZlOnR5cmVfc3RhdHVzIGNvbnZlOmNvbm5lY3Rpdml0eV9zdGF0dXMgY29udmU6ZGlhZ25vc3RpY3NfZW5naW5lX3N0YXR1cyBjb252ZTp3YXJuaW5ncyIsImNsaWVudF9pZCI6Im1vamlwaXhfMTAiLCJncm50aWQiOiJ1dUNBUXNVeEhuR0ZmdHNIWHVEM253SVFpUjBmc3M0TSIsImlzcyI6Imh0dHBzOi8vdm9sdm9pZC5ldS52b2x2b2NhcnMuY29tIiwiaWF0IjoxNzQ0MzE1OTc2LCJqdGkiOiJvZ2w5ZFhaTnZqZGZ6VzMyRUttb2k1IiwibWFya2V0IjoiR0IiLCJhY3IiOiJ1cm46dm9sdm9pZDphYWw6YnJvbnplOmFueSIsImF1ZCI6Im1vamlwaXhfMTAiLCJmaXJzdE5hbWUiOiJEZXZlbG9wZXIiLCJsYXN0TmFtZSI6IlZvbHZvIENhcnMiLCJzdWIiOiJlM2Y1M2JkYi1iZjUwLTRlMGEtYmU5Ny1kYjkzNmMxMGEzYjQiLCJwaS5zcmkiOiJHRl8tN0ZscXhEOEFnSnoxdlRncG1wTi1TTkUuLnZmQ2IuZkRjSkllM0U0c0N4dWxWWWxSWDhrMFhVMSIsInVzZXJOYW1lIjoiZGV2ZWxvcGVydm9sdm9jYXJzY29tQGdtYWlsLmNvbSIsImVtYWlsIjoiZGV2ZWxvcGVydm9sdm9jYXJzY29tQGdtYWlsLmNvbSIsImV4cCI6MTc0NDMxNzc3Nn0.SKJws8Xrvq4JQC_YNjZh8KbZkOztmvSB_jyx6gXwiL-qj7nw0sWyaTu-KD4PE5Lb0VghWPuBQTI87Kyi7rM6zm37_5-dCIaEs3sM5Pzmz1EvZcJ435fAtjotFMoEXflQheEXxZEGsGzG6YomcVG0tWMGNrHSxhXbj0qEeuAqe-E4UOrMMZkIXGWXH8yHiRi0QaU-7u9vz2lV1a1WaxWnkmpPsFZcD4B6JclW66k7PVkKA6ofTXDR4MjTy0F2sQ3zEggGkAFQ6cNjmwoYXVrSmSN3cOtcTMKvztJZN0nXAaVFchImGnPQ9pzgu4CEKSJ6ofwjhaqdGDf30RUKf8HJGA'
#Получение VIN
headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {token}'
} 
api='050ccfbfa63143a5900bed0fe3785fd1'
params = {
    'vcc-api-key': f'{api}'
}
data = requests.get(url, headers=headers, params=params).json()
vin = data['data'][0]['vin']
# Печатаем значение VIN для контроля
print(vin)
#Connected Vehicle API 
# Класс для получения данных по данному API - не рабочий класс
# class VMCconnvehapi:
    
#     def __init__(self, url , token, api):
#         # self._vin = vin
#         self._token = token
#         self._api = api
#         # self._mainres = mainres
#         self.url = url 
        

# def pull_data(url, headers, params, **kwarg):
#     vin= requests.get(url, headers=headers, params=params)
#   Тестовый набор "конечных точек" тестового автомобиля:
url_api = [
    f'{url}/{vin}/engine',
    f'{url}/{vin}/windows',
    f'{url}/{vin}/engine-status',
    f'{url}/{vin}/fuel',
    f'{url}/{vin}/odometer'
]
json_r4=[]
with open('out.json', 'w'):
    pass
for i, r2 in enumerate(url_api):
    r2 = requests.get(url_api[i], headers=headers, params=params).json()
    print(r2)
    
#Запись данных API в файл:
    json_r4.append(r2)
    with open('out.json', 'w') as outfile:
        json.dump(json_r4, outfile,  indent=4)

#     with open('out.json', 'a') as f:
#         json.dump([r3], f, indent= '\t')
# with open('out.json', 'r') as fi:
#     d = json.load(fi) 
#     # print(d[int('data')][int('oilLevelWarning')][int('value')])
#     print(type(d))
# Чтение данных из файла:
with open('out.json') as f:
    data = json.loads(f.read())
    d1=data[2]
    # print(d1)
    res = d1["data"]["engineStatus"]
    print(res)
    # res1 = res["frontLeftWindow"]
    # print(res1)
    # print(data[3])