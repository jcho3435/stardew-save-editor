import os, datetime, shutil
import PySimpleGUI as sg
from components.views import View

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

def hide_rows(window: sg.Window, keys: list):
    for key in keys:
        window[key].hide_row()

def unhide_rows(window: sg.Window, keys: list):
    for key in keys:
        window[key].unhide_row()

def set_visibility(window: sg.Window, keys: list, isVisible):
    for key in keys:
        window[key].update(visible = isVisible)

def switch_view(window: sg.Window, view: View):
    if view == View.LOAD:
        window["-EDITOR-"].hide_row()
        window["-LOAD-"].unhide_row()
    elif view == View.EDITOR:
        window["-LOAD-"].hide_row()
        window["-EDITOR-"].unhide_row()