# Changelog

## [0.1.0a1](https://github.com/smartgic/ovos-phal-plugin-mm-wakeword/tree/0.1.0a1) (2024-08-05)

**Initial Release:**

- Converted from OVOS skill to PHAL plugin architecture
- Maintains all original MagicMirror² integration functionality
- Uses JsonConfigXDG for configuration management
- Supports wake word detection events and audio output events
- Compatible with existing MMM-ovos-wakeword MagicMirror² module

**Features:**

- Display "Listening" message on MagicMirror² when wake word is detected
- Automatically remove message when listening ends
- Configurable HTTP timeout and SSL verification
- Comprehensive error handling and logging

**Configuration:**

- Configuration file: `~/.config/OpenVoiceOS/ovos-phal-plugin-mm-wakeword.json`
- Required settings: `url` and `key`
- Optional settings: `timeout` (default: 10s), `verify` (default: false)

\* *This Changelog was automatically generated*
