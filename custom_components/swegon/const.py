from homeassistant.const import Platform

# Minimal constants placeholder. Replace with upstream const.py for full functionality.
DOMAIN: str = "swegon"
PLATFORMS = [Platform.BINARY_SENSOR, Platform.BUTTON, Platform.NUMBER, Platform.SELECT, Platform.SENSOR, Platform.SWITCH]

CONF_NAME: str = "name"
CONF_DEVICE_MODEL: str = "device_model"
CONF_IP: str = "ip_address"
CONF_PORT: str = "port"
CONF_SLAVE_ID: str = "slave_id"
CONF_SCAN_INTERVAL: str = "scan_interval"
CONF_SCAN_INTERVAL_FAST: str = "scan_interval_fast"

DEFAULT_SCAN_INTERVAL: int = 300
DEFAULT_SCAN_INTERVAL_FAST: int = 5

DEVICE_CASA_R4 = "CASA R4"
DEVICE_CASA_R15 = "CASA R15"
