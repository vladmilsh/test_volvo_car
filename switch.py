from __future__ import annotations
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from . import vmc
from .const import DOMAIN
import logging
_LOGGER = logging.getLogger(__name__)

class MySwitch(SwitchEntity):
    # Implement one of these methods.

    def turn_on(self, **kwargs) -> None:
        """Turn the entity on."""

    async def async_turn_on(self, **kwargs):
        """Turn the entity on."""

class MySwitch(SwitchEntity):
    # Implement one of these methods.

    def turn_off(self, **kwargs):
        """Turn the entity off."""

    async def async_turn_off(self, **kwargs):
        """Turn the entity off."""

class MySwitch(SwitchEntity):
    # Implement one of these methods.

    def toggle(self, **kwargs):
        """Toggle the entity."""

    async def async_toggle(self, **kwargs):
        """Toggle the entity."""