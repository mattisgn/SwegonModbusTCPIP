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
    CONF_NAME: "Swegon Casa R5H",
    CONF_IP: "192.168.10.13",
    CONF_PORT: 502,
    CONF_SLAVE_ID: 1,
}

DEFAULT_OPTIONS: dict[str, Any] = {
    CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL,
    CONF_SCAN_INTERVAL_FAST: DEFAULT_SCAN_INTERVAL_FAST,
}


# -----------------------------------------------------------------------------
# Config Flow
# -----------------------------------------------------------------------------
class SwegonFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Swegon."""

    VERSION = 1

    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        """Return the options flow."""
        return SwegonOptionsFlowHandler(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # Hardcode the model ONCE at creation time
            data = {
                CONF_NAME: user_input[CONF_NAME],
                CONF_DEVICE_MODEL: DEVICE_CASA_R5H,
                CONF_IP: user_input[CONF_IP],
                CONF_PORT: user_input[CONF_PORT],
                CONF_SLAVE_ID: user_input[CONF_SLAVE_ID],
            }

            options = {
                CONF_SCAN_INTERVAL: user_input[CONF_SCAN_INTERVAL],
                CONF_SCAN_INTERVAL_FAST: user_input[CONF_SCAN_INTERVAL_FAST],
            }

            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=data,
                options=options,
            )

        schema_defaults = {
            **DEFAULT_DEVICE_DATA,
            **DEFAULT_OPTIONS,
        }

        return self.async_show_form(
            step_id="user",
            data_schema=_device_schema(schema_defaults),
            errors=errors,
        )


# -----------------------------------------------------------------------------
# Options Flow
# -----------------------------------------------------------------------------
class SwegonOptionsFlowHandler(OptionsFlow):
    """Handle Swegon options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                options={
                    CONF_SCAN_INTERVAL: user_input[CONF_SCAN_INTERVAL],
                    CONF_SCAN_INTERVAL_FAST: user_input[CONF_SCAN_INTERVAL_FAST],
                },
            )
            return self.async_create_entry(title="", data={})

        defaults = {
            **DEFAULT_OPTIONS,
            **self.config_entry.options,
        }

        return self.async_show_form(
            step_id="init",
            data_schema=_options_schema(defaults),
        )


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------
def _device_schema(defaults: dict[str, Any]) -> vol.Schema:
    """Schema for creating the config entry."""
    return vol.Schema(
        {
            vol.Required(
                CONF_NAME, default=defaults.get(CONF_NAME)
            ): cv.string,
            vol.Required(
                CONF_IP, default=defaults.get(CONF_IP)
            ): cv.string,
            vol.Optional(
                CONF_PORT, default=defaults.get(CONF_PORT)
            ): vol.All(vol.Coerce(int), vol.Range(min=0, max=65535)),
            vol.Optional(
                CONF_SLAVE_ID, default=defaults.get(CONF_SLAVE_ID)
            ): vol.All(vol.Coerce(int), vol.Range(min=0, max=255)),
            vol.Optional(
                CONF_SCAN_INTERVAL, default=defaults.get(CONF_SCAN_INTERVAL)
            ): vol.All(vol.Coerce(int), vol.Range(min=5, max=999)),
            vol.Optional(
                CONF_SCAN_INTERVAL_FAST,
                default=defaults.get(CONF_SCAN_INTERVAL_FAST),
            ): vol.All(vol.Coerce(int), vol.Range(min=1, max=999)),
        }
    )


def _options_schema(defaults: dict[str, Any]) -> vol.Schema:
    """Schema for the options flow."""
    return vol.Schema(
        {
            vol.Optional(
                CONF_SCAN_INTERVAL, default=defaults.get(CONF_SCAN_INTERVAL)
            ): vol.All(vol.Coerce(int), vol.Range(min=5, max=999)),
            vol.Optional(
                CONF_SCAN_INTERVAL_FAST,
                default=defaults.get(CONF_SCAN_INTERVAL_FAST),
            ): vol.All(vol.Coerce(int), vol.Range(min=1, max=999)),
        }
    )    VERSION = 1

    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        """Get the options flow for this handler."""
        return SwegonOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        """Handle a flow initialized by the user, adding the integration."""
        errors = {}

        if user_input is not None:
            # --- MODIFIED: Ensure the model is set before creating the entry ---
            user_input[CONF_DEVICE_MODEL] = DEVICE_CASA_R5H
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        return self.async_show_form(step_id="user", data_schema=getDeviceSchema(DEVICE_DATA.copy()), errors=errors)

class SwegonOptionsFlowHandler(OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input: dict[str, Any] | None = None):
        # Manage the options for the custom component."""

        if user_input is not None:
            # --- MODIFIED: Ensure the model is set before updating the entry ---
            user_input[CONF_DEVICE_MODEL] = DEVICE_CASA_R5H
            
            # Update config_entry with new data
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=user_input, options=self.config_entry.options
            )

            return self.async_create_entry(title="", data={})

        return self.async_show_form(step_id="init", data_schema=getDeviceSchema(self.config_entry.data))

""" ################################################### """
"""                     Dynamic schemas                 """
""" ################################################### """
# Schema taking device details when adding or updating
def getDeviceSchema(user_input: dict[str, Any] | None = None) -> vol.Schema:
    # --- MODIFIED: Removed DEVICE_TYPES list and model selector field ---
    # DEVICE_TYPES = [DEVICE_CASA_R4, DEVICE_CASA_R15]

    data_schema = vol.Schema(
        {
            vol.Required(
                CONF_NAME, description="Name", default=user_input[CONF_NAME]
            ): cv.string,
            # --- MODIFIED: Removed the CONF_DEVICE_MODEL selector field ---
            # vol.Required(CONF_DEVICE_MODEL, default=user_input[CONF_DEVICE_MODEL]): selector.SelectSelector(
            #     selector.SelectSelectorConfig(options=DEVICE_TYPES),
            # ),     
            vol.Required(
                CONF_IP, description="IP Address", default=user_input[CONF_IP]
            ): cv.string,
            vol.Optional(
                CONF_PORT, description="Port", default=user_input[CONF_PORT]
            ): vol.All(vol.Coerce(int), vol.Range(min=0, max=65535)),
            vol.Optional(
                CONF_SLAVE_ID, description="Slave ID", default=user_input[CONF_SLAVE_ID]
            ): vol.All(vol.Coerce(int), vol.Range(min=0, max=256)),
            vol.Optional(
                CONF_SCAN_INTERVAL, default=user_input[CONF_SCAN_INTERVAL]
            ): vol.All(vol.Coerce(int), vol.Range(min=5, max=999)),
            vol.Optional(
                CONF_SCAN_INTERVAL_FAST, default=user_input[CONF_SCAN_INTERVAL_FAST]
            ): vol.All(vol.Coerce(int), vol.Range(min=1, max=999)),
        }
    )

    return data_schema
