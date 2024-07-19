from components.constants import Keys, CharacterSavePaths, WorldSavePaths
from lxml import etree
from functions.get_and_load_xml import get_xml_roots
from functions.functions import get_current_time

def save_name_to_tree(farmer: etree._Element, name: str):
    farmer.xpath("./name[1]")[0].text = name.strip()

# def save_skills_to_tree(farmer, skill):
#     pass

def save_farmer_data_to_tree(values: dict) -> str:
    event_string = ""
    character_data, world_data = get_xml_roots()

    # Save host data
    farmerName = values[Keys._FarmerNames[0]]

    #Change in character saves
    save_name_to_tree(character_data, farmerName)

    event_string += f"[{get_current_time()}] Host farmer changes saved to character xml tree.\n"

    #Change in world saves
    worldsave_farmer = world_data.xpath(WorldSavePaths._Farmer)[0] #This is the <player> tag for the host player
    save_name_to_tree(worldsave_farmer, farmerName)

    event_string += f"[{get_current_time()}] Host farmer changes saved to world xml tree.\n"
    

    # Save farmhand data
    farmhands = world_data.xpath(WorldSavePaths._Farmhands) # gets list of farmhand <Farmer> tags
    index = 1
    for player in farmhands:
        save_name_to_tree(player, values[Keys._FarmerNames[index]])
        index += 1

    event_string += f"[{get_current_time()}] Farmhand changes saved to world xml tree.\n\n"

    return event_string