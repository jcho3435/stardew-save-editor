import os

_MAXPLAYERS = 8

_SaveFolderRE = r"^.*_[0-9]+$"
_XML_DECLARATION = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
_Links = {
    "github": "https://github.com/jcho3435/stardew-save-editor",
    "docs": "file:///" + os.path.abspath("docs/home.html").replace("\\", "/").replace(" ", "%20")
}

class Keys:
    _FolderInput = "-FOLDER-"
    _FolderBrowser = "-FOLDERBROWSERBUTTON-"
    _ValidateFolder = "-VALIDATEFOLDER-"
    _SaveWarning = "-SAVEWARNING-"
    _FarmerFrames = [f"-FARMERFRAME{i}-" for i in range(_MAXPLAYERS)]

    #Editable values
    _FarmerNames = [f"-FARMERNAME{i}-" for i in range(_MAXPLAYERS)]
    _FarmerSkillLevels = {
        "farming": [f"-FARMERFARMINGLVL{i}-" for i in range(_MAXPLAYERS)],
        "mining": [f"-FARMERMININGLVL{i}-" for i in range(_MAXPLAYERS)],
        "foraging": [f"-FARMERFORAGINGLVL{i}-" for i in range(_MAXPLAYERS)],
        "fishing": [f"-FARMERFISHINGLVL{i}-" for i in range(_MAXPLAYERS)],
        "combat": [f"-FARMERCOMBATLVL{i}-" for i in range(_MAXPLAYERS)]
    }

    #Tabs
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