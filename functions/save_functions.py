from components.constants import Keys, WorldSavePaths
from lxml import etree
from functions.get_and_load_xml import get_xml_roots
from functions.functions import get_current_time
import components.constants as constants

def save_name_to_tree(farmer: etree._Element, name: str):
    farmer.xpath("./name[1]")[0].text = name.strip()

def save_skill_levels_and_xp_to_tree(farmer: etree._Element, values: dict, index):
    for skill, keys in Keys._FarmerSkillLevels.items():
        farmer.xpath(f"./{skill}Level[1]")[0].text = values[keys[index]].strip()

    for skill, keys in Keys._FarmerSkillExperience.items():
        farmer.xpath(f"./experiencePoints/int[{constants._SkillNameToXMLExperienceIndexMap[skill]}]")[0].text = values[keys[index]].strip()

def save_farmers_tab_data_to_tree(values: dict) -> str:
    event_string = ""
    character_data, world_data = get_xml_roots()

    # Save host data
    farmerName = values[Keys._FarmerNames[0]]

    #Change in character saves
    save_name_to_tree(character_data, farmerName)
    save_skill_levels_and_xp_to_tree(character_data, values, 0)

    event_string += f"[{get_current_time()}] Farmer tab host farmer changes saved to character xml tree.\n"

    #Change in world saves
    worldsave_farmer = world_data.xpath(WorldSavePaths._Farmer)[0] #This is the <player> tag for the host player
    save_name_to_tree(worldsave_farmer, farmerName)
    save_skill_levels_and_xp_to_tree(worldsave_farmer, values, 0)

    event_string += f"[{get_current_time()}] Farmer tab host farmer changes saved to world xml tree.\n"
    

    # Save farmhand data
    farmhands = world_data.xpath(WorldSavePaths._Farmhands) # gets list of farmhand <Farmer> tags
    index = 1
    for farmer in farmhands:
        save_name_to_tree(farmer, values[Keys._FarmerNames[index]])
        save_skill_levels_and_xp_to_tree(farmer, values, index)
        index += 1

    if index != 1:
        event_string += f"[{get_current_time()}] Farmer tab farmhand changes saved to world xml tree.\n\n"

    return event_string