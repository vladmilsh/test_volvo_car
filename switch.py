from __future__ import annotations
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from . import vmc
from .const import DOMAIN
import logging
_LOGGER = logging.getLogger(__name__)