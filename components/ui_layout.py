import PySimpleGUI as sg
from components.constants import Keys, _AllFriendableNPCs, _CURRENTVERSION, Seasons, WeatherPatterns
from components.vars import _Links, _BASEPATH, _Set_Backups_Dict
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
        [sg.Listbox(choices, size=(40, 12), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key=f"{Keys._BackupsTabListboxPrefix}:{backup_name}"), sg.Button("Delete All", button_color="red", key=f"{Keys._DeleteAllBackupsPrefix}:{backup_name}")],
    ]

    return sg.Frame(backup_name, frame_layout, pad=(5, (3, 12)), expand_x=True, key=f"{Keys._BackupsTabFramePrefix}:{backup_name}")

def generateBackupTabFrames(backups_tab_layout: list, frame_column_key: str):
    '''
    Initial generation of all backups. Each world gets its own frame. Stores the name of all backups in global variable _Backups
    '''
    import os
    backups = {}
    col_layout = []

    for folder in os.listdir("backups"):
        backup_name = "_".join(folder.split("_")[0:-1])
        backups[backup_name] = True
        choices = sorted(os.listdir(f"backups/{folder}"), reverse=True)
        if choices == []:
            os.rmdir(f"backups/{folder}")
        else:
            col_layout.append([createBackupFrame(backup_name, choices)])

    backups_tab_layout.append([sg.Column(col_layout, key=frame_column_key), sg.Push()]) # This additional column is needed to contain the frames that are hidden/unhidden so that they do not shift sideways
    
    _Set_Backups_Dict(backups)

def createTabHeader(text):
    return sg.Text(text, font=("Times New Roman", 16), pad=(5, (3, 10)))

def createAboutTabHeader(text):
    return sg.Text(text, font=("Times New Roman", 16, "underline"), text_color="black", pad=5)

def createAboutTabDescription(*args, **kwargs):
    text = ""
    for arg in args:
        text += textwrap.fill(arg, 170)
        text += "\n\n"
    #TODO: consider trimming the ending \n\n
    if "blist" in kwargs:
        text = text.strip("\n")
        text += "\n"
        for item in kwargs["blist"]:
            text += f"  • {item}\n"
        text += "\n"

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
        [sg.Text("", size=4), sg.Text("Note: By default, save folders are located at C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black")],
        [sg.Text("", size=4), sg.Text("", key=Keys._ValidateFolder)],
        [sg.Text("", size=4), sg.Text("", key=Keys._SaveWarning, text_color="black")]
    ]

farmers_tab_layout = [ # FARMERS
    [createTabHeader("Change Farmer Data")],
]
generateFarmersTabFrames(farmers_tab_layout)

friendship_tab_layout = [ # FRIENDSHIP
    [createTabHeader("Change Friendship Data")],
    [sg.Text("Select farmer:", pad=(5, (3, 20))), sg.Combo([], size=32, enable_events=True, key=Keys._FriendshipTabFarmerCombo, readonly=True, pad=(5, (3, 20)))]
]
friendship_tab_npcs = [[sg.Sizer(350, 0)]] + [[sg.Image(f"{_BASEPATH}/icons/npcs/{npc}.png", subsample=2), sg.Text(f"{npc}:", p=(5, 8)), sg.Input(key=Keys._NPCFriendshipPoints[npc], disabled=True, p=((0, 5), 8), size=18, disabled_readonly_background_color="#cfcfcf")] for npc in sorted(_AllFriendableNPCs)]
friendship_tab_layout += [[sg.Frame("Friendship Points", friendship_tab_npcs, expand_x=True, expand_y=True)]]

world_tab_layout = [ # WORLD
    [createTabHeader("Change World Data")],
    [sg.Image(f"{_BASEPATH}/icons/calendar-icon.png", subsample=2), sg.Text("Day:"), sg.Input(key=Keys._WorldDayOfMonth, size=4, p=((0, 5), 8)), sg.Text("Season:"), sg.Combo([season.name.capitalize() for season in Seasons], key=Keys._WorldSeason, size=10, p=((0, 5), 8), readonly=True), sg.Text("Year:"), sg.Input(key=Keys._WorldYear, size=6, p=((0, 5), 8))],
    [sg.Text("Note: Currently, this editor does not support setting stormy weather.", p=(5, (8, 3)))],
    [sg.Text("Weather:", p=(5, (3, 8))), sg.Combo([weather.name for weather in WeatherPatterns], size=12, key=Keys._WorldWeather, p=(0, (3, 8)), readonly=True), sg.Image(None, key=Keys._WorldTabWeatherImage)]
]

save_tab_layout = [ # SAVE
    [createTabHeader("Save Changes")],
    [sg.Button("Save Changes")]
]

backups_tab_layout = [ # BACKUPS
    [createTabHeader("Backups Manager")],
    [sg.Button("Delete All Backups", button_color="red", p=(5, 3, 12)), sg.Button("Delete Selected", p=(5, 3, 12))]
]
generateBackupTabFrames(backups_tab_layout, Keys._BackupsTabFramesColumn)

about_tab_layout = [ # ABOUT
    [sg.Text("About the editor:", text_color="black", font=("Times New Roman", 30), pad=(5, (3, 10)))],
    [sg.Text("This application is a minimalist Stardew Valley save editor for windows. The code is fully open source and can be found", p=((5, 0), 3), text_color="black", font=("Arial", 12)), sg.Text("here.", tooltip=_Links["github"], p=(1, 3), enable_events=True, key=f"URL {_Links["github"]}", text_color="dark gray", font=("Arial", 12, "underline"))],
    [sg.Text("This page gives a basic overview of the editor's tabs. For more detailed docs and explanations on each of the tabs' fields, view the web based docs", p=((5, 0), 3), text_color="black", font=("Arial", 12)), sg.Text("here,", tooltip=_Links["docs"], p=(0, 3), enable_events=True, key=f"URL {_Links["docs"]}", text_color="dark gray", font=("Arial", 12, "underline")), sg.Text("or view the GitHub wiki", p=(1, 3), text_color="black", font=("Arial", 12)), sg.Text("here.", tooltip=_Links["github wiki"], p=((0, 5), 3), enable_events=True, key=f"URL {_Links["github wiki"]}", text_color="dark gray", font=("Arial", 12, "underline"))],
    [sg.Text(textwrap.fill("Warning: There is no input validation on any of the modifiable fields, so in order to avoid Stardew Valley crashing due to bad save data, avoid inputting bad values. For example, for fields which should take a number, do not input any alphabetical characters. You can find more details on constraints on values for each field on the docs.", 170), p=((5, 0), (3, 22)), text_color="black", font=("Arial", 12))],
    [createAboutTabHeader("Load Tab")],
    [createAboutTabDescription(
        "Load your save file here. Always make sure to save your current changes before loading a new file. The editor does not check for unsaved changes. If you load a new file before saving, you will lose your changes.",
        "Save files are backed up every time they are loaded. You can find your save files in the backups directory. Backups are never automatically deleted."
    )],
    [createAboutTabHeader("Farmers Tab")],
    [createAboutTabDescription(
        "Change profile information for all players who have joined your world. This tab currently supports changing of each farmer's:",
        blist=["Name", "Skill levels", "Skill experience points"],
    )],
    [createAboutTabHeader("Friendship Tab")],
    [createAboutTabDescription("Change friendship points with NPCs for all players who have joined your world. Use the dropdown menu to swap between farmers. Changed friendship points will be remembered when switching between players.")],
    [createAboutTabHeader("World Tab")],
    [createAboutTabDescription(
        "Change information associated with the world and not associated directly with individual players. Currently supports changing:",
        blist=["Date (day, season, year)", "Weather"]
        )],
    
    [createAboutTabHeader("Save Tab")],
    [createAboutTabDescription("Save your changes. After loading a game save, changes must be saved before you can load a new game save.")],
    [createAboutTabHeader("Backups Tab")],
    [createAboutTabDescription(
        "The backups manager currently only supports deleting backups. It is unlikely that it will ever support loading backups.",
        "The backups manager allows for deleting all backups, deleting all backups of a specific farm, and deleting selected backups, which are selected in the list boxes on the backup manager tab."
    )],

    [createAboutTabHeader("Version Info")],
    [sg.Text(f"Stardew Save Editor Version: {_CURRENTVERSION}\nPython version: 3.12.4\nPlatform: Windows\nPort: PySimpleGUI\ntkinter version: 8.6.13\nPySimpleGUI version: 5.0.6.12", font=("Arial", 12), text_color="black", expand_x=True)]
]

layout = [
    [sg.TabGroup([[
        sg.Tab(Keys._LoadTab, load_tab_layout), 
        sg.Tab(Keys._FarmersTab, scrollableColumnWrapper(farmers_tab_layout, Keys._FarmersTabColumn), visible=False),
        sg.Tab(Keys._FriendshipTab, scrollableColumnWrapper(friendship_tab_layout, Keys._FriendshipTabColumn), visible=False),
        sg.Tab(Keys._WorldTab, scrollableColumnWrapper(world_tab_layout, Keys._WorldTabColumn), visible=False),
        sg.Tab(Keys._SaveTab, save_tab_layout, visible=False),

        sg.Tab(Keys._SpacerTab, [[]], disabled=True, visible=False),
        sg.Tab(Keys._BackupsTab, scrollableColumnWrapper(backups_tab_layout, Keys._BackupsTabColumn)),
        sg.Tab(Keys._AboutTab, scrollableColumnWrapper(about_tab_layout, Keys._AboutTabColumn))
    ]], expand_x=True, expand_y=True, enable_events=True, key=Keys._TabGroup)]
]