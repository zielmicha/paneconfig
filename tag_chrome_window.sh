#!/bin/bash
xdotool key ctrl+b
for i in $(seq 10); do xdotool key Left; done 
xdotool key F2
xdotool type "$1"
xdotool key Return
