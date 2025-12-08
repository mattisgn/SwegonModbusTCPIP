"""Placeholder number module."""
from homeassistant.components.number import NumberEntity

async def async_setup_entry(hass, config_entry, async_add_devices):
    async_add_devices([], True)
