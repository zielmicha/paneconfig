#!/bin/bash

WINDOW_ID=$id

xdotool windowfocus $WINDOW_ID
xdotool key --window $WINDOW_ID ctrl+l

for i in $(seq 1 30); do
    xdotool key --window $WINDOW_ID ctrl+l
    xdotool key --window $WINDOW_ID ctrl+c
    xclip -o; echo

    xdotool key --window $WINDOW_ID ctrl+Tab
done
