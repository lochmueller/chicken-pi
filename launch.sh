#!/bin/sh

# active w1-therm
sudo modprobe w1-therm

DIR="$(dirname "$0")"
cd $DIR
FLASK_APP=main nohup flask run -h 0.0.0.0 > log.txt 2>&1 &