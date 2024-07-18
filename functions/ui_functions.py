import PySimpleGUI as sg
from components.constants import Keys
from functions.functions import get_xml_roots, get_current_time

def hide_rows(window: sg.Window, keys: list | str):
    if type(keys) == str:
        window[keys].hide_row()
    else:
        for key in keys:
            window[key].hide_row()

def unhide_rows(window: sg.Window, keys: list | str):
    if type(keys) == str:
        window[keys].unhide_row()
    else:
        for key in keys:
            window[key].unhide_row()

def set_visibility(window: sg.Window, keys: list | str, isVisible: bool):
    if type(keys) == str:
        window[keys].update(visible = isVisible)
    else:
        for key in keys:
            window[key].update(visible = isVisible)



#loading save data
def _load_profile_data(window: sg.Window, folderpath: str) -> str:
    event_string = ""
    window[Keys._FarmerName].update(default_text = "")

def load_save_data(window: sg.Window, folderpath: str) -> str:
    event_string = ""
    
    character_save, world_save, e_string = get_xml_roots(folderpath)

    
    event_string += _load_profile_data(window, folderpath)