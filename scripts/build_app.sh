#!/bin/bash

pyinstaller -wF -i "icons/app-icon.ico" -n "StardewSaveEditor" --add-data "icons:icons" --add-data "docs:docs" runner.py