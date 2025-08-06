"""MagicMirror² wake word detection PHAL plugin"""

import json
import requests

from json_database import JsonConfigXDG
from ovos_plugin_manager.phal import PHALPlugin
from ovos_utils.log import LOG


class MmWakewordPlugin(PHALPlugin):
    """This is the place where all the magic happens for the
    MagicMirror² wake word PHAL plugin.
    """

    def __init__(self, bus=None, config=None):
        super().__init__(bus=bus, name="ovos-phal-plugin-mm-wakeword", config=config)

        # Retrieves settings from ~/.config/OpenVoiceOS/ovos-phal-plugin-mm-wakeword.json
        self.settings = JsonConfigXDG(self.name, subfolder="OpenVoiceOS")
        
        # Initialize variables with empty or None values
        self.headers = {}
        
        # Setup the plugin
        self.setup()

        # Map bus events to methods
        self.bus.on("recognizer_loop:record_begin", self._handle_listener_started)
        # self.bus.on("recognizer_loop:record_end", self._handle_listener_ended)
        self.bus.on("recognizer_loop:audio_output_end", self._handle_listener_ended)
        # self.bus.on("ovos.utterance.cancelled", self._handle_listener_ended)

    def setup(self):
        """Check for settings requirements and prepare HTTP headers once
        configured.
        """
        if not self.settings.get("url") or not self.settings.get("key"):
            LOG.warning("MagicMirror² address or API key not defined - plugin will not function")
            LOG.warning("Please configure url and key in ~/.config/OpenVoiceOS/ovos-phal-plugin-mm-wakeword.json")
        else:
            self.headers["Content-Type"] = "application/json"
            self.headers["X-Api-Key"] = self.settings.get("key")
            LOG.info("MagicMirror² address: %s", self.settings.get("url"))

    def http_endpoint(self, payload):
        """Handle HTTP request to the MagicMirror² endpoint."""
        if not self.settings.get("url") or not self.settings.get("key"):
            LOG.warning("MagicMirror² not configured - skipping HTTP request")
            return
            
        try:
            requests.post(
                url=self.settings.get("url") + "/ovos",
                data=json.dumps(payload),
                headers=self.headers,
                verify=self.settings.get("verify", False),
                timeout=self.settings.get("timeout", 10),
            )
        except requests.exceptions.RequestException as err:
            LOG.error("Failed to send request to MagicMirror²: %s", err)

    def _handle_listener_started(self, _):
        """Handle the record_begin event detection."""
        payload = {"notification": "OVOS_SEND_MESSAGE", "payload": self.settings.get("message", "Listening...")}
        self.http_endpoint(payload)

    def _handle_listener_ended(self, _):
        """Handle the record_end and other events that end listening."""
        payload = {"notification": "OVOS_DELETE_MESSAGE", "payload": "delete"}
        self.http_endpoint(payload)
