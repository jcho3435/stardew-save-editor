from components.constants import Keys, WorldSavePaths, Seasons
from lxml import etree
from functions.get_and_load_xml import get_xml_roots
from functions.functions import get_current_time
import components.constants as constants, components.vars as vars

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

# - - - - - - - - - - - - - - - - - Save Farmers Tab Data  - - - - - - - - - - - - - - - - - #
def save_name_to_tree(farmer: etree._Element, name: str):
    farmer.xpath("./name[1]")[0].text = name.strip()

def save_skill_levels_and_xp_to_tree(farmer: etree._Element, values: dict, index):
    for skill, keys in Keys._FarmerSkillLevels.items():
        farmer.xpath(f"./{skill}Level[1]")[0].text = values[keys[index]].strip()

    for skill, keys in Keys._FarmerSkillExperience.items():
        farmer.xpath(f"./experiencePoints/int[{vars._SkillNameToXMLExperienceIndexMap[skill]}]")[0].text = values[keys[index]].strip()

def save_farmers_tab_data_to_tree(values: dict) -> str:
    event_string = ""
    character_data, world_data = get_xml_roots()

    # Save host data
    farmerName = values[Keys._FarmerNames[0]]

    #Change in character saves
    save_name_to_tree(character_data, farmerName)
    save_skill_levels_and_xp_to_tree(character_data, values, 0)

    event_string += f"[{get_current_time()}] [SAVE] Farmer tab host farmer changes saved to character xml tree.\n"

    #Change in world saves
    worldsave_farmer = world_data.xpath(WorldSavePaths._Farmer)[0] #This is the <player> tag for the host player
    save_name_to_tree(worldsave_farmer, farmerName)
    save_skill_levels_and_xp_to_tree(worldsave_farmer, values, 0)

    event_string += f"[{get_current_time()}] [SAVE] Farmer tab host farmer changes saved to world xml tree.\n"
    

    # Save farmhand data
    farmhands = world_data.xpath(WorldSavePaths._Farmhands) # gets list of farmhand <Farmer> tags
    index = 1
    for farmer in farmhands:
        save_name_to_tree(farmer, values[Keys._FarmerNames[index]])
        save_skill_levels_and_xp_to_tree(farmer, values, index)
        index += 1

    if index != 1:
        event_string += f"[{get_current_time()}] [SAVE] Farmer tab farmhand changes saved to world xml tree.\n\n"

    return event_string

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - Save Friendship Tab Data  - - - - - - - - - - - - - - - - - #

def save_friendship_points_to_tree(farmer: etree._Element, index: int):
    friendshipData = vars._Get_Friendship_data()
    data = friendshipData[index]

    npc_items: list[etree._Element] = farmer.xpath("./friendshipData[1]/item")
    for item in npc_items:
        npc = item.xpath("./key/string[1]")[0].text
        item.xpath("./value/Friendship/Points[1]")[0].text = data[npc] #reassignment

def save_friendship_tab_data_to_tree() -> str:
    event_string = ""
    character_data, world_data = get_xml_roots()

    # Save host data
    # Change in character save file
    save_friendship_points_to_tree(character_data, 0)
    event_string += f"[{get_current_time()}] [SAVE] Friendship tab host farmer changes saved to character xml tree.\n"

    # Change in world save file
    world_save_host = world_data.xpath(WorldSavePaths._Farmer)[0]
    save_friendship_points_to_tree(world_save_host, 0)
    event_string += f"[{get_current_time()}] [SAVE] Friendship tab host farmer changes saved to world xml tree.\n"

    #Save farmhand data
    farmhands = world_data.xpath(WorldSavePaths._Farmhands)
    index = 1
    for farmer in farmhands:
        save_friendship_points_to_tree(farmer, index)
        index += 1

    if index != 1:
        event_string += f"[{get_current_time()}] [SAVE] Farmer tab farmhand changes saved to world xml tree.\n\n"

    return event_string

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - Save World Tab Data  - - - - - - - - - - - - - - - - - -  #
def save_world_date_to_tree(values: dict):
    # Date data must be saved in:
    # - world save <year>, <dayOfMonth>, <currentSeason> (actual in game day/year/season)
    # - character save <___ForSaveGame> tags
    # - world save <___ForSaveGame> tags for both host and all farmhands

    def save_date_to_ForSaveGame_tags(farmer: etree._Element, day, season, year):
        farmer.xpath(WorldSavePaths._FarmerRelativeDayOfMonthForSaveGame)[0].text = day # This works for character save farmer as well
        farmer.xpath(WorldSavePaths._FarmerRelativeSeasonForSaveGame)[0].text = season
        farmer.xpath(WorldSavePaths._FarmerRelativeYearForSaveGame)[0].text = year
    
    day = values[Keys._WorldDayOfMonth]
    season = values[Keys._WorldSeason].lower()
    year = values[Keys._WorldYear]
    seasonInd = Seasons[season].value

    character_data, world_data = get_xml_roots()

    # Save _ForSaveGame tags for character save
    save_date_to_ForSaveGame_tags(character_data, day, seasonInd, year)

    # Save _ForSaveGame tags for host in world save
    host = world_data.xpath(WorldSavePaths._Farmer)[0]
    save_date_to_ForSaveGame_tags(host, day, seasonInd, year)

    # Save _ForSaveGame tags for farmhands in world save
    farmhands = world_data.xpath(WorldSavePaths._Farmhands)
    for farmer in farmhands:
        save_date_to_ForSaveGame_tags(farmer, day, seasonInd, year)

    # Save to <year>, <dayOfMonth>, <currentSeason>
    world_data.xpath(WorldSavePaths._CurrentDayOfMonth)[0].text = day
    world_data.xpath(WorldSavePaths._CurrentSeason)[0].text = season
    world_data.xpath(WorldSavePaths._CurrentYear)[0].text = year

def save_world_tab_data_to_tree(values: dict) -> str:
    event_string = ""

    save_world_date_to_tree(values)
    event_string += f"[{get_current_time()}] [SAVE] World tab date changes saved to xml trees.\n\n"

    return event_string