import os
from functions.functions import getBasePath

_MAXPLAYERS = 8

_AllFriendableNPCs = [
    "Harvey", "Leah", "Linus", "Penny", "Pierre", "Abigail", "Alex", "Clint", "Demetrius", "Emily", "Evelyn", "Gus", "Kent", "Lewis", "Marnie", "Maru", "Pam", "Robin", "Sandy", "Caroline",
    "Dwarf", "Elliott", "Haley", "Jas", "Krobus", "Leo", "Sam", "Sebastian", "Shane", "Vincent", "Willy", "Wizard", "George", "Jodi"
]

class Keys:
    '''
    Contains keys for window elements
    '''
    _FolderInput = "-FolderSelection-"
    _FolderBrowser = "-FolderBrowserButton-"
    _ValidateFolder = "-ValidateFolder-"
    _SaveWarning = "-SaveWarning-"
    _FarmersTabFrames = [f"-FarmersTabFrame{i}-" for i in range(_MAXPLAYERS)]
    _FriendshipTabFrames = [f"-FriendshipTabFrame{i}-" for i in range(_MAXPLAYERS)]
    _FriendshipTabFarmerCombo = "-FriendshipTabFarmerCombo-"

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

    _NPCFriendshipPoints = {npc: f"-{npc}Friendship-" for npc in _AllFriendableNPCs}

    #Tabs ----------------------------------------------------------------------
    _LoadTab = "Load"
    _FarmersTab = "Farmers"
    _FriendshipTab = "Friendship"
    _SaveTab = "Save"
    _AboutTab = "About"
    _EditorTabs = [_FarmersTab, _SaveTab, _FriendshipTab] #used for setting visibility after load event
    _AllTabs = _EditorTabs + [_LoadTab, _AboutTab]
    _TabGroup = "-TabGroup-"
    
    #Columns -------------------------------------------------------------------
    _FarmersTabColumn = "-FarmersTabColumn-"
    _FriendshipTabColumn = "-FriendshipTabColumn-"
    _AboutTabColumn = "-AboutTabColumn-"

class CharacterSavePaths:
    _FarmerSkillLevels = {
        "farming": "/Farmer/farmingLevel[1]", 
        "mining": "/Farmer/miningLevel[1]", 
        "foraging": "/Farmer/foragingLevel[1]", 
        "fishing": "/Farmer/fishingLevel[1]", 
        "combat": "/Farmer/combatLevel[1]"
        }
    _FriendshipData = "Farmer/friendshipData[1]"

class WorldSavePaths:
    _Farmer = "/SaveGame/player"
    _Farmhands = "/SaveGame/farmhands/Farmer"

    _FarmerFriendshipData = "/SaveGame/player/friendshipData[1]"
    _FarmhandRelativeFriendshipData = "./friendshipData[1]"