import PySimpleGUI as sg
import sys, datetime
import functions.program_lock as program_lock
import functions.log_functions as log_functions
from functions.functions import get_current_time, init_directories
from functions.event_handling import handle_event
from components.constants import Keys

init_directories()

if program_lock.is_running():
    program_lock.log_closed_run()
    sys.exit(123)

layout = []
window = None
try:
    load_layout = [
        [sg.Push(), sg.Text("Stardew Valley Save Editor!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
        [sg.Text("Folder:", size=5), sg.Input(expand_x=True, key=Keys._FolderInput, enable_events=True, disabled=True), sg.FolderBrowse("Select Save Folder")],
        [sg.Text("Note: By default, save folders are located at C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black", justification="center", expand_x=True)],
        [sg.Column([[sg.Text("", size=4), sg.Text("", key=Keys._ValidateFolder)]])],
    ]

    editor_layout = [
        [sg.Button("Save Changes")]
        #Figure out how to save - this comes later
        # Track whether there have been changes since last save
        # need to use tabs  - replace all visibility things with tab groups instead
    ]

    layout = [
        [sg.TabGroup([[
            sg.Tab("Load", load_layout), 
            sg.Tab("Edit", editor_layout, visible=False)
            ]], expand_x=True, expand_y=True)]
    ]

    # Create the Window
    window = sg.Window('Hello World!', layout, use_ttk_buttons=True, size=(1280, 720))
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
        else:
            event_string += handle_event(window, event, values)


    window.close()
except Exception as e:
    log_functions.log_exceptions(e, time)
finally:
    log_functions.log_events(event_string, time)
    program_lock.clean_up()

if window.NumOpenWindows > 0:
    window.close()