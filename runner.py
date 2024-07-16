import PySimpleGUI as sg
import os, sys, datetime
import functions.program_lock as program_lock
import functions.functions as functions

functions.init_directories()

if program_lock.is_running():
    program_lock.log_closed_run()
    sys.exit(1)

layout = [
    [sg.Push(), sg.Text("Stardew Valley Save Editor!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
    [sg.Text("Folder:"), sg.Input(expand_x=True, key="_folder", enable_events=True, disabled=True), sg.FolderBrowse("Select Save Folder")],
    [sg.Text("Note: Save folders are found in C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black", justification="center", expand_x=True)],
]

# Create the Window
window = sg.Window('Hello World!', layout, size=(1280, 720))

# Event Loop to process "events" and get the "values" of the inputs
try:
    time = datetime.datetime.now()
    fname = f"EventLog_{time.year}-{time.month}-{time.day}.log"
    f = open(f"logs\\{fname}", "a")
    f.write(f"Run {time} - - - - - - - - -\n\n")
    while True:
        event, values = window.read()

        f.write(f"Event: {event}\nValues: {values}\n\n")
        # if user closes window
        if event == sg.WIN_CLOSED:
            break

        if event == "Submit":
            window["update"].update(window["update"].get() + values["Name"])

    window.close()
except Exception as e:
    functions.log_exceptions(e)
finally:
    f.write("\n")
    f.close()
    program_lock.clean_up()

if window.NumOpenWindows > 0:
    window.close()