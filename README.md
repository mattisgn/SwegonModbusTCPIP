# SwegonModbusTCPIP

Home Assistant custom component for Swegon CASA R5H (SCB 3.0) over Modbus TCP/IP.

This integration provides sensors, switches, select dropdowns, and number controls to monitor and control Swegon ventilation units via Modbus TCP protocol entirely through the Home Assistant UI.

## Installation

### Via HACS

1. In Home Assistant, go to **HACS** → **Integrations**
2. Click the three dots menu (⋯) → **Custom repositories**
3. Add repository: `https://github.com/mattisgn/SwegonModbusTCPIP`
4. Select category: **Integration**
5. Click **Install**
6. Restart Home Assistant

### Manual Installation

Copy the `custom_components/swegon_modbus/` directory to your Home Assistant `custom_components/` folder:

```
~/.homeassistant/custom_components/swegon_modbus/
```

## Configuration

1. Go to Home Assistant **Settings** → **Devices & Services** → **Integrations**
2. Click **Create Integration** or the **+** button
3. Search for "Swegon Modbus TCP/IP"
4. Fill in the configuration:
   - **Name**: Display name for your Swegon unit (default: "Swegon CASA")
   - **Host**: IP address of your Swegon CASA unit (e.g., `192.168.1.111`)
   - **Port**: Modbus TCP port (default: `502`)
5. Click **Create**
6. Restart Home Assistant

## Features

### Sensors (Read-Only)
- **Temperatures**: Fresh air, supply, extract, and exhaust air temperatures (°C)
- **Fan Speeds**: Supply and exhaust fan RPM
- **Rotor Speed**: Rotary heat exchanger RPM (R5H models)
- **Status**: Operating mode status, filter guard information
- **Setpoint Readback**: Current temperature setpoint (°C)

### Switches (On/Off Control)
- **Smart Mode**: Enable/disable smart ventilation control
- **Fireplace Mode**: Toggle fireplace ventilation boost

### Select (Multiple Options)
- **Operating Mode**: Select from Stopped, Away, Home, Boost, or Travelling

### Number (Adjustable Values)
- **Temperature Setpoint**: Adjust target temperature (13–25°C)

## Register Addressing

All register addresses follow the Swegon SCB 3.0 commissioning record with zero-based Modbus addressing:
- **Input Registers (3x)**: Offset by -1 (e.g., 3x6201 → address 6200)
- **Holding Registers (4x)**: Offset by -1 (e.g., 4x5101 → address 5100)

## Notes

- Ensure your Swegon unit is accessible on your network and configured for Modbus TCP on port 502
- Register addresses are based on Swegon CASA Smart SCB 3.0 specifications
- Temperature values are scaled by 0.1 (e.g., Modbus value 215 = 21.5°C)
- Setpoint write values are scaled by 10 (e.g., 21.5°C = 215)

## Requirements

- Home Assistant 2023.1.0 or later
- `pymodbus>=3.1.0`

## License

MIT

## Credits

Adapted from [Ztaeyn/HomeAssistant-VTR-Modbus](https://github.com/Ztaeyn/HomeAssistant-VTR-Modbus)
