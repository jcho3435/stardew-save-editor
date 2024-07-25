from functions.functions import get_current_time
import PySimpleGUI as sg
import os, shutil
import elevate

#TODO: define function to update the backups page

def _Delete_All_Backups_Event() -> str:
    event_string = f"[{get_current_time()}] Generated all backups deletion popup.\n"
    response = sg.popup_yes_no("Are you sure you want to PERMANENTLY delete all backups?", "WARNING: This action cannot be undone.", "This app may need to ask for elevated permissions in order to delete your backup files.", title="Delete all backups?")
    if response == "Yes":
        event_string += f"[{get_current_time()}] User confirmed deletion of backups.\n"
        try:
            for folder in os.listdir("backups"):
                shutil.rmtree(f"backups/{folder}")
        except PermissionError as e:
            event_string += f"[{get_current_time()}] Permission error encountered while trying to delete backups. Requesting elevated permissions, then trying again.\n"
            elevate.elevate()
            for folder in os.listdir("backups"):
                if os.path.isdir(f"backups/{folder}"):
                    shutil.rmtree(f"backups/{folder}")

        event_string += f"[{get_current_time()}] All backups have been deleted.\n\n"
        #TODO: Update the backups tab to reflect no backups
    else:
        event_string += f"[{get_current_time()}] User rejected deletion of backups.\n\n"
    
    return event_string