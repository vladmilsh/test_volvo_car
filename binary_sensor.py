from __future__ import annotations
from typing import Any, Callable, Tuple
from homeassistant.helpers.entity import Entity
from .const import DOMAIN
from . import vmc
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
)
import logging
_LOGGER = logging.getLogger(__name__)
async def async_setup_entry(hass, config_entry, async_add_entities):
    sst1 = hass.data[DOMAIN][config_entry.entry_id]