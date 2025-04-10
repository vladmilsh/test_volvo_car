#  Copyright (c) 2025, Vladimir <vladmilsh@gmail.com>
"""Это тестовая интеграция автомобиля Volvo.
vmc/VMC - "vovlvo my car"
"""
import requests
import json
import asyncio
import logging
import time
import pycurl
from homeassistant.core import HomeAssistant
VMC_CLOUD_API_URL = 'https://volvoid.eu.volvocars.com/as/authorization.oauth2?'
_LOGGER = logging.getLogger(__name__)

#Общий класс интеграции, используется для инициализации, а так же как объект хранящий информацию обо всех устройствах интеграции
class VMC:

    def __init__(self, hass: HomeAssistant, username: str, password: str) -> None:
        self._username = username
        self._password = password
        self.devices = []
        self.hass:HomeAssistant = hass
    #Метод получения информации из API и создания объектов и сохранение их в массив self.devices  на основе этой информации, 
    #специально вынесен из конструктора в отдельный метод из-за ограничений HA на вызов запросов в не асинхронных методах.
    #В моем случае я вызывал методы API с помощью модуля request, парсил с помощью json,
    # затем передавал нужную информацию в конструктор класса устройства. Это текст от автора - "su_lysov"
    def pull_data(self):
        response = requests.post(VMC_CLOUD_API_URL + "auth/login/",
                                 json={"username": self._username, "password": self._password, "email": self._username},
                                 headers={'Content-Type': 'application/json'})
        self.key = json.loads(response.text)["key"]
        response = requests.get(VMC_CLOUD_API_URL + "houses", headers={"Authorization": "Token " + self.key})
        houses = json.loads(response.text)
        for house in houses:  # перебираем все дома
            response = requests.get(VMC_CLOUD_API_URL +
                                    "houses/" + str(house["id"]) + "/devices",
                                    headers={"Authorization": "Token " + self.key})
            devices = json.loads(response.text)
            # Перебираем все устройства в доме
            for device in devices:
                response = requests.get(VMC_CLOUD_API_URL +
                                        "houses/" + str(house["id"]) + "/devices/" + str(device["id"]),
                                        headers={"Authorization": "Token " + self.key})
                json_device = json.loads(response.text)
                
class Sensor:
    def __init__(self, name: str, status: str):
        self._name = name
        self._alarm = status
    def __init__(self, name: str, status: str, frendly_name: str):
        self._name = name
        self._alarm = status
        self._frendly_name = frendly_name

    @property
    def get_frendly_name(self) -> str:
        return self._frendly_name

    @property
    def get_leak_sensor_name(self) -> str:
        return self._name

    @property
    def get_leak_sensor_alarm_status(self) -> bool:
        return self._alarm

    def update(self, LeakSensorsDesc: json):
        self._alarm = LeakSensorsDesc[self._name]
    #  print("sensor "+ self._name +" status updated")