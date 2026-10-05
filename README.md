# SwegonModbusTCPIP

Home Assistant custom component for Swegon CASA R5H (SCB 3.0) over Modbus TCP/IP.

This integration provides sensors, switches, and automations to monitor and control Swegon ventilation units via Modbus TCP protocol.

## Installation

### Via HACS

1. In Home Assistant, go to **HACS** → **Integrations**
2. Click the three dots menu (⋯) → **Custom repositories**
3. Add repository: `https://github.com/mattisgn/SwegonModbusTCPIP`
4. Select category: **Integration**
5. Click **Install**
6. Restart Home Assistant

### Manual Installation

Copy the `custom_components/swegon_modbus/` directory to your Home Assistant `custom_components/` folder.

## Configuration

1. Copy `custom_components/swegon_modbus/swegon_casa_modbus.yaml` into your Home Assistant configuration directory (e.g. `packages/` or include it from `configuration.yaml`).

2. Update the `host` under `modbus` to the IP address of your Swegon unit:
   ```yaml
   modbus:
     - name: swegon_casa
       type: tcp
       host: YOUR.SWEGON.IP.ADDRESS  # Change this
       port: 502
   ```

3. Include the configuration in `configuration.yaml`:
   ```yaml
   homeassistant:
     packages:
       swegon: !include packages/swegon_casa_modbus.yaml
   ```

4. Restart Home Assistant.

## Features

### Sensors
- Fresh air, supply, extract, and exhaust air temperatures
- Supply and exhaust fan RPM
- Rotor RPM (for R5H heat exchanger)
- Operating mode status
- Filter guard information
- Temperature setpoint readback

### Switches
- Smart Mode control
- Fireplace Mode toggle

### Controls
- Operating mode selector (Stopped, Away, Home, Boost, Travelling)
- Temperature setpoint (13–25°C)

### Automations
- Sync operating mode between dashboard and Swegon unit
- Sync temperature setpoint to Modbus
- Reflect unit status back to dashboard

## Register Addressing

Register addresses in this configuration follow the Swegon SCB 3.0 commissioning record. Home Assistant uses zero-based Modbus addressing, so:
- Input Registers (3x) are offset by -1 (e.g. 3x6201 → address 6200)
- Holding Registers (4x) are offset by -1 (e.g. 4x5101 → address 5100)

## Notes

- Test carefully and adapt scan intervals to your setup.
- Ensure your Swegon unit is configured for Modbus TCP on port 502.
- Register addresses are based on Swegon CASA Smart SCB 3.0 specifications.

## License

MIT

## Credits

Adapted from [Ztaeyn/HomeAssistant-VTR-Modbus](https://github.com/Ztaeyn/HomeAssistant-VTR-Modbus)
