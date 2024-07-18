from lxml import etree
from functions.functions import get_current_time

_character_data = None
_world_data = None
_xml_loaded = False

def load_xml_roots(folderpath) -> str:
    global _xml_loaded
    if _xml_loaded:
        return f"[{get_current_time()}] Unnecessary call to load_xml_roots(). XML already loaded.\n\n"
    
    event_string = ""
    character_save_file = "save_data/SaveGameInfo" # TODO: MODIFY THIS TO BE THE CORRECT FOLDER LATER
    world_save_file = "save_data/ChingChong_363368866"

    with open(character_save_file, "rb") as f: 
        data = f.read()

    # REMOVE BOM CHARACTERS
    if data.startswith(b'\xef\xbb\xbf'):
        data = data[3:]

    global _character_data
    _character_data = etree.fromstring(data)

    event_string += f"[{get_current_time()}] Finished reading character data into tree format.\n"

    with open(world_save_file, "rb") as f: 
        data = f.read()

    # REMOVE BOM CHARACTERS
    if data.startswith(b'\xef\xbb\xbf'):
        data = data[3:]

    global _world_data
    _world_data = etree.fromstring(data)

    event_string += f"[{get_current_time()}] Finished reading world data into tree format.\n\n"

    _xml_loaded = True

    return event_string

def get_xml_roots() -> tuple[etree._Element, etree._Element]:
    return _character_data, _world_data