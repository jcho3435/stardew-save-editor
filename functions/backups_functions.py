from functions.functions import get_current_time
import PySimpleGUI as sg
import os, shutil, datetime
import elevate
import components.vars as vars
from components.constants import Keys
from components.ui_layout import createBackupFrame

def create_backup(window: sg.Window, folderpath: str) -> str:
    name = os.path.basename(folderpath)
    time = datetime.datetime.now()

    event_string = ""

    backup_name = f"{name}_{int(time.timestamp())}"
    backup_path = f"backups/{name}_backups/{backup_name}"
    os.makedirs(backup_path, exist_ok=True)
       
    for filename in os.listdir(folderpath):
        src_path = os.path.join(folderpath, filename)
        dst_path = os.path.join(backup_path, filename)

        shutil.copy(src_path, dst_path)

        event_string += f"[{get_current_time()}] [BACKUPS] Copied {filename} from {folderpath} to {backup_path}\n"

    event_string += "\n"

    # Update backup manager tab
    backups = vars._Get_Backups_Dict()
    if name in backups.keys():
        if backups[name]: #Backup frame exists and is active
             vals: list = window[f"{Keys._BackupsTabListboxPrefix}:{name}"].Values
             window[f"{Keys._BackupsTabListboxPrefix}:{name}"].update(values=vals + [backup_name])
        else: #Backup frame exists but is not active - this means the listbox is empty and the frame is invisible
            window[f"{Keys._BackupsTabFramePrefix}:{name}"].update(visible=True)
            window[f"{Keys._BackupsTabFramePrefix}:{name}"].unhide_row()
            window[f"{Keys._BackupsTabListboxPrefix}:{name}"].update(values=[backup_name])
            backups[name] = True
    else: #Backup frame does not exist - create new frame
        window.extend_layout(window[Keys._BackupsTabFramesColumn], [[createBackupFrame(name, [backup_name])]])
        backups[name] = True

    event_string += f"[{get_current_time()}] [BACKUPS] Backups manager tab updated.\n\n"
    return event_string

def _Delete_All_Backups_Event(window: sg.Window) -> str:
    event_string = f"[{get_current_time()}] [BACKUPS] Generating all backups deletion popup.\n"
    response = sg.popup_yes_no("Are you sure you want to PERMANENTLY delete all backups?", "WARNING: This action cannot be undone.", title="Delete all backups?")
    if response == "Yes":
        event_string += f"[{get_current_time()}] [BACKUPS] User confirmed deletion of backups.\n"
        try:
            for folder in os.listdir("backups"):
                shutil.rmtree(f"backups/{folder}")
        except PermissionError as e:
            event_string += f"[{get_current_time()}] [BACKUPS] Permission error encountered while trying to delete backups. Requesting elevated permissions, then trying again.\n"
            elevate.elevate()
            for folder in os.listdir("backups"):
                if os.path.isdir(f"backups/{folder}"):
                    shutil.rmtree(f"backups/{folder}")

        event_string += f"[{get_current_time()}] [BACKUPS] All backups have been deleted.\n"
        
        backups = vars._Get_Backups_Dict()
        for backup in backups.keys(): #For each backup - set it to false in the dict, remove all options from the listbox, and make the frame invisible
            window[f"{Keys._BackupsTabListboxPrefix}:{backup}"].update(values=[])
            window[f"{Keys._BackupsTabFramePrefix}:{backup}"].update(visible=False)
            window[f"{Keys._BackupsTabFramePrefix}:{backup}"].hide_row()
            backups[backup] = False 
        event_string += f"[{get_current_time()}] [UI] Backups tab updated to reflect deleted backups.\n\n"
    else:
        event_string += f"[{get_current_time()}] [BACKUPS] User rejected deletion of all backups.\n\n"
    
    return event_string

def _Delete_All_Specific_World_Backups(window: sg.Window, world: str):
    event_string = f"[{get_current_time()}] [BACKUPS] Generating popup for deletion of all backups for {world}.\n"
    response = sg.popup_yes_no("Are you sure you want to PERMANENTLY delete all backups?", "WARNING: This action cannot be undone.", title="Delete all backups?")

    if response == "Yes":
        try:
            shutil.rmtree(f"backups/{world}_backups")
        except PermissionError as e:
            event_string += f"[{get_current_time()}] [BACKUPS] Permission error encountered while trying to delete backups/{world}_backups. Requesting elevated permissions, then trying again.\n"
            elevate.elevate()
            shutil.rmtree(f"backups/{world}_backups")

        event_string += f"[{get_current_time()}] [BACKUPS] All backups for {world} have been deleted.\n"

        window[f"{Keys._BackupsTabListboxPrefix}:{world}"].update(values=[])
        window[f"{Keys._BackupsTabFramePrefix}:{world}"].update(visible=False)
        window[f"{Keys._BackupsTabFramePrefix}:{world}"].hide_row()

        backups = vars._Get_Backups_Dict()
        backups[world] = False

        event_string += f"[{get_current_time()}] [UI] Backups tab updated to reflect deleted backups.\n\n"
    else:
        event_string += f"[{get_current_time()}] [BACKUPS] User rejected deletion of all backups for {world}.\n\n"

    return event_string