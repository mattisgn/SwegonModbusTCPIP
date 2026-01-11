"""Config flow for the Swegon integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry, ConfigFlow, OptionsFlow
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv

from .const import (
    DOMAIN,
    CONF_NAME,
    CONF_DEVICE_MODEL,
    CONF_IP,
    CONF_PORT,
    CONF_SLAVE_ID,
    CONF_SCAN_INTERVAL,
    CONF_SCAN_INTERVAL_FAST,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL_FAST,
    DEVICE_CASA_R5H,
)

_LOGGER = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Defaults used when creating a new config entry
# -----------------------------------------------------------------------------
DEFAULT_DEVICE_DATA: dict[str, Any] = {
    CONF_NAME:
