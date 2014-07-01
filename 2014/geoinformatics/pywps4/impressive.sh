#!/bin/sh

xrandr --output LVDS1 --mode 1024x768 --output HDMI1 --mode 1024x768 --right-of LVDS1

impressive -g 2048x768 cepicky-pywps4.pdf
