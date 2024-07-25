import PySimpleGUI as sg
from components.constants import Keys, _AllFriendableNPCs
from components.vars import _Links, _BASEPATH, _Set_Backups_List
import textwrap

# helpers --------------------------------------------------------------------------------
def generateFarmersTabFrames(farmers_tab_layout: list):
    '''
    Generates the frames for each farmer in the farmers tab, then appends it to the farmer tab's layout
    '''
    farmerNames = Keys._FarmerNames
    farmerSkillLevels = Keys._FarmerSkillLevels
    farmerSkillExperience = Keys._FarmerSkillExperience
    for i in range(8):
        frame_layout = [
            [sg.Text("Farmer Name:", p=(5, (3, 8))), sg.Input(key=farmerNames[i], disabled=True, p=(0, (3, 8)))],
            [sg.Text("Farming", p=((5, 0), 3)), sg.Image(f"{_BASEPATH}/icons/farming-icon.png", zoom=2, p=((1, 5), 3)), sg.Text("Level:"), sg.Input(key=farmerSkillLevels["farming"][i], disabled=True, p=((0, 5), 3), size=4), sg.Text("Experience:"), sg.Input(key=farmerSkillExperience["farming"][i], disabled=True, p=((0, 5), 3), size=12)],
            [sg.Text("Mining", p=((5, 0), 3)), sg.Image(f"{_BASEPATH}/icons/mining-icon.png", zoom=2, p=((1, 5), 3)), sg.Text("Level:"), sg.Input(key=farmerSkillLevels["mining"][i], disabled=True, p=((0, 5), 3), size=4), sg.Text("Experience:"), sg.Input(key=farmerSkillExperience["mining"][i], disabled=True, p=((0, 5), 3), size=12)],
            [sg.Text("Foraging", p=((5, 0), 3)), sg.Image(f"{_BASEPATH}/icons/foraging-icon.png", p=((1, 5), 3)), sg.Text("Level:"), sg.Input(key=farmerSkillLevels["foraging"][i], disabled=True, p=((0, 5), 3), size=4), sg.Text("Experience:"), sg.Input(key=farmerSkillExperience["foraging"][i], disabled=True, p=((0, 5), 3), size=12)],
            [sg.Text("Fishing", p=((5, 0), 3)), sg.Image(f"{_BASEPATH}/icons/fishing-icon.png", p=((1, 5), 3)), sg.Text("Level:"), sg.Input(key=farmerSkillLevels["fishing"][i], disabled=True, p=((0, 5), 3), size=4), sg.Text("Experience:"), sg.Input(key=farmerSkillExperience["fishing"][i], disabled=True, p=((0, 5), 3), size=12)],
            [sg.Text("Combat", p=((5, 0), 3)), sg.Image(f"{_BASEPATH}/icons/combat-icon.png", p=((1, 5), 3)), sg.Text("Level:"), sg.Input(key=farmerSkillLevels["combat"][i], disabled=True, p=((0, 5), 3), size=4), sg.Text("Experience:"), sg.Input(key=farmerSkillExperience["combat"][i], disabled=True, p=((0, 5), 3), size=12)]
        ]
        title = f"Farmer {i+1} Profile"
        if i == 0:
            title += " (World host)"
        farmers_tab_layout.append([sg.Frame(title, frame_layout, key=Keys._FarmersTabFrames[i],  visible=False)])

def createBackupFrame(backup_name: str, choices: list[str]) -> sg.Frame:
    '''
    Creates frame elements for backups
    '''
    frame_layout = [
        [sg.Listbox(choices, size=(40, 12), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key=f"{Keys._BackupsTabListboxPrefix}:{backup_name}", no_scrollbar=True), sg.Button("Delete All", button_color="red", key=f"{Keys._DeleteAllBackupsPrefix}:{backup_name}")],
    ]

    return sg.Frame(backup_name, frame_layout, pad=(5, (3, 12)), expand_x=True, key=f"{Keys._BackupsTabFramePrefix}:{backup_name}")

def generateBackupTabFrames(backups_tab_layout: list):
    '''
    Initial generation of all backups. Each world gets its own frame. Stores the name of all backups in global variable _Backups
    '''
    import os
    backups = []

    for folder in os.listdir("backups"):
        backup_name = "_".join(folder.split("_")[0:-1])
        backups.append(backup_name)
        choices = os.listdir(f"backups/{folder}")
        backups_tab_layout.append([createBackupFrame(backup_name, choices)])
    
    _Set_Backups_List(backups)

def createAboutTabHeader(text):
    return sg.Text(text, font=("Times New Roman", 16, "underline"), text_color="black", pad=5)

def createAboutTabDescription(*args):
    text = ""
    for arg in args:
        text += textwrap.fill(arg, 170)
        text += "\n\n"
    #TODO: consider trimming the ending \n\n
    return sg.Text(text, font=("Arial", 12), text_color="black", expand_x=True)

def scrollableColumnWrapper(layout, key):
    """
    Wraps a layout with a scrollable column element
    """
    return [[sg.Column(layout, scrollable=True, vertical_scroll_only=True, expand_x=True, expand_y=True, key=key)]]

# Layouts ---------------------------------------------------------------------------------
load_tab_layout = [ # LOAD
        [sg.Push(), sg.Text("Stardew Valley Save Editor!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
        [sg.Text("Folder:", size=5), sg.Input(expand_x=True, key=Keys._FolderInput, enable_events=True, disabled=True), sg.FolderBrowse("Select Save Folder", key=Keys._FolderBrowser)],
        [sg.Text("Note: By default, save folders are located at C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black", justification="center", expand_x=True)],
        [sg.Text("", size=4), sg.Text("", key=Keys._ValidateFolder)],
        [sg.Text("", size=4), sg.Text("", key=Keys._SaveWarning, text_color="black")]
    ]

farmers_tab_layout = [ # FARMERS
    [sg.Text("Change Farmer Data", font=("Times New Roman", 16))],
]
generateFarmersTabFrames(farmers_tab_layout)

friendship_tab_layout = [ # FRIENDSHIP
    [sg.Text("Change Friendship Data", font=("Times New Roman", 16))],
    [sg.Text("Select farmer:", pad=(5, (3, 20))), sg.Combo([], size=32, enable_events=True, key=Keys._FriendshipTabFarmerCombo, readonly=True, pad=(5, (3, 20)))]
]
friendship_tab_npcs = [[sg.Image(f"{_BASEPATH}/icons/npcs/{npc}.png", subsample=2), sg.Text(f"{npc}:", p=(5, 8)), sg.Input(key=Keys._NPCFriendshipPoints[npc], disabled=True, p=((0, 5), 8), size=18, disabled_readonly_background_color="#cfcfcf")] for npc in sorted(_AllFriendableNPCs)]
friendship_tab_layout += friendship_tab_npcs

save_tab_layout = [ # SAVE
    [sg.Button("Save Changes")]
]

backups_tab_layout = [ # BACKUPS
    [sg.Button("Delete All Backups", button_color="red", p=(5, 3, 12)), sg.Button("Delete Selected", p=(5, 3, 12))],
    [sg.Text("Note: You can scroll to see more options in each listbox. There is no scrollbar due to a bug with PySimpleGUI.")]
]
generateBackupTabFrames(backups_tab_layout)

about_tab_layout = [ # ABOUT
    [sg.Text("About the editor:", text_color="black", font=("Times New Roman", 30), pad=(5, (3, 10)))],
    [sg.Text("This application is a minimalist stardew valley save editor for windows. The code is fully open source and can be found", p=((5, 0), 3), text_color="black", font=("Arial", 12)), sg.Text("here.", tooltip=_Links["github"], p=(1, 3), enable_events=True, key=f"URL {_Links["github"]}", text_color="dark gray", font=("Arial", 12, "underline"))],
    [sg.Text("For detailed docs and explanations on each tab's fields, click", p=((5, 0), 3), text_color="black", font=("Arial", 12)), sg.Text("here.", tooltip=_Links["docs"], p=(1, 3), enable_events=True, key=f"URL {_Links["docs"]}", text_color="dark gray", font=("Arial", 12, "underline"))],
    [sg.Text(textwrap.fill("Warning: There is no input validation on any of the modifiable fields, so in order to avoid crashing due to bad save data, avoid inputting bad values. For example, for fields which should take a number, do not input and alphabetical characters. You can find more details on constraints on values for each field on the docs.", 170), p=((5, 0), (3, 22)), text_color="black", font=("Arial", 12))],
    [createAboutTabHeader("Load Tab")],
    [createAboutTabDescription(
        "Load your save file here. Always make sure to save your current changes before loading a new file. The editor does not check for unsaved changes. If you load a new file before saving, you will lose your changes.",
        "Save files are backed up every time they are loaded. You can find your save files in the backups directory. Backups are never automatically deleted."
        )],
    [createAboutTabHeader("Farmers Tab")],
    [createAboutTabDescription(
        "Change profile information for all players who have joined your world. This tab currently supports changing of each farmer's name, skill levels, and skill experience points."
    )]
]

layout = [
    [sg.TabGroup([[
        sg.Tab(Keys._LoadTab, load_tab_layout), 
        sg.Tab(Keys._FarmersTab, scrollableColumnWrapper(farmers_tab_layout, Keys._FarmersTabColumn), visible=False),
        sg.Tab(Keys._FriendshipTab, scrollableColumnWrapper(friendship_tab_layout, Keys._FriendshipTabColumn), visible=False),
        sg.Tab(Keys._SaveTab, save_tab_layout, visible=False),

        sg.Tab(Keys._BackupsTab, scrollableColumnWrapper(backups_tab_layout, Keys._BackupsTabColumn)),
        sg.Tab(Keys._AboutTab, scrollableColumnWrapper(about_tab_layout, Keys._AboutTabColumn))
    ]], expand_x=True, expand_y=True, enable_events=True, key=Keys._TabGroup)]
]