from lxml import etree
from functions.functions import get_current_time
import os

_character_data = None
_world_data = None

def load_xml_roots(folderpath) -> str:
    event_string = ""

    basename = os.path.basename(folderpath)
    character_save_file = os.path.join(folderpath, "SaveGameInfo")
    world_save_file = os.path.join(folderpath, basename)

    character_save_file = "save_data2/SaveGameInfo" # TODO: MODIFY THIS TO BE THE CORRECT FOLDER LATER
    world_save_file = "save_data2/MoreRice_363478863"

    with open(character_save_file, "rb") as f: 
        data = f.read()

    # REMOVE BOM CHARACTERS
    if data.startswith(b'\xef\xbb\xbf'):
        data = data[3:]

    global _character_data
    _character_data = etree.fromstring(data)

    event_string += f"[{get_current_time()}] [LOAD] Finished reading character data from save file into tree format.\n"

    with open(world_save_file, "rb") as f: 
        data = f.read()

    # REMOVE BOM CHARACTERS
    if data.startswith(b'\xef\xbb\xbf'):
        data = data[3:]

    global _world_data
    _world_data = etree.fromstring(data)

    event_string += f"[{get_current_time()}] [LOAD] Finished reading world data from save file into tree format.\n\n"

    _xml_loaded = True

    return event_string

def get_xml_roots() -> tuple[etree._Element, etree._Element]:
    return _character_data, _world_data