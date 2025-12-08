"""Minimal coordinator placeholder for Swegon integration.
Replace with upstream coordinator.py for full functionality."""
import logging
import datetime as dt
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

class SwegonCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, device, device_module, ip, port, slave_id, scan_interval, scan_interval_fast):
        super().__init__(hass, _LOGGER, name="Swegon Coordinator", update_interval=dt.timedelta(seconds=scan_interval))
        self._device = device
        self._swegonDevice = None
        self.config_selection = 0
        self._update_callbacks = {}

    def registerOnUpdateCallback(self, entity, callbackfunc):
        self._update_callbacks.update({entity: callbackfunc})

    def get_config_options(self):
        return {0: "Default"}

    def get_value(self, group, key):
        return None

    async def write_value(self, group, key, value):
        _LOGGER.debug("Stub write_value: %s %s %s", group, key, value)

    async def _async_update_data(self):
        # minimal no-op update
        return {}
