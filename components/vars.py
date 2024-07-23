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
def _Init_Friendship_Data():
    global _FriendshipData
    _FriendshipData = [{}, {}, {}, {}, {}, {}, {}, {}]

def _Get_Friendship_data():
    return _FriendshipData

_FriendshipTabOldComboInd: int = -1
def _Set_Friendship_Tab_Old_Combo_Ind(i: int):
    global _FriendshipTabOldComboInd
    _FriendshipTabOldComboInd = i

def _Get_Friendship_Tab_Old_Combo_Ind():
    return _FriendshipTabOldComboInd

_CurrTab: str = Keys._LoadTab
def _Set_Curr_Tab(tab: str):
    global _CurrTab
    _CurrTab = tab

def _Get_Curr_Tab():
    return _CurrTab