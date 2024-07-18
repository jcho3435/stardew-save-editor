import os, re
import PySimpleGUI as sg
from functions.functions import get_current_time, create_backup, has_save_files
from functions.ui_functions import set_visibility, load_save_data
import components.constants as constants
from components.constants import Keys

def _Folder_Selection_Event(window: sg.Window, values) -> str:
    event_string = ""
    folderpath = values[Keys._FolderInput]
    foldername = os.path.basename(folderpath)
    if re.match(constants._SaveFolderRE, foldername): # Valid folder name 
        valid, error_log, friendly_text = has_save_files(folderpath)
        if not valid:
            window[Keys._ValidateFolder].update(value=friendly_text, text_color="red")
            return error_log
        
        event_string = create_backup(folderpath)
        window[Keys._ValidateFolder].update(value="Save folder loaded.", text_color="black")

        load_save_data(window, folderpath)
        set_visibility(window, "Edit", True)
        window["Edit"].select()
    else:                                           # Invalid folder name
        window[Keys._ValidateFolder].update(value="Invalid folder selected.", text_color="red")
        event_string = f"[{get_current_time()}] Invalid folder selection: {folderpath}\n\n"
    
    return event_string

def _Save_Changes_Event(window: sg.Window):
    pass


def handle_event(window: sg.Window, event: str, values: dict) -> str:
    if event == Keys._FolderInput:
        return _Folder_Selection_Event(window, values)
    elif event == "Save Changes":
        return _Save_Changes_Event(window)
