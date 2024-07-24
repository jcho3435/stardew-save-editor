'''
Holds definitions for functions for modifying the UI, loading data, and filling the UI with loaded data.
'''

import PySimpleGUI as sg
from components.constants import Keys, WorldSavePaths
import components.constants as constants, components.vars as vars
from functions.functions import get_current_time
from functions.get_and_load_xml import load_xml_roots, get_xml_roots
from lxml import etree
from components.vars import _Init_Friendship_Vars, _Get_Friendship_data

def hide_rows(window: sg.Window, keys: list | str):
    if type(keys) == str:
        window[keys].hide_row()
    else:
        for key in keys:
            window[key].hide_row()

def unhide_rows(window: sg.Window, keys: list | str):
    if type(keys) == str:
        window[keys].unhide_row()
    else:
        for key in keys:
            window[key].unhide_row()

def set_visibility(window: sg.Window, keys: list | str, isVisible: bool):
    if type(keys) == str:
        window[keys].update(visible = isVisible)
    else:
        for key in keys:
            window[key].update(visible = isVisible)

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
def _load_profile_data(window: sg.Window) -> str:
    character_save, world_save = get_xml_roots()

    #Load host farmer
    enable_and_fill_farmer_frame(window, 0, character_save)

    #Load farmhands
    farmhands = world_save.xpath(WorldSavePaths._Farmhands) # returns a list of tags <Farmer>
    index = 1
    for farmer in farmhands:
        enable_and_fill_farmer_frame(window, index, farmer)
        index += 1

    window[Keys._FarmersTabColumn].contents_changed()
    return f"[{get_current_time()}] Farmers profile data loaded.\n\n"

#load friendship data into global list
def _load_friendship_data():
    character_save, world_save = get_xml_roots()

    #load host farmer friendship data
    load_friendship_data_dict(character_save, 0)

    #load farmhand friendship data
    farmhands = world_save.xpath(WorldSavePaths._Farmhands) # returns a list of tags <Farmer>
    index = 1
    for farmer in farmhands:
        load_friendship_data_dict(farmer, index)
        index += 1

    return f"[{get_current_time()}] Friendship data loaded into _FriendshipData variable.\n\n"

def load_save_data(window: sg.Window, folderpath: str) -> str:
    event_string = ""
    _reset_profile_tab_ui(window)
    _reset_friendship_tab_ui(window)
    _Init_Friendship_Vars()


    # load xml
    event_string += load_xml_roots(folderpath)
    
    event_string += _load_profile_data(window)
    event_string += _load_friendship_data()

    return event_string