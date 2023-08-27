# Chicken Pi

Dieses Projekt ist der aktuelle Stand von "Chicken Pi", als Digitalisierung eines Hühnerstalls inkl. Integration ins Smart Home.
Weitere Informationen auf https://360friends.de/tag/chicken-pi/

## Installation

Installation via `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/lochmueller/chicken-pi/main/install.sh)"` auf einem Raspberry Pi.

## Benutzung

Beispiele:

`curl http://192.168.178.106:5000/light`
`curl http://192.168.178.106:5000/light?state=on -X POST`

## Dev

Connect to current Pi: `ssh chicken.local`
