from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
import asyncio
from . import vmc
from .const import DOMAIN
import logging
_LOGGER = logging.getLogger(__name__)
PLATFORMS: list[str] = ["sensor", "binary_sensor", "switch", "device_tracker"]
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    #Создать объект с подключением к сервису
    vmc1 = vmc.VMC(hass, entry.data["username"], entry.data["password"])
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = vmc1
    await hass.async_add_executor_job(
             vmc1.pull_data
         )

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok