import os, re
import PySimpleGUI as sg
from functions.functions import get_current_time, create_backup, has_save_files
from functions.ui_functions import set_visibility, load_save_data
from functions.get_and_load_xml import get_xml_roots
import components.constants as constants
from components.constants import Keys
import functions.save_functions as save_functions
from lxml import etree

def _Folder_Selection_Event(window: sg.Window, values) -> str:
    event_string = ""
    folderpath = values[Keys._FolderInput]
    foldername = os.path.basename(folderpath)
    if re.match(constants._SaveFolderRE, foldername): # Valid folder name 
        valid, error_log, friendly_text = has_save_files(folderpath)
        if not valid:
            window[Keys._ValidateFolder].update(value=friendly_text, text_color="red")
            return error_log
        
        event_string += create_backup(folderpath)
        window[Keys._ValidateFolder].update(value="Save folder loaded.", text_color="black")

        window[Keys._FolderBrowser].update(disabled=True, button_color="gray")
        event_string += load_save_data(window, folderpath)
        set_visibility(window, "Farmer", True)
        window["Farmer"].select()
    else:                                           # Invalid folder name
        window[Keys._ValidateFolder].update(value="Invalid folder selected.", text_color="red")
        event_string = f"[{get_current_time()}] Invalid folder selection: {folderpath}\n\n"
    
    return event_string

def _Save_Changes_Event(window: sg.Window, values: dict) -> str:
    event_string = ""
    event_string += save_functions.save_farmer_data_to_tree(window)


    character_data, world_data = get_xml_roots()

    character_save_file = "save_data/SaveGameInfo" #TODO: CHANGE THIS SHIT TO NOT BE HARDCODED
    world_save_file = "save_data/ChingChong_363368866"

    with open(character_save_file, 'wb') as file:
        #WRITE BOM CHARACTERS
        file.write(b'\xef\xbb\xbf')

        #write xml declaration
        file.write(constants._XML_DECLARATION.encode("utf-8"))

        # Serialize XML tree to bytes and write to file
        character_save_string = etree.tostring(character_data, encoding='utf-8', xml_declaration=False)
        file.write(character_save_string)

        event_string += f"[{get_current_time()}] Character save XML tree saved to character save file.\n"
    
    with open(world_save_file, 'wb') as file:
        #WRITE BOM CHARACTERS
        file.write(b'\xef\xbb\xbf')

        #write xml declaration
        file.write(constants._XML_DECLARATION.encode("utf-8"))
        
        # Serialize XML tree to bytes and write to file
        world_save_string = etree.tostring(world_data, encoding='utf-8', xml_declaration=False)
        file.write(world_save_string)

        event_string += f"[{get_current_time()}] World save XML tree saved to character save file.\n\n"
        

    return event_string

def handle_event(window: sg.Window, event: str, values: dict) -> str:
    if event == Keys._FolderInput:
        return _Folder_Selection_Event(window, values)
    elif event == "Save Changes":
        return _Save_Changes_Event(window, values)
