"""Swegon Modbus TCP/IP integration for Home Assistant."""
from __future__ import annotations

import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = "swegon_modbus"
VERSION = "1.0.0"


async def async_setup(hass, config):
    """Set up the Swegon Modbus integration."""
    _LOGGER.info("Setting up Swegon Modbus TCP/IP integration")
    return True
