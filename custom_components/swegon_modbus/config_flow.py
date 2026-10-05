"""Config flow for Swegon Modbus TCP/IP integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.data_entry_flow import FlowResult

_LOGGER = logging.getLogger(__name__)

DOMAIN = "swegon_modbus"


class SwegonModbusConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for the Swegon Modbus TCP/IP integration."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            if not user_input.get(CONF_HOST):
                errors[CONF_HOST] = "invalid_host"
            else:
                return self.async_create_entry(
                    title=user_input.get(CONF_NAME, "Swegon Modbus"),
                    data=user_input,
                )

        data_schema = vol.Schema(
            {
                vol.Required(CONF_NAME, default="Swegon CASA"): str,
                vol.Required(CONF_HOST): str,
                vol.Required(CONF_PORT, default=502): int,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )
