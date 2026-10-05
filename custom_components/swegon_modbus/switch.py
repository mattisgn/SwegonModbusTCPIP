"""Switch platform for Swegon Modbus integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo

from . import DOMAIN
from .const import DEFAULT_PORT, SWITCH_SMART_MODE, SWITCH_FIREPLACE_MODE

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Swegon Modbus switches from a config entry."""
    host = entry.data[CONF_HOST]
    port = entry.data.get(CONF_PORT, DEFAULT_PORT)
    name = entry.data[CONF_NAME]

    entities = [
        SwegonModbusSwitch(
            name="Smart Mode",
            unique_id="swegon_smart_mode",
            address=SWITCH_SMART_MODE,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        ),
        SwegonModbusSwitch(
            name="Fireplace Mode",
            unique_id="swegon_fireplace_mode",
            address=SWITCH_FIREPLACE_MODE,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        ),
    ]

    async_add_entities(entities)


class SwegonModbusSwitch(SwitchEntity):
    """Representation of a Swegon Modbus switch."""

    def __init__(
        self,
        name: str,
        unique_id: str,
        address: int,
        entry_id: str = "",
        host: str = "",
        port: int = 502,
    ) -> None:
        """Initialize the switch."""
        self._attr_name = f"Swegon {name}"
        self._attr_unique_id = unique_id
        self.address = address
        self.entry_id = entry_id
        self.host = host
        self.port = port
        self._attr_is_on = None

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, f"{self.host}_{self.port}")},
            name="Swegon Modbus",
            manufacturer="Swegon",
            model="CASA R5H SCB 3.0",
        )

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        self._attr_is_on = True

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        self._attr_is_on = False

    async def async_update(self) -> None:
        """Update the switch state from Modbus."""
        pass
