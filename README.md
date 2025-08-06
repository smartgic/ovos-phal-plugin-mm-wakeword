# PHAL plugin - MagicMirror² Wake Word

Display an image and a message on MagicMirror² when Open Voice OS is listening.

## About

[MagicMirror²](https://magicmirror.builders/) is an open source modular smart mirror platform. With a growing list of installable modules, the MagicMirror² allows you to convert your hallway or bathroom mirror into your personal assistant.

This PHAL plugin interacts with MagicMirror² to let you know if OVOS is listening. When a wake word is detected an image and message are displayed on the screen and when the recording is done the image and message disappear.

<img src='docs/screenshot.png' width='800'/>

## Installation

```shell
pip install ovos-phal-plugin-mm-wakeword
```

## Configuration

The plugin configuration file is `~/.config/OpenVoiceOS/ovos-phal-plugin-mm-wakeword.json`.

| Option    | Value                    | Description                           |
| --------- | ------------------------ | ------------------------------------- |
| `url`     | `http://localhost:8080`  | MagicMirror² URL                      |
| `key`     | `N/A`                    | MagicMirror² API key                  |
| `message` | `Listening...`           | Message displayed when triggered      |
| `timeout` | `10`                     | HTTP request timeout in seconds       |
| `verify`  | `false`                  | Verify SSL certificate                |

### Example

Configuration sample of `~/.config/OpenVoiceOS/ovos-phal-plugin-mm-wakeword.json`.

```json
{
  "url": "http://mm.home.lan",
  "key": "en323q9WBNMK3Q04WIPNEAsdfhesammhp44",
  "message": "Listening...",
  "timeout": 10,
  "verify": false
}
```

## MagicMirror² Configuration

In order to reach the `/ovos` route on your MagicMirror², you need to allow remote connections for a specific IP address or for a network range.

Please have a look here: https://github.com/smartgic/MMM-ovos-wakeword

## Credits

- [Smart'Gic](https://smartgic.io/)

## Category

**IoT**

## Tags

#smartmirror
#magicmirror
#wakeword
#raspberrypi
#smarthome
