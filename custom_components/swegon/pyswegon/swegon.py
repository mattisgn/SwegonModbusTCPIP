"""
A minimal Swegon helper for the custom component.

This is a simplified, self-contained implementation intended to match
the interface used by the coordinator and entities in this integration.
It provides:
 - class Swegon(device_module, ip, port, slave_id)
 - Swegon.Datapoints dict with groups and entries that have a .Value attribute
 - async methods:
    readDeviceInfo, readSetpoints, readAlarms, readSensors, readCommands, readUnitStatuses
    readValue(group, key)
    writeValue(group, key, value)
 - getters: getModelName, getSerialNumber, getFW

Note: This is a basic stub implementation. For full functionality, replace
that file with the upstream implementation (uses pymodbus) from the upstream repo.
"""
import asyncio
import logging
from types import SimpleNamespace

_LOGGER = logging.getLogger(__name__)

def _v(value):
    return SimpleNamespace(Value=value)

class Swegon:
    def __init__(self, device_module, ip, port, slave_id):
        self.device_module = device_module
        self.ip = ip
        self.port = port
        self.slave_id = slave_id

        # Minimal datapoints structure used by the coordinator and entities
        self.Datapoints = {
            "Device_Info": {
                "FW_Maj": _v(0),
                "Model": _v("Unknown"),
                "Serial": _v("0000"),
                "FW": _v("0.0.0"),
            },
            "Config": {
                "Config_Value": _v(0),
            },
            "Alarms": {
                "Active_Alarms": _v(False),
            },
            "Sensors": {
                "Fresh_Temp": _v(None),
                "Supply_Temp1": _v(None),
                "Supply_Temp2": _v(None),
                "Extract_Temp": _v(None),
                "Exhaust_Temp": _v(None),
                "UP1_Temp": _v(None),
                "RH": _v(None),
                "AH": _v(None),
            },
            "Sensors2": {
                "Heat_Exchanger": _v(None),
            },
            "UnitStatuses": {
                "Supply_Fan": _v(None),
                "Exhaust_Fan": _v(None),
                "Heating_Output": _v(None),
            },
            "VirtualSensors": {
                "Efficiency": _v(None),
            },
            "Commands": {
                "Op_Mode": _v(0),
                "Fireplace_Mode": _v(0),
                "Travelling_Mode": _v(0),
            },
            "Setpoints": {
                "Temp_SP": _v(20.0),
            }
        }

    async def readDeviceInfo(self):
        # Populate device info with dummy values (replace with real Modbus reads)
        await asyncio.sleep(0)
        self.Datapoints["Device_Info"]["FW_Maj"].Value = 1
        self.Datapoints["Device_Info"]["Model"].Value = "CASA R5H"
        self.Datapoints["Device_Info"]["Serial"].Value = "SN12345678"
        self.Datapoints["Device_Info"]["FW"].Value = "1.0.0"
        _LOGGER.debug("readDeviceInfo called")

    async def readSetpoints(self):
        await asyncio.sleep(0)
        # leave Temp_SP as-is or update from device
        _LOGGER.debug("readSetpoints called")

    async def readAlarms(self):
        await asyncio.sleep(0)
        # Example: no alarms
        self.Datapoints["Alarms"]["Active_Alarms"].Value = False
        _LOGGER.debug("readAlarms called")

    async def readSensors(self):
        await asyncio.sleep(0)
        # Populate some example sensor values (should be replaced with actual reads)
        self.Datapoints["Sensors"]["Fresh_Temp"].Value = 18.5
        self.Datapoints["Sensors"]["Supply_Temp1"].Value = 19.5
        self.Datapoints["Sensors"]["Supply_Temp2"].Value = 20.0
        self.Datapoints["Sensors"]["Extract_Temp"].Value = 21.0
        self.Datapoints["Sensors"]["Exhaust_Temp"].Value = 22.0
        self.Datapoints["Sensors"]["UP1_Temp"].Value = 21.5
        self.Datapoints["Sensors"]["RH"].Value = 45.0
        self.Datapoints["Sensors"]["AH"].Value = 7.8
        self.Datapoints["Sensors2"]["Heat_Exchanger"].Value = 85
        self.Datapoints["UnitStatuses"]["Supply_Fan"].Value = 50
        self.Datapoints["UnitStatuses"]["Exhaust_Fan"].Value = 48
        self.Datapoints["UnitStatuses"]["Heating_Output"].Value = 0
        self.Datapoints["VirtualSensors"]["Efficiency"].Value = 78
        _LOGGER.debug("readSensors called")

    async def readCommands(self):
        await asyncio.sleep(0)
        # Commands reflect current values
        _LOGGER.debug("readCommands called")

    async def readUnitStatuses(self):
        await asyncio.sleep(0)
        _LOGGER.debug("readUnitStatuses called")

    async def readValue(self, group, key):
        await asyncio.sleep(0)
        # If the key exists, do nothing; else create default
        if group in self.Datapoints and key in self.Datapoints[group]:
            return self.Datapoints[group][key].Value
        return None

    async def writeValue(self, group, key, value):
        await asyncio.sleep(0)
        if group in self.Datapoints and key in self.Datapoints[group]:
            self.Datapoints[group][key].Value = value
        else:
            # create if missing
            if group not in self.Datapoints:
                self.Datapoints[group] = {}
            self.Datapoints[group][key] = _v(value)
        _LOGGER.debug("writeValue: %s %s -> %s", group, key, value)

    def getModelName(self):
        return self.Datapoints["Device_Info"]["Model"].Value

    def getSerialNumber(self):
        return self.Datapoints["Device_Info"]["Serial"].Value

    def getFW(self):
        return self.Datapoints["Device_Info"]["FW"].Value
