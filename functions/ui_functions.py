import PySimpleGUI as sg
from components.constants import Keys, CharacterSavePaths, WorldSavePaths
from functions.functions import get_current_time
from functions.get_and_load_xml import load_xml_roots, get_xml_roots
from lxml import etree
from components.ui_layout import enable_farmer_frame

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
def _load_profile_data(window: sg.Window) -> str:
    event_string = ""
    character_save, world_save = get_xml_roots()

    #Load host farmer
    farmer_name = character_save.xpath(CharacterSavePaths._FarmerName)[0].text
    enable_farmer_frame(window, farmer_name, 0)

    farmhands_names = world_save.xpath(WorldSavePaths._FarmhandsNames) # returns a list of tags <name>
    index = 1
    for tag in farmhands_names:
        name = tag.text
        enable_farmer_frame(window, name, index)
        index += 1

    event_string = f"[{get_current_time}] Profile data loaded.\n\n"

    return event_string

def load_save_data(window: sg.Window, folderpath: str) -> str:
    event_string = ""
    
    # load xml
    event_string += load_xml_roots(folderpath)
    
    event_string += _load_profile_data(window)

    return event_string