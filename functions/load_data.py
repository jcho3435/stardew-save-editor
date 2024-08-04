'''
Holds definitions for functions for loading data and filling the UI with loaded data.
'''

import PySimpleGUI as sg
from components.constants import Keys, WorldSavePaths, WeatherPatterns
import components.constants as constants, components.vars as vars
from functions.functions import get_current_time, strToBool
from functions.get_and_load_xml import load_xml_roots, get_xml_roots
from lxml import etree
from components.vars import _Init_Friendship_Vars, _Get_Friendship_data
from functions.ui_functions import set_visibility, col_contents_changed
import functions.event_handling as event_handling

def enable_and_fill_farmer_frame(window: sg.Window, index: int, farmer: etree._Element):
    farmerName = farmer.xpath("./name[1]")[0].text
    window[Keys._FarmerNames[index]].update(farmerName, disabled=False)

    for skill, keys in Keys._FarmerSkillLevels.items():
        skillLevel = farmer.xpath(f"./{skill}Level")[0].text
        window[keys[index]].update(skillLevel, disabled=False)
    
    for skill, keys in Keys._FarmerSkillExperience.items():
        skillXp = farmer.xpath(f"./experiencePoints/int[{vars._SkillNameToXMLExperienceIndexMap[skill]}]")[0].text
        window[keys[index]].update(skillXp, disabled=False)

    window[Keys._FarmersTabFrames[index]].update(visible=True)

def load_friendship_data_dict(farmer: etree._Element, index: int):
    friendshipData = farmer.xpath("./friendshipData[1]")[0]
    items: list[etree._Element] = friendshipData.xpath("./item")

    data = {}
    for item in items:
        npc = item.xpath("./key/string[1]")[0].text
        friendship = item.xpath("./value/Friendship/Points[1]")[0].text
        data[npc] = friendship
    
    friendshipDataList = _Get_Friendship_data()
    friendshipDataList[index] = data

def _reset_profile_tab_ui(window: sg.Window):
    for key in Keys._FarmerNames:
        window[key].update(value="", disabled=True)

    for keys in Keys._FarmerSkillLevels.values():
        for key in keys:
            window[key].update(value="", disabled=True)
    
    for keys in Keys._FarmerSkillExperience.values():
        for key in keys:
            window[key].update(value="", disabled=True)

    set_visibility(window, Keys._FarmersTabFrames, False)

def _reset_friendship_tab_ui(window: sg.Window):
    window[Keys._FriendshipTabFarmerCombo].update(values=[], set_to_index=0) #Only this call is necessary, but the others are there for redundancy
    for npc, key in Keys._NPCFriendshipPoints.items():
        window[key].update(value="", disabled=True)

#loading save data
def _load_and_fill_profile_tab_data(window: sg.Window) -> str:
    character_save, world_save = get_xml_roots()

    #Load host farmer
    enable_and_fill_farmer_frame(window, 0, character_save)

    #Load farmhands
    farmhands = world_save.xpath(WorldSavePaths._Farmhands) # returns a list of tags <Farmer>
    index = 1
    for farmer in farmhands:
        enable_and_fill_farmer_frame(window, index, farmer)
        index += 1

    col_contents_changed(window, Keys._FarmersTabColumn)
    return f"[{get_current_time()}] [LOAD] Farmers profile data loaded.\n"

#load friendship data into global list
def _load_friendship_tab_data() -> str:
    character_save, world_save = get_xml_roots()

    #load host farmer friendship data
    load_friendship_data_dict(character_save, 0)

    #load farmhand friendship data
    farmhands = world_save.xpath(WorldSavePaths._Farmhands) # returns a list of tags <Farmer>
    index = 1
    for farmer in farmhands:
        load_friendship_data_dict(farmer, index)
        index += 1

    return f"[{get_current_time()}] [LOAD] Friendship data loaded into _FriendshipData variable.\n"

def _load_and_fill_world_tab_data(window: sg.Window) -> str:
    character_save, world_save = get_xml_roots() # Since the actual in game day, year, and season are stored in world save, we pull data from that file

    day, season, year = world_save.xpath(WorldSavePaths._CurrentDayOfMonth)[0].text, world_save.xpath(WorldSavePaths._CurrentSeason)[0].text, world_save.xpath(WorldSavePaths._CurrentYear)[0].text
    window[Keys._WorldDayOfMonth].update(value=day)
    window[Keys._WorldSeason].update(value=season.capitalize())
    window[Keys._WorldYear].update(value=year)
    
    weather = {tag: strToBool(world_save.xpath(f"./{tag}[1]")[0].text) for tag in constants._WeatherTags} # Pulls out the 4 bools for weather tags
    choices: list[str] = window[Keys._WorldWeather].Values
    match_found = False
    for pattern in WeatherPatterns:
        if weather == pattern.value:
            ind = choices.index(pattern.name)
            window[Keys._WorldWeather].update(set_to_index=ind)
            event_handling.update_weather_icon(window, {Keys._WorldWeather: pattern.name}) # Kinda unclean solution but this works
            match_found = True
            break
    
    if not match_found:
        window[Keys._WorldWeather].update(set_to_index=0)
    

    return f"[{get_current_time()}] [LOAD] World tab data loaded.\n\n"

def load_save_data(window: sg.Window, folderpath: str) -> str:
    event_string = ""
    _reset_profile_tab_ui(window)
    _reset_friendship_tab_ui(window)
    _Init_Friendship_Vars()


    # load xml
    event_string += load_xml_roots(folderpath)
    
    event_string += _load_and_fill_profile_tab_data(window)
    event_string += _load_friendship_tab_data() # This function only needs to update/load the dictionaries. The actual loading of content onto the tab occurs on change to friendship tab event and combobox update event. This is only done this way because we use a combo box on that tab to swap between farmer profiles, AND the combo box is updated with the most recent values for farmers' names every time we swap to friendship tab.
    event_string += _load_and_fill_world_tab_data(window)

    return event_string