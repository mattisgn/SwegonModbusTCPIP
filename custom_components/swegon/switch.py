"""Placeholder switch module."""
from homeassistant.components.switch import SwitchEntity

async def async_setup_entry(hass, config_entry, async_add_devices):
    async_add_devices([], True)
