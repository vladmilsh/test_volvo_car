from homeassistant.const import (UnitOfVolume,PERCENTAGE,UnitOfTemperature)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.helpers.entity import Entity

from .const import DOMAIN
from . import vmc
import logging
_LOGGER = logging.getLogger(__name__)