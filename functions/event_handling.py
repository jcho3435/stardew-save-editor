import os, re, webbrowser
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
        window[Keys._ValidateFolder].update(value="Save folder loaded. Backup created in backups folder", text_color="black")
        window[Keys._SaveWarning].update("Make sure to save all changes before loading a new save or closing the window.")

        window[Keys._FolderBrowser].update(disabled=True, button_color="gray")
        event_string += load_save_data(window, folderpath)
        set_visibility(window, Keys._EditorTabs, True)
        window[Keys._FarmersTab].select()
    else:                                           # Invalid folder name
        window[Keys._ValidateFolder].update(value="Invalid folder selected.", text_color="red")
        event_string = f"[{get_current_time()}] Invalid folder selection: {folderpath}\n\n"
    
    return event_string

def _Save_Changes_Event(window: sg.Window, values: dict) -> str:
    event_string = ""
    event_string += save_functions.save_farmers_tab_data_to_tree(values)

    character_data, world_data = get_xml_roots()

    folderpath = values[Keys._FolderInput]
    basename = os.path.basename(folderpath)
    character_save_file = os.path.join(folderpath, "SaveGameInfo")
    world_save_file = os.path.join(folderpath, basename)

    character_save_file = "save_data2/SaveGameInfo" #TODO: CHANGE THIS SHIT TO NOT BE HARDCODED
    world_save_file = "save_data2/MoreRice_363478863"

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
    
    window["Load"].select()
    window[Keys._ValidateFolder].update("Changes have been saved.")
    window[Keys._FolderBrowser].update(disabled=False, button_color="#283B5B")

    return event_string

def _Url_Event(event):
    url = event.split(' ')[1]
    webbrowser.open(url)

    return f"[{get_current_time()}] Opened page {url} in web browser.\n\n"

def _Switch_To_Friendship_Tab_Event(window: sg.Window, values: dict):
    old_val = values[Keys._FriendshipTabFarmerCombo]
    default_index = ""
    if old_val != "":
        default_index = old_val[-2]
    else:
        default_index = "1"

    farmers_names = []
    index = 0
    for key in Keys._FarmersTabFrames:
        if window[key].visible:
            farmers_names.append(f"{values[Keys._FarmerNames[index]]} (Farmer {index + 1})")
        index += 1

    window[Keys._FriendshipTabFarmerCombo].update(values=farmers_names, set_to_index=(int(default_index)-1)) #Change from 1 indexed for user to 0 indexed by python

    return f"[{get_current_time()}] Friendship tab combo box filled with most up to date entries for farmer names.\n\n" #TODO: THIS
    #needs to fill the combo box with the right names

def handle_event(window: sg.Window, event: str, values: dict) -> str:
    if event == Keys._FolderInput:
        return _Folder_Selection_Event(window, values)
    elif event == "Save Changes":
        return _Save_Changes_Event(window, values)
    elif event.startswith("URL "):
        return _Url_Event(event)
    elif event == Keys._TabGroup:
        event_string = f"[{get_current_time}] Switched to {values[event]} tab.\n\n"
        if values[event] == Keys._FriendshipTab:
            event_string += _Switch_To_Friendship_Tab_Event(window, values)
        return event_string