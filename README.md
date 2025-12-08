# SwegonModbusTCPIP

Home Assistant configuration snippets for Swegon CASA R5H (SCB 3.0) over Modbus TCP/IP.

Files added:
- home_assistant/swegon_casa_modbus.yaml — Home Assistant modbus sensors, switches, inputs and automations for Swegon CASA R5H.

Usage:
1. Copy `home_assistant/swegon_casa_modbus.yaml` into your Home Assistant configuration directory (e.g. under `packages/` or include it from `configuration.yaml`).
2. Update the `host` under `modbus` to the IP address of your Swegon unit.
3. Restart Home Assistant.

Notes:
- Register addresses in this file follow the Swegon SCB 3.0 commissioning record; Home Assistant uses zero-based Modbus addressing so some registers are offset by -1.
- Test carefully and adapt scan intervals and register types to your setup.

License: MIT
