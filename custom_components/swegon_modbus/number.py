"""Number platform for Swegon Modbus integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.number import NumberEntity, NumberMode
from homeassistant.const import UnitOfTemperature, CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo

from . import DOMAIN
from .const import DEFAULT_PORT, SENSOR_TEMP_SETPOINT

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Swegon Modbus number from a config entry."""
    host = entry.data[CONF_HOST]
    port = entry.data.get(CONF_PORT, DEFAULT_PORT)
    name = entry.data[CONF_NAME]

    entities = [
        SwegonModbusNumber(
            name="Temperature Setpoint",
            unique_id="swegon_temp_setpoint_number",
            address=SENSOR_TEMP_SETPOINT,
            min_value=13,
            max_value=25,
            step=1,
            hub_name=f"{name}_{host}_{port}",
            host=host,
            port=port,
        ),
    ]

    async_add_entities(entities)


class SwegonModbusNumber(NumberEntity):
    """Representation of a Swegon Modbus number entity."""

    _attr_mode = NumberMode.BOX

    def __init__(
        self,
        name: str,
        unique_id: str,
        address: int,
        min_value: float = 0,
        max_value: float = 100,
        step: float = 1,
        hub_name: str = "swegon_casa",
        host: str = "",
        port: int = 502,
    ) -> None:
        """Initialize the number."""
        self._attr_name = f"Swegon {name}"
        self._attr_unique_id = unique_id
        self._attr_native_min_value = min_value
        self._attr_native_max_value = max_value
        self._attr_native_step = step
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self.address = address
        self.hub_name = hub_name
        self.host = host
        self.port = port
        self._attr_native_value = None

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, f"{self.host}_{self.port}")},
            name="Swegon Modbus",
            manufacturer="Swegon",
            model="CASA R5H SCB 3.0",
        )

    async def async_set_native_value(self, value: float) -> None:
        """Set the value."""
        try:
            # Scale temperature to Modbus format (x10)
            modbus_value = int(value * 10)
            await self.hass.data[DOMAIN].get("modbus_hub").async_pb_call(
                unit=1,
                address=self.address,
                values=[modbus_value],
                write_type="holding",
            )
            self._attr_native_value = value
        except Exception as err:
            _LOGGER.error("Error setting temperature %s: %s", value, err)

    async def async_update(self) -> None:
        """Update the number value from Modbus."""
        try:
            value = await self.hass.data[DOMAIN].get("modbus_hub").async_pb_call(
                unit=1,
                address=self.address,
                count=1,
                read_type="holding",
            )

            if value and len(value.registers) > 0:
                raw_value = value.registers[0]
                if raw_value > 32767:
                    raw_value = raw_value - 65536
                self._attr_native_value = round(raw_value / 10, 1)
        except Exception as err:
            _LOGGER.error("Error updating number %s: %s", self._attr_name, err)
