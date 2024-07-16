import PySimpleGUI as sg
import os, sys, datetime
import functions.program_lock as program_lock
import functions.log_functions as log_functions
from functions.functions import get_current_time, init_directories, create_backup
import constants
import re

init_directories()

if program_lock.is_running():
    program_lock.log_closed_run()
    sys.exit(1)

layout = [
    [sg.Push(), sg.Text("Stardew Valley Save Editor!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
    [sg.Text("Folder:", size=5), sg.Input(expand_x=True, key="_Folder", enable_events=True, disabled=True), sg.FolderBrowse("Select Save Folder")],
    [sg.Text("Note: By default, save folders are located at C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black", justification="center", expand_x=True)],
    [sg.Text("", size=5), sg.Text("", key="-VALID-", text_color="red")]
]

# Create the Window
window = sg.Window('Hello World!', layout, size=(1280, 720))
time = datetime.datetime.now()

event_string = ""
# Event Loop to process "events" and get the "values" of the inputs
try:
    event_string += f"Run {time} - - - - - - - - -\n\n"

    while True:
        event, values = window.read()
    
        event_string += f"[{get_current_time()}] Event: {event}\n[{get_current_time()}] Values: {values}\n\n"
        # if user closes window
        if event == sg.WIN_CLOSED:
            break

        if event == "_Folder":
            folderpath = values["_Folder"]
            foldername = os.path.basename(folderpath)
            if re.match(constants._SaveFolderRE, foldername):
                create_backup(folderpath)
            else:
                window["-VALID-"].update(f"Invalid folder selected.")
                event_string += f"[{get_current_time()}] Invalid folder selection: {folderpath}\n\n"

            # window["update"].update(window["update"].get() + values["Name"])

    window.close()
except Exception as e:
    log_functions.log_exceptions(e, time)
finally:
    log_functions.log_events(event_string, time)
    program_lock.clean_up()

if window.NumOpenWindows > 0:
    window.close()