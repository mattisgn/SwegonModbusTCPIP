"""Placeholder sensor module."""
from homeassistant.components.sensor import SensorEntity

async def async_setup_entry(hass, config_entry, async_add_devices):
    async_add_devices([], True)
