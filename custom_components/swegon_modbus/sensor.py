"""Sensor platform for Swegon Modbus integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo

from . import DOMAIN
from .const import (
    DEFAULT_PORT,
    SENSOR_FRESH_AIR_TEMP,
    SENSOR_SUPPLY_AIR_TEMP,
    SENSOR_EXTRACT_AIR_TEMP,
    SENSOR_EXHAUST_AIR_TEMP,
    SENSOR_SUPPLY_FAN_RPM,
    SENSOR_EXHAUST_FAN_RPM,
    SENSOR_ROTOR_RPM,
    SENSOR_OPERATING_MODE_STATUS,
    SENSOR_FILTER_GUARD,
    SENSOR_TEMP_SETPOINT,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Swegon Modbus sensors from a config entry."""
    host = entry.data[CONF_HOST]
    port = entry.data.get(CONF_PORT, DEFAULT_PORT)
    name = entry.data[CONF_NAME]

    entities = []

    # Temperature sensors
    entities.append(
        SwegonModbusSensor(
            name="Fresh Air Temp",
            unique_id="swegon_fresh_air_temp",
            address=SENSOR_FRESH_AIR_TEMP,
            scale=0.1,
            unit=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )
    entities.append(
        SwegonModbusSensor(
            name="Supply Air Temp",
            unique_id="swegon_supply_air_temp",
            address=SENSOR_SUPPLY_AIR_TEMP,
            scale=0.1,
            unit=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )
    entities.append(
        SwegonModbusSensor(
            name="Extract Air Temp",
            unique_id="swegon_extract_air_temp",
            address=SENSOR_EXTRACT_AIR_TEMP,
            scale=0.1,
            unit=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )
    entities.append(
        SwegonModbusSensor(
            name="Exhaust Air Temp",
            unique_id="swegon_exhaust_air_temp",
            address=SENSOR_EXHAUST_AIR_TEMP,
            scale=0.1,
            unit=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )

    # RPM sensors
    entities.append(
        SwegonModbusSensor(
            name="Supply Fan RPM",
            unique_id="swegon_supply_fan_rpm",
            address=SENSOR_SUPPLY_FAN_RPM,
            scale=1,
            unit="rpm",
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )
    entities.append(
        SwegonModbusSensor(
            name="Exhaust Fan RPM",
            unique_id="swegon_exhaust_fan_rpm",
            address=SENSOR_EXHAUST_FAN_RPM,
            scale=1,
            unit="rpm",
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )
    entities.append(
        SwegonModbusSensor(
            name="Rotor RPM",
            unique_id="swegon_rotor_rpm",
            address=SENSOR_ROTOR_RPM,
            scale=1,
            unit="rpm",
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )

    # Status sensors
    entities.append(
        SwegonModbusSensor(
            name="Operating Mode Status",
            unique_id="swegon_operating_mode_status",
            address=SENSOR_OPERATING_MODE_STATUS,
            scale=1,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )
    entities.append(
        SwegonModbusSensor(
            name="Filter Guard Info",
            unique_id="swegon_filter_guard",
            address=SENSOR_FILTER_GUARD,
            scale=1,
            entry_id=entry.entry_id,
            host=host,
            port=port,
        )
    )
    entities.append(
        SwegonModbusSensor(
            name="Temperature Setpoint",
            unique_id="swegon_temp_setpoint",
            address=SENSOR_TEMP_SETPOINT,
            scale=0.1,
            unit=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
            entry_id=entry.entry_id,
            host=host,
            port=port,
            is_holding=True,
        )
    )

    async_add_entities(entities)


class SwegonModbusSensor(SensorEntity):
    """Representation of a Swegon Modbus sensor."""

    def __init__(
        self,
        name: str,
        unique_id: str,
        address: int,
        scale: float = 1,
        unit: str | None = None,
        device_class: SensorDeviceClass | None = None,
        entry_id: str = "",
        host: str = "",
        port: int = 502,
        is_holding: bool = False,
    ) -> None:
        """Initialize the sensor."""
        self._attr_name = f"Swegon {name}"
        self._attr_unique_id = unique_id
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = device_class
        self.address = address
        self.scale = scale
        self.entry_id = entry_id
        self.is_holding = is_holding
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

    async def async_update(self) -> None:
        """Update the sensor value from Modbus."""
        self._attr_native_value = None
