#!/bin/bash


sed -i -r 's/\"([0-9A-Fa-f])/"#\1/g' colors.py
