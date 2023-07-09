#!/bin/bash


sed -i -r 's/\"([0-9A-F])/"#\1/g' colors.py
