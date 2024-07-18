from components.constants import Keys, CharacterSavePaths, WorldSavePaths
import PySimpleGUI as sg
from functions.get_and_load_xml import get_xml_roots
from functions.functions import get_current_time

def save_farmer_data_to_tree(window: sg.Window) -> str:
    event_string = ""
    character_data, world_data = get_xml_roots()
    farmerName = window[Keys._FarmerName].get()

    #Change in character saves
    character_data.xpath(CharacterSavePaths._FarmerName)[0].text = farmerName

    event_string += f"[{get_current_time()}] Farmer changes saved to character xml tree.\n"

    #Change in world saves
    world_data.xpath(WorldSavePaths._FarmerName)[0].text = farmerName

    event_string += f"[{get_current_time()}] Farmer changes saved to world xml tree.\n\n"

    return event_string