#  Copyright (c) 2025, Vladimir <vladmilsh@gmail.com>
"""Это тестовая интеграция автомобиля Volvo.
vmc/VMC - "volvo my car"
"""
import requests
import json
import asyncio
import logging
import time
import pycurl
from homeassistant.core import HomeAssistant