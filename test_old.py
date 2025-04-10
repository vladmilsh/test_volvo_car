import requests
import json
# import pycurl
vin = 'YV4952NA4F120DEMO'
token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6Inh0RDNiOHJCRHBjQjYxeWhqTW83NXJoek01WV9SUzI1NiIsInBpLmF0bSI6Ijl0MWYifQ.eyJzY29wZSI6ImxvY2F0aW9uOnJlYWQgb3BlbmlkIiwiY2xpZW50X2lkIjoibW9qaXBpeF8xMCIsImdybnRpZCI6ImJBU3h1bG9acm1NWUZzM2E4aVh1SWJFY1dpUkZoQm1hIiwiaXNzIjoiaHR0cHM6Ly92b2x2b2lkLmV1LnZvbHZvY2Fycy5jb20iLCJpYXQiOjE3NDIxOTgxMzgsImp0aSI6IjM5Z0Z6Wkhpb2Y1TXR5Y1N2bkNjVDgiLCJtYXJrZXQiOiJHQiIsImFjciI6InVybjp2b2x2b2lkOmFhbDpicm9uemU6YW55IiwiYXVkIjoibW9qaXBpeF8xMCIsImZpcnN0TmFtZSI6IkRldmVsb3BlciIsImxhc3ROYW1lIjoiVm9sdm8gQ2FycyIsInN1YiI6ImUzZjUzYmRiLWJmNTAtNGUwYS1iZTk3LWRiOTM2YzEwYTNiNCIsInBpLnNyaSI6IkFCWmpkUm9ZSXUydVVUWWd2WkNSQU9XM0stby4udmZDai5UQkZGMlVieGo4SDVJSDU2cVNDWXBIVlZCIiwidXNlck5hbWUiOiJkZXZlbG9wZXJ2b2x2b2NhcnNjb21AZ21haWwuY29tIiwiZW1haWwiOiJkZXZlbG9wZXJ2b2x2b2NhcnNjb21AZ21haWwuY29tIiwiZXhwIjoxNzQyMTk5OTM4fQ.k7Xhkq-82XbV6ZCx-mBbKLDQEefJQ4Dib8M4m38adVJhAE89CV8uRXUUU4P6Rtsck3J6wqnx5Bt2FwD2Ft_PzzNZiLahi_A-P6lOeS33SFdLJ-gRuJaGniyMaruYDLIhCyAd4bP4xjfBmcOThXEElQOcwwjTs34Owak3j67mW7sJAv6qWvBFiBpQH8AJrmcFTfH3mO3uePwSbzTUcHSjvemP2JJFB3HcRUeb1UhNH9bbD3TPZkl6wph0yPrL-FNgb-V3-DDrUm8VB6ZhGJZlDvMk24piIKypPX9N-QGVLXqhEl06UDJ3bmmcg3LJBAaP8rckZf3da-OxiYbHQQyguw'
api='050ccfbfa63143a5900bed0fe3785fd1'
# url = f'https://api.volvocars.com/connected-vehicle/v2/vehicles'
# url = f"https://api.volvocars.com/location/v1/vehicles/{vin}/location"
url = [
    "https://api.volvocars.com/connected-vehicle/v2/vehicles",
    f"https://api.volvocars.com/connected-vehicle/v2/vehicles/{vin}/engine",
    f'https://api.volvocars.com/location/v1/vehicles/{vin}/location'
   ]

    
headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {token}'
}

params= {
    'vcc-api-key': f'{api}'
}
# headers = [
#     'accept: application/json',
#     'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6InBwQnBGd1BzdWRoY2NvdDJxREQ5MWUydlAwY19SUzI1NiIsInBpLmF0bSI6Ijl0MWYifQ.eyJzY29wZSI6ImNvbnZlOmJyYWtlX3N0YXR1cyBjb252ZTpmdWVsX3N0YXR1cyBjb252ZTpkb29yc19zdGF0dXMgb3BlbmlkIGNvbnZlOmRpYWdub3N0aWNzX3dvcmtzaG9wIGNvbnZlOnRyaXBfc3RhdGlzdGljcyBjb252ZTplbnZpcm9ubWVudCBjb252ZTpvZG9tZXRlcl9zdGF0dXMgY29udmU6ZW5naW5lX3N0YXR1cyBjb252ZTpsb2NrX3N0YXR1cyBjb252ZTp2ZWhpY2xlX3JlbGF0aW9uIGNvbnZlOndpbmRvd3Nfc3RhdHVzIGNvbnZlOnR5cmVfc3RhdHVzIGNvbnZlOmNvbm5lY3Rpdml0eV9zdGF0dXMgY29udmU6ZGlhZ25vc3RpY3NfZW5naW5lX3N0YXR1cyBjb252ZTp3YXJuaW5ncyIsImNsaWVudF9pZCI6Im1vamlwaXhfMTAiLCJncm50aWQiOiJ1dUNBUXNVeEhuR0ZmdHNIWHVEM253SVFpUjBmc3M0TSIsImlzcyI6Imh0dHBzOi8vdm9sdm9pZC5ldS52b2x2b2NhcnMuY29tIiwiaWF0IjoxNzQyMTQyNDM4LCJqdGkiOiJENjhBc2QySFR6SWhlc2R6VXlUUERGIiwibWFya2V0IjoiR0IiLCJhY3IiOiJ1cm46dm9sdm9pZDphYWw6YnJvbnplOmFueSIsImF1ZCI6Im1vamlwaXhfMTAiLCJmaXJzdE5hbWUiOiJEZXZlbG9wZXIiLCJsYXN0TmFtZSI6IlZvbHZvIENhcnMiLCJzdWIiOiJlM2Y1M2JkYi1iZjUwLTRlMGEtYmU5Ny1kYjkzNmMxMGEzYjQiLCJwaS5zcmkiOiJHRl8tN0ZscXhEOEFnSnoxdlRncG1wTi1TTkUuLnZmQ2IuZkRjSkllM0U0c0N4dWxWWWxSWDhrMFhVMSIsInVzZXJOYW1lIjoiZGV2ZWxvcGVydm9sdm9jYXJzY29tQGdtYWlsLmNvbSIsImVtYWlsIjoiZGV2ZWxvcGVydm9sdm9jYXJzY29tQGdtYWlsLmNvbSIsImV4cCI6MTc0MjE0NDIzOH0.B2rb8RxSYLm8QyJ8yhejGIjSEp1L3jVvsP3l3tepNb1cG0UQJ3VNuX-UMmaCjuPd8FHFbmWG1WJ0Lyjj-GFHIKR4FHNegbm3w5A-9cd_vvEhOo2tqHFVUGXFpjnlV-K0f3ot7aCNr4M_xNBV97ewHnN7kuiM56lYRD6W_1fRV6BROeu81_89RlWNjo7PFY5tjTMkUAnsFrPJFln1ginV7CQdbsofiumZ6xLuNxY-KLZ1eKXYNUvUnSbVXPpj-vrXOblF1a43bhfpUY9PNuCmzVPeS2WQdew0dE5atCOXP7rXsiUzoAVhpDwqtmBJSDkcpZgc8XIgFTccC3KZkRQ5SQ',
#     'vcc-api-key: 050ccfbfa63143a5900bed0fe3785fd1'
# ]
# r2 = requests.get(url, headers=headers, params=params)
# r2=(url+vin, headers, params)
# r3=r2.json()
# print(r2)
for i, r2 in enumerate(url):
    r2 = requests.get(url[i], headers=headers, params=params)
    r3=r2.json()
    print(r3)
# class VMC:

#     def __init__(self, hass: str, username: str, password: str) -> None:
#         self._username = username
#         self._password = password
#         self.devices = []
#         self.hass = hass
# url = [f"{mainres}engine",
#        f"{mainres}windows",
#        f"{mainres}engine-status", 
#        f"{mainres}fuel",
#        f"{mainres}odometer"
#     ]
# headers = {
#     'accept': 'application/json',
#     'authorization': f'Bearer {token}'
#     }

# params= {
#     'vcc-api-key': f'{api}'
#     }
# # print ( VMCconnvehapi(vin, token, api, mainres, url))

# for i, r2 in enumerate(url):
#     res= requests.get(url[i], headers=headers, params=params)
#     r = res.json()
#     print (r)
