from enum import Enum

_MAXPLAYERS = 8

_CURRENTVERSION = "v0.2-prerelease" #TODO: Change this on every version

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
    _BackupsTabFramePrefix = "BackupFrame"
    _BackupsTabListboxPrefix = "BackupsListbox"
    _DeleteAllBackupsPrefix = "DELETE_ALL_BACKUP"
    _WorldTabWeatherImage = "-WorldTabWeatherImage-"

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
    _WorldDayOfMonth = "-WorldDayOfMonth-"
    _WorldSeason = "-WorldSeason-"
    _WorldYear = "-WorldYear-"
    _WorldWeather = "-WorldWeather-"
    _DailyLuck = "-DailyLuck-"

    #Tabs ----------------------------------------------------------------------
    _LoadTab = "Load"
    _FarmersTab = "Farmers"
    _FriendshipTab = "Friendship"
    _WorldTab = "World"
    _SaveTab = "Save"
    _SpacerTab = "                 "
    _BackupsTab = "Backup Manager"
    _AboutTab = "About"
    _EditorTabs = [_FarmersTab, _SaveTab, _FriendshipTab, _WorldTab] #used for setting visibility after load event
    _AllTabs = _EditorTabs + [_LoadTab, _AboutTab]
    _TabGroup = "-TabGroup-"
    
    #Columns -------------------------------------------------------------------
    _FarmersTabColumn = "-FarmersTabColumn-"
    _FriendshipTabColumn = "-FriendshipTabColumn-"
    _WorldTabColumn = "-WorldTabColumn-"
    _BackupsTabColumn = "-BackupsTabColumn-"
    _BackupsTabFramesColumn = "-BackupsTabFramesColumn-"
    _AboutTabColumn = "-AboutTabColumn-"

class CharacterSavePaths:
    _FarmerSkillLevels = {
        "farming": "/Farmer/farmingLevel[1]", 
        "mining": "/Farmer/miningLevel[1]", 
        "foraging": "/Farmer/foragingLevel[1]", 
        "fishing": "/Farmer/fishingLevel[1]", 
        "combat": "/Farmer/combatLevel[1]"
        }
    _FriendshipData = "/Farmer/friendshipData[1]"

    _SeasonForSaveGame = "/Farmer/seasonForSaveGame[1]"
    _DayOfMonthForSaveGame = "/Farmer/dayOfMonthForSaveGame[1]"
    _YearForSaveGame = "/Farmer/yearForSaveGame[1]"

class WorldSavePaths:
    _Farmer = "/SaveGame/player"
    _Farmhands = "/SaveGame/farmhands/Farmer"

    _FarmerFriendshipData = "/SaveGame/player/friendshipData[1]"
    _FarmhandRelativeFriendshipData = "./friendshipData[1]" # Relative to Farmer tag

    _CurrentSeason = "/SaveGame/currentSeason[1]"
    _CurrentDayOfMonth = "/SaveGame/dayOfMonth[1]"
    _CurrentYear = "/SaveGame/year[1]"
    _FarmerRelativeSeasonForSaveGame = "./seasonForSaveGame"
    _FarmerRelativeDayOfMonthForSaveGame = "./dayOfMonthForSaveGame"
    _FarmerRelativeYearForSaveGame = "./yearForSaveGame"

    _DailyLuck = "/SaveGame/dailyLuck[1]"

class Seasons(Enum):
    spring = "0"
    summer = "1"
    fall = "2"
    winter = "3"

_WeatherTags = ["isRaining", "isDebrisWeather", "isLightning", "isSnowing"]
class WeatherPatterns(Enum):
    Sunny = {"isRaining": False, "isDebrisWeather": False, "isLightning": False, "isSnowing": False}
    Windy = {"isRaining": False, "isDebrisWeather": True, "isLightning": False, "isSnowing": False}
    Rainy = {"isRaining": True, "isDebrisWeather": False, "isLightning": False, "isSnowing": False}
    Stormy = {"isRaining": True, "isDebrisWeather": False, "isLightning": True, "isSnowing": False} # Does not work
    Snowy = {"isRaining": False, "isDebrisWeather": False, "isLightning": False, "isSnowing": True}