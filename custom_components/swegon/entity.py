"""Minimal base entity placeholder."""
import logging
from homeassistant.helpers.update_coordinator import CoordinatorEntity

_LOGGER = logging.getLogger(__name__)

class SwegonBaseEntity(CoordinatorEntity):
    def __init__(self, coordinator, swegonentity):
        super().__init__(coordinator)
        self._group = getattr(swegonentity, 'group', None)
        self._key = getattr(swegonentity, 'key', None)
        self._extra_state_attributes = {}
        self._attr_name = getattr(swegonentity, 'entityName', 'Swegon')

    @property
    def extra_state_attributes(self):
        return self._extra_state_attributes
