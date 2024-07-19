_SaveFolderRE = r"^.*_[0-9]+$"
_XML_DECLARATION = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
_Links = {
    "github": "https://github.com/jcho3435/stardew-save-editor",
    "docs": ""
}

class Keys:
    _FolderInput = "-FOLDER-"
    _FolderBrowser = "-FOLDERBROWSERBUTTON-"
    _ValidateFolder = "-VALIDATEFOLDER-"
    _SaveWarning = "-SAVEWARNING-"
    _FarmerFrames = ["-FARMERFRAME0-", "-FARMERFRAME1-", "-FARMERFRAME2-", "-FARMERFRAME3-", "-FARMERFRAME4-", "-FARMERFRAME5-", "-FARMERFRAME6-", "-FARMERFRAME7-"]

    #Editable values
    _FarmerNames = ["-FARMERNAME0-", "-FARMERNAME1-", "-FARMERNAME2-", "-FARMERNAME3-", "-FARMERNAME4-", "-FARMERNAME5-", "-FARMERNAME6-", "-FARMERNAME7-"]

    #Tabs
    _FarmersTab = "Farmers"
    _SaveTab = "Save"
    _AboutTab = "About"
    _EditorTabs = [_FarmersTab, _SaveTab] #used for setting visibility after load event
    

class CharacterSavePaths:
    _FarmerName = "/Farmer/name[1]"


class WorldSavePaths:
    _FarmerName = "/SaveGame/player/name[1]"
    _FarmhandsNames = "/SaveGame/farmhands/Farmer/name"