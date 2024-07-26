import os, datetime, shutil, sys

def init_directories():
    if not os.path.isdir("backups"):
        os.mkdir("backups")
    if not os.path.isdir("logs"):
        os.mkdir("logs")

def get_current_time(include_microseconds = False):
    return datetime.datetime.now().time() if include_microseconds else datetime.datetime.now().time().replace(microsecond=0)

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

def getBasePath():
    try:
        return sys._MEIPASS.replace("\\", "/")
    except Exception:
        return os.path.abspath(".")