from functions.functions import get_current_time, init_directories

#Initialize backups and log directories if they do not already exist
# it is necessary for the directories to be initialized before the imports
init_directories()

import PySimpleGUI as sg
import sys, datetime
import functions.program_lock as program_lock
import functions.log_functions as log_functions
from functions.event_handling import handle_event
from components.constants import Keys
import components.vars as vars

# Program lock allows only one instance of the program to be running at a time. Lock file created in tmp/
if program_lock.is_running():
    program_lock.log_closed_run()
    sg.popup("The program was automatically closed due to an instance already being run.\nIf this is a mistake, delete 'tmp/program.lock' then run the program again.", title="Duplicate Run Detected")
    sys.exit(123)

vars._Set_Curr_Tab(Keys._LoadTab)

window = None
try:
    from components.ui_layout import layout

    # Create the Window
    window = sg.Window('Stardew Valley Save Editor', layout, use_ttk_buttons=True, icon="icons/app-icon.ico", resizable=True, finalize=True)
except Exception as e:
    program_lock.clean_up(e)

time = datetime.datetime.now()

event_string = ""

# Event Loop to process "events" and get the "values" of the inputs
try:
    event_string += f"Run {time} - - - - - - - - -\n\n"

    while True:
        event, values = window.read()
    
        event_string += f"[{get_current_time()}] [INTERNAL] Event: {event}\n{' '*22}Values: {values}\n\n"
        print(f"Event: {event}\nValues: {values}\n\n") # TODO: DELETE THIS LINE WHEN DONE DEBUGGING/TESTING

        # if user closes window, exit
        if event == sg.WIN_CLOSED:
            break
        else:
            event_string += handle_event(window, event, values)

    window.close()
except Exception as e:
    event_string += log_functions.log_exceptions(e, time)
finally:
    log_functions.log_events(event_string, time)
    program_lock.clean_up()

if not window.was_closed():
    window.close()