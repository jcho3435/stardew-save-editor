# Stardew Valley Save Editor

This editor is for windows because I don't want to think about other operating systems.<br>
<br>
Version info:<br>
Python version: 3.12.4<br>
Platform: Windows<br>
Port: PySimpleGUI<br>
tkinter version: 8.6.13<br>
PySimpleGUI version: 5.0.6.12<br>


All error logs and event logs are located in `logs/`<br>
Logs can be cleaned by running `clean_logs.bat`, located in scripts/

Construct app using `scripts/build_app.sh`.<br>

## Application Features:
 - Creating backups: Save files are backed up every time they are loaded. You can find your save files in the backups directory. Backups are never automatically deleted.<br>
 - Change profile information for all players who have joined your world, including:<br>
   - Farmer name<br>
   - Farmer skill levels<br>
   - Farmer skill experience<br>
 - Change friendship points with NPCs for all players who have joined your world.<br>
 - Backup manager: allows for deleting all backups, deleting all backups of a specific farm, or deleting selected backups.<br>

## Download:
Click on <a href="https://github.com/jcho3435/stardew-save-editor/releases">releases</a> to find a version to download.

When running the app, you will likely get a popup from Windows Defender SmartScreen. To get around the popup, click <u>More Info</u>, then click <u>run anyway</u><br>
This popup appears because I do not have a digital certificate for this app (they are very expensive and outside my budget).

When you first run the app, you will get a PySimpleGUI window asking you for a license. You will need to create an account, so follow the link provided and create a free hobbyist account in order to get a license.<br>
This is also needed because I don't want to spend $100/year on the PySimpleGUI commercial license when I do not intend to make money off of my work.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). See the [LICENSE](LICENSE) file for details.
