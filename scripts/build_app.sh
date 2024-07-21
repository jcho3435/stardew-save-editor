#!/bin/bash

# I'm running this with git bash
# App made for windows, has a script folder with both a windows script and a bash script. Smart. I know.

name="StardewSaveEditor"
pyinstaller -wF -i "icons/app-icon.ico" -n "$name" --add-data "icons:icons" --add-data "docs:docs" runner.py


cp scripts/clean_logs.bat dist/

mv dist/ $name/