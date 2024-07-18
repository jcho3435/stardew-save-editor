import os, datetime, shutil
import PySimpleGUI as sg
from lxml import etree

def init_directories():
    if not os.path.isdir("backups"):
        os.mkdir("backups")
    if not os.path.isdir("logs"):
        os.mkdir("logs")

def get_current_time(include_microseconds = False):
    return datetime.datetime.now().time() if include_microseconds else datetime.datetime.now().time().replace(microsecond=0)

def create_backup(folderpath) -> str:
    name = os.path.basename(folderpath)
    time = datetime.datetime.now()

    event_string = ""

    backup_dir = f"backups\\{name}_backups\\{name}_{int(time.timestamp())}"
    os.makedirs(backup_dir, exist_ok=True)
       
    for filename in os.listdir(folderpath):
        src_path = os.path.join(folderpath, filename)
        dst_path = os.path.join(backup_dir, filename)

        shutil.copy(src_path, dst_path)

        event_string += f"[{get_current_time()}] Copied {filename} from {folderpath} to {backup_dir}\n"

    event_string += "\n"
    return event_string

def has_save_files(folderpath) -> bool:
    basename = os.path.basename(folderpath)
    expected_files = [basename, f"{basename}_old", "SaveGameInfo", "SaveGameInfo_old"]

    for file in os.listdir(folderpath):
        fullpath = os.path.join(folderpath, file)
        if not os.path.isfile(fullpath) or file not in expected_files:
            return False, f"[{get_current_time}] Invalid save folder {folderpath}. {file} should not be in save folder.\n\n", f"Invalid save folder {folderpath}. {file} should not be in save folder."
        expected_files.remove(file)
    
    if basename in expected_files or "SaveGameInfo" in expected_files:
        return False, f"[{get_current_time}] One or more save files are missing. Looking for files '{basename}' and 'SaveGameInfo'.\n\n", f"One or more save files are missing. Looking for files '{basename}' and 'SaveGameInfo'."
    
    return True, None, None