#!/bin/sh

# active w1-therm
sudo modprobe w1-therm

DIR="$(dirname "$0")"
cd $DIR
nohup flask run -h 0.0.0.0 > logs/flask.txt 2>&1 &