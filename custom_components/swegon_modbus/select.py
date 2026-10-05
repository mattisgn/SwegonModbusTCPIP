"""Select platform for Swegon Modbus integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo

from . import DOMAIN
from .const import DEFAULT_PORT, SENSOR_OPERATING_MODE_STATUS

_LOGGER = logging.getLogger(__name__)

OPERATING_MODES = ["Stopped", "Away", "Home", "Boost", "Travelling"]
MODE_MAP = {
    "Stopped": 0,
    "Away": 1,
    "Home": 2,
    "Boost": 3,
    "Travelling": 4,
}
REVERSE_MODE_MAP = {v: k for k, v in MODE_MAP.items()}


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Swegon Modbus select from a config entry."""
    host = entry.data[CONF_HOST]
    port = entry.data.get(CONF_PORT, DEFAULT_PORT)
    name = entry.data[CONF_NAME]

    entities = [
        SwegonModbusSelect(
            name="Operating Mode",
            unique_id="swegon_operating_mode_select",
            address=SENSOR_OPERATING_MODE_STATUS,
            options=OPERATING_MODES,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        ),
    ]

    async_add_entities(entities)


class SwegonModbusSelect(SelectEntity):
    """Representation of a Swegon Modbus select entity."""

    def __init__(
        self,
        name: str,
        unique_id: str,
        address: int,
        options: list[str],
        entry_id: str = "",
        host: str = "",
        port: int = 502,
    ) -> None:
        """Initialize the select."""
        self._attr_name = f"Swegon {name}"
        self._attr_unique_id = unique_id
        self._attr_options = options
        self.address = address
        self.entry_id = entry_id
        self.host = host
        self.port = port
        self._attr_current_option = None

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, f"{self.host}_{self.port}")},
            name="Swegon Modbus",
            manufacturer="Swegon",
            model="CASA R5H SCB 3.0",
        )

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        self._attr_current_option = option

    async def async_update(self) -> None:
        """Update the select value from Modbus."""
        pass
