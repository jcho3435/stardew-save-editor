import PySimpleGUI as sg
import os, sys, datetime
import functions.program_lock as program_lock
import functions.log_functions as log_functions
from functions.functions import get_current_time, init_directories, create_backup, switch_view, hide_rows, unhide_rows, set_visibility
import components.constants as constants
from components.views import View
import re

init_directories()

if program_lock.is_running():
    program_lock.log_closed_run()
    sys.exit(123)

layout = []
window = None
try:
    load_layout = [
        [sg.Push(), sg.Text("Stardew Valley Save Editor!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
        [sg.Text("Folder:", size=5), sg.Input(expand_x=True, key="-FOLDER-", enable_events=True, disabled=True), sg.FolderBrowse("Select Save Folder")],
        [sg.Text("Note: By default, save folders are located at C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black", justification="center", expand_x=True)],
        [sg.Column([[sg.Text("", size=4), sg.Text("Invalid folder selected.", text_color="red")]], visible=False, key="-INVALID-")]
    ]

    editor_layout = [
        [sg.Button("Load Save"), sg.Button("Save Changes")]
        #Figure out how to save - this comes later
        # Track whether there have been changes since last save
    ]

    layout = [
        [sg.Column(load_layout, key="-LOAD-", expand_x=True)],
        [sg.Column(editor_layout, key="-EDITOR-", expand_x=True, visible=False)],
        [sg.Text("Random")]
    ]

    # Create the Window
    window = sg.Window('Hello World!', layout, size=(1280, 720))
    hide_rows(window, ["-EDITOR-", "-INVALID-"])
except Exception as e:
    program_lock.clean_up(e)

time = datetime.datetime.now()

event_string = ""

# Event Loop to process "events" and get the "values" of the inputs
try:
    event_string += f"Run {time} - - - - - - - - -\n\n"

    while True:
        event, values = window.read()
    
        event_string += f"[{get_current_time()}] Event: {event}\n[{get_current_time()}] Values: {values}\n\n"
        print(f"[{get_current_time()}] Event: {event}\n[{get_current_time()}] Values: {values}\n\n") # TODO: DELETE THIS LINE WHEN DONE DEBUGGING/TESTING
        # if user closes window, exit
        if event == sg.WIN_CLOSED:
            break

        if event == "-FOLDER-":
            folderpath = values["-FOLDER-"]
            foldername = os.path.basename(folderpath)
            if re.match(constants._SaveFolderRE, foldername): # Valid folder name 
                set_visibility(window, ["-INVALID-"], False)
                hide_rows(window, ["-INVALID-"])
                event_string += create_backup(folderpath)
                switch_view(window, View.EDITOR)
            else:                           # Invalid folder name
                set_visibility(window, ["-INVALID-"], True)
                unhide_rows(window, ["-INVALID-"])
                event_string += f"[{get_current_time()}] Invalid folder selection: {folderpath}\n\n"
                


    window.close()
except Exception as e:
    log_functions.log_exceptions(e, time)
finally:
    log_functions.log_events(event_string, time)
    program_lock.clean_up()

if window.NumOpenWindows > 0:
    window.close()