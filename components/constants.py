import os
from functions.functions import getBasePath

_MAXPLAYERS = 8
_BASEPATH = getBasePath()

_SaveFolderRE = r"^.*_[0-9]+$"
_XML_DECLARATION = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
_Links = {
    "github": "https://github.com/jcho3435/stardew-save-editor",
    "docs": "file:///" + os.path.abspath(f"{_BASEPATH}/docs/home.html").replace("\\", "/").replace(" ", "%20")
}

# This is for finding using xpath, which is 1 indexed
_SkillNameToXMLExperienceIndexMap = {
    "farming": 1,
    "fishing": 2,
    "foraging": 3,
    "mining": 4,
    "combat": 5,
    "luck": 6 # luck is unused by stardew
}

class Keys:
    _FolderInput = "-FolderSelection-"
    _FolderBrowser = "-FolderBrowserButton-"
    _ValidateFolder = "-ValidateFolder-"
    _SaveWarning = "-SaveWarning-"
    _FarmersTabFrames = [f"-FarmersTabFrame{i}-" for i in range(_MAXPLAYERS)]

    # Editable values ----------------------------------------------------------
    _FarmerNames = [f"-FarmerName{i}-" for i in range(_MAXPLAYERS)]
    _FarmerSkillLevels = {
        "farming": [f"-FarmerFarmingLVL{i}-" for i in range(_MAXPLAYERS)],
        "mining": [f"-FarmerMiningLVL{i}-" for i in range(_MAXPLAYERS)],
        "foraging": [f"-FarmerForagingLVL{i}-" for i in range(_MAXPLAYERS)],
        "fishing": [f"-FarmerFishingLVL{i}-" for i in range(_MAXPLAYERS)],
        "combat": [f"-FarmerCombatLVL{i}-" for i in range(_MAXPLAYERS)]
    }
    _FarmerSkillExperience = {
        "farming": [f"-FarmerFarmingXP{i}-" for i in range(_MAXPLAYERS)],
        "mining": [f"-FarmerMiningXP{i}-" for i in range(_MAXPLAYERS)],
        "foraging": [f"-FarmerForagingXP{i}-" for i in range(_MAXPLAYERS)],
        "fishing": [f"-FarmerFishingXP{i}-" for i in range(_MAXPLAYERS)],
        "combat": [f"-FarmerCombatXP{i}-" for i in range(_MAXPLAYERS)]
    }

    #Tabs ----------------------------------------------------------------------
    _FarmersTab = "Farmers"
    _SaveTab = "Save"
    _AboutTab = "About"
    _EditorTabs = [_FarmersTab, _SaveTab] #used for setting visibility after load event
    

class CharacterSavePaths:
    _FarmerSkillLevels = {
        "farming": "/Farmer/farmingLevel[1]", 
        "mining": "/Farmer/miningLevel[1]", 
        "foraging": "/Farmer/foragingLevel[1]", 
        "fishing": "/Farmer/fishingLevel[1]", 
        "combat": "/Farmer/combatLevel[1]"
        }


class WorldSavePaths:
    _Farmer = "/SaveGame/player"
    _Farmhands = "/SaveGame/farmhands/Farmer"