import PySimpleGUI as sg
from components.constants import Keys, _Links
import textwrap

# helpers --------------------------------------------------------------------------------
def generateFarmersFrames(farmers_tab_layout: list):
    for i in range(8):
        frame_layout = [
            [sg.Text("Farmer Name:"), sg.Input(key=Keys._FarmerNames[i], disabled=True)]
            #Add more to frame- need to add skills and xp
            #skill levels are ordered in xml as farming, mining, combat, foraging, fishing, luck
            #skill exp points are ordered in farming/foraging, fishing, farming/foraging, mining, combat, luck(?)
            # TODO: Figure out if luck is a value that should be modified
        ]
        title = f"Farmer {i+1} Profile"
        if i == 0:
            title += " (World host)"
        farmers_tab_layout.append([sg.Frame(title, frame_layout, key=Keys._FarmerFrames[i], pad=(5, (3, 12)), expand_x=True, visible=False)])

def scrollableColumnWrapper(layout):
    return [[sg.Column(layout, scrollable=True, vertical_scroll_only=True, expand_x=True, expand_y=True)]]

def createAboutTabHeader(text):
    return sg.Text(text, font=("Times New Roman", 16, "underline"), text_color="black", pad=5)

def createAboutTabDescription(*args):
    text = ""
    for arg in args:
        text += textwrap.fill(arg, 170)
        text += "\n\n"
    #TODO: consider trimming the ending \n\n
    return sg.Text(text, font=("Arial", 12), text_color="black", expand_x=True)

# Layouts ---------------------------------------------------------------------------------
load_tab_layout = [
        [sg.Push(), sg.Text("Stardew Valley Save Editor!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
        [sg.Text("Folder:", size=5), sg.Input(expand_x=True, key=Keys._FolderInput, enable_events=True, disabled=True), sg.FolderBrowse("Select Save Folder", key=Keys._FolderBrowser)],
        [sg.Text("Note: By default, save folders are located at C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black", justification="center", expand_x=True)],
        [sg.Text("", size=4), sg.Text("", key=Keys._ValidateFolder)],
        [sg.Text("", size=4), sg.Text("", key=Keys._SaveWarning, text_color="black")]
    ]

farmers_tab_layout = [
    [sg.Text("Change Farmer Data", font=("Times New Roman", 16))],
]
generateFarmersFrames(farmers_tab_layout)

save_tab_layout = [
    [sg.Button("Save Changes")]
]

about_tab_layout = [
    [sg.Text("About the editor:", text_color="black", font=("Times New Roman", 30), pad=(5, (3, 10)))],
    [sg.Text("This application is a minimalist stardew valley save editor for windows. The code is fully open source and can be found", p=((5, 0), 3), text_color="black", font=("Arial", 12)), sg.Text("here.", tooltip=_Links["github"], p=(1, 3), enable_events=True, key=f"URL {_Links["github"]}", text_color="dark gray", font=("Arial", 12, "underline"))],
    [sg.Text("For detailed docs and explanations on each tab's fields, click", p=((5, 0), 3), text_color="black", font=("Arial", 12)), sg.Text("here.", tooltip=_Links["docs"], p=(1, 3), enable_events=True, key=f"URL {_Links["docs"]}", text_color="dark gray", font=("Arial", 12, "underline"))],
    [sg.Text("Warning: There is no input validation on any of the modifiable fields, so in order to avoid crashing due to bad save data, avoid inputting bad values. For example, for fields which should take a number, do not input and alphabetical characters.", p=((5, 0), (3, 22)), text_color="black", font=("Arial", 12))],
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
        sg.Tab("Load", load_tab_layout), 
        sg.Tab(Keys._FarmersTab, scrollableColumnWrapper(farmers_tab_layout), visible=False),
        sg.Tab(Keys._SaveTab, save_tab_layout, visible=False),


        sg.Tab(Keys._AboutTab, scrollableColumnWrapper(about_tab_layout))
        ]], expand_x=True, expand_y=True)]
]







# Importable functions ------------------------------------------------------------------------------------
def enable_farmer_frame(window: sg.Window, farmerName, index):
    window[Keys._FarmerNames[index]].update(farmerName, disabled=False)
    window[Keys._FarmerFrames[index]].update(visible=True)