#!/bin/bash

# format hex strings in metalmaps/colors.py to start with a #

sed -i -r 's/\"([0-9A-Fa-f])/"#\1/g' metalmaps/colors.py
