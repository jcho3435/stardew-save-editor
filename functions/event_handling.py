import os, re, webbrowser
import PySimpleGUI as sg
from functions.functions import get_current_time, has_save_files
from functions.ui_functions import set_visibility, load_save_data
from functions.get_and_load_xml import get_xml_roots
import components.constants as constants, components.vars as vars
from components.constants import Keys
import functions.save_functions as save_functions
from lxml import etree
import functions.backups_functions as backups_functions

def _Folder_Selection_Event(window: sg.Window, values) -> str:
    event_string = ""
    folderpath = values[Keys._FolderInput]
    foldername = os.path.basename(folderpath)
    if re.match(vars._SaveFolderRE, foldername): # Valid folder name 
        valid, error_log, friendly_text = has_save_files(folderpath)
        if not valid:
            window[Keys._ValidateFolder].update(value=friendly_text, text_color="red")
            return error_log
        
        event_string += backups_functions.create_backup(window, folderpath)
        window[Keys._ValidateFolder].update(value="Save folder loaded. Backup created in backups folder", text_color="black")
        window[Keys._SaveWarning].update("Make sure to save all changes before loading a new save or closing the window.")

        window[Keys._FolderBrowser].update(disabled=True, button_color="gray")
        event_string += load_save_data(window, folderpath)
        set_visibility(window, Keys._EditorTabs, True)
        window[Keys._FarmersTab].select()
    else:                                           # Invalid folder name
        window[Keys._ValidateFolder].update(value="Invalid folder selected.", text_color="red")
        event_string = f"[{get_current_time()}] [LOAD] Invalid folder selection: {folderpath}\n\n"
    
    return event_string

def _Save_Changes_Event(window: sg.Window, values: dict) -> str:
    event_string = ""
    event_string += save_functions.save_farmers_tab_data_to_tree(values)
    event_string += save_functions.save_friendship_tab_data_to_tree()

    character_data, world_data = get_xml_roots()

    folderpath = values[Keys._FolderInput]
    basename = os.path.basename(folderpath)
    character_save_file = os.path.join(folderpath, "SaveGameInfo")
    world_save_file = os.path.join(folderpath, basename)

    # character_save_file = "save_data2/SaveGameInfo" #TODO: CHANGE THIS SHIT TO NOT BE HARDCODED
    # world_save_file = "save_data2/MoreRice_363478863"

    with open(character_save_file, 'wb') as file:
        #WRITE BOM CHARACTERS
        file.write(b'\xef\xbb\xbf')

        #write xml declaration
        file.write(vars._XML_DECLARATION.encode("utf-8"))

        # Serialize XML tree to bytes and write to file
        character_save_string = etree.tostring(character_data, encoding='utf-8', xml_declaration=False)
        file.write(character_save_string)

        event_string += f"[{get_current_time()}] [SAVE] Character save XML tree saved to character save file.\n"
    
    with open(world_save_file, 'wb') as file:
        #WRITE BOM CHARACTERS
        file.write(b'\xef\xbb\xbf')

        #write xml declaration
        file.write(vars._XML_DECLARATION.encode("utf-8"))
        
        # Serialize XML tree to bytes and write to file
        world_save_string = etree.tostring(world_data, encoding='utf-8', xml_declaration=False)
        file.write(world_save_string)

        event_string += f"[{get_current_time()}] [SAVE] World save XML tree saved to character save file.\n\n"
    
    window["Load"].select()
    window[Keys._ValidateFolder].update("Changes have been saved.")
    window[Keys._FolderBrowser].update(disabled=False, button_color="#283B5B")

    return event_string

def _Url_Event(event):
    url = event.split(' ')[1]
    webbrowser.open(url)

    return f"[{get_current_time()}] [LINK] Opened page {url} in web browser.\n\n"

def update_friendship_data_dict(values: dict): # Move this function elsewhere?
    oldIndex = vars._Get_Friendship_Tab_Old_Combo_Ind()
    data = vars._FriendshipData[oldIndex]

    for npc in data.keys():
        data[npc] = values[f"-{npc}Friendship-"]

def _Handle_Friendship_Tab_Display_Selection(window: sg.Window, values: dict):
    # Display the friendship data
    farmers: list[str] = window[Keys._FriendshipTabFarmerCombo].Values
    index = farmers.index(values[Keys._FriendshipTabFarmerCombo])

    if index != vars._Get_Friendship_Tab_Old_Combo_Ind():
        update_friendship_data_dict(values)
        friendshipData = vars._Get_Friendship_data()[index]

        for npc, points in friendshipData.items():
            window[Keys._NPCFriendshipPoints[npc]].update(points, disabled=False)

        npcs = friendshipData.keys()
        allnpcs = constants._AllFriendableNPCs
        locked = [npc for npc in allnpcs if npc not in npcs]

        for npc in locked:
            window[Keys._NPCFriendshipPoints[npc]].update("NPC Locked")

        vars._Set_Friendship_Tab_Old_Combo_Ind(index)

    return f"[{get_current_time()}] [UI] Displaying friendship data for {values[Keys._FriendshipTabFarmerCombo]}.\n\n"

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

    i = int(default_index)-1
    window[Keys._FriendshipTabFarmerCombo].update(values=farmers_names, set_to_index=i) #Change from 1 indexed for user to 0 indexed by python
    values[Keys._FriendshipTabFarmerCombo] = farmers_names[i]

    event_string = _Handle_Friendship_Tab_Display_Selection(window, values)

    vars._Set_Friendship_Tab_Old_Combo_Ind(i)

    return event_string + f"[{get_current_time()}] [UI] Friendship tab combo box filled with most recent entries for farmer names.\n\n"

def _Handle_Delete_Backup_Event(window: sg.Window, values: dict, event: str) -> str:
    if event == "Delete All Backups":
        return backups_functions._Delete_All_Backups_Event(window)
    elif event == "Delete Selected":
        return backups_functions._Delete_Selected_Backups_Event(window, values)
    elif event.startswith(f"{Keys._DeleteAllBackupsPrefix}:"):
        world = event.split(":")[-1]
        return backups_functions._Delete_All_Specific_World_Backups(window, world)
   

def handle_event(window: sg.Window, event: str, values: dict) -> str:
    if event == Keys._FolderInput:
        return _Folder_Selection_Event(window, values)
    elif event == "Save Changes":
        return _Save_Changes_Event(window, values)
    elif event.startswith("URL "):
        return _Url_Event(event)
    elif event == Keys._FriendshipTabFarmerCombo:
        return _Handle_Friendship_Tab_Display_Selection(window, values)
    elif event == Keys._TabGroup:
        event_string = f"[{get_current_time()}] [UI] Switched to {values[event]} tab.\n\n"
        if values[event] == Keys._FriendshipTab:
            event_string += _Switch_To_Friendship_Tab_Event(window, values)
        else:
            if vars._Get_Curr_Tab() == Keys._FriendshipTab:
                update_friendship_data_dict(values)
        vars._Set_Curr_Tab(values[event])
        return event_string
    elif event == "Delete Selected" or event == "Delete All Backups" or event.startswith(f"{Keys._DeleteAllBackupsPrefix}:"):
        return _Handle_Delete_Backup_Event(window, values, event)