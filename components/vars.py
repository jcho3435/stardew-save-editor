import os
from functions.functions import getBasePath
from components.constants import Keys

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

_FriendshipData: list[dict[str: str]]
def _Get_Friendship_data():
    return _FriendshipData

_FriendshipTabOldComboInd: int
def _Set_Friendship_Tab_Old_Combo_Ind(i: int):
    global _FriendshipTabOldComboInd
    _FriendshipTabOldComboInd = i

def _Get_Friendship_Tab_Old_Combo_Ind():
    return _FriendshipTabOldComboInd

_CurrTab: str
def _Set_Curr_Tab(tab: str):
    global _CurrTab
    _CurrTab = tab

def _Get_Curr_Tab():
    return _CurrTab

def _Init_Friendship_Vars():
    global _FriendshipData
    _FriendshipData = [{}, {}, {}, {}, {}, {}, {}, {}]
    global _FriendshipTabOldComboInd
    _FriendshipTabOldComboInd = -1
    global _CurrTab
    _CurrTab = Keys._LoadTab

_Backups: dict[str: bool]
def _Set_Backups_Dict(backups: dict[str: bool]):
    '''
    Backups is a dictionary where the keys contain all of the backups which have dedicated frames on the backups tab, and the values are bools which indicate whether or not a given frame is active.
    This is needed because elements cannot be completely removed from a layout. They can only be hidden.
    '''
    global _Backups
    _Backups = backups

def _Get_Backups_Dict() -> dict[str: bool]:
    return _Backups