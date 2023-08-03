#!/bin/bash

gnome-terminal --title="RandomNameGenerator" -- bash -c "python RandomNameGenerator/server.py; exec bash"
gnome-terminal --title="DogoBase" -- bash -c "python DogoBase/server.py; exec bash"
