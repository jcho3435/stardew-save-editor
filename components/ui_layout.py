import PySimpleGUI as sg
from components.constants import Keys, _Links

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


# Layouts
load_tab_layout = [
        [sg.Push(), sg.Text("Stardew Valley Save Editor!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
        [sg.Text("Folder:", size=5), sg.Input(expand_x=True, key=Keys._FolderInput, enable_events=True, disabled=True), sg.FolderBrowse("Select Save Folder", key=Keys._FolderBrowser)],
        [sg.Text("Note: By default, save folders are located at C:\\Users\\[USER]\\AppData\\Roaming\\StardewValley\\Saves\\[SaveName]_#########", text_color="black", justification="center", expand_x=True)],
        [sg.Text("", size=4), sg.Text("", key=Keys._ValidateFolder)],
        [sg.Text("", size=4), sg.Text("", key=Keys._SaveWarning, text_color="black")]
    ]

farmers_tab_layout = [
    [sg.Text("Change Farmer Data", font=("Times New Roman", 15))],
]
generateFarmersFrames(farmers_tab_layout)

save_tab_layout = [
    [sg.Button("Save Changes")]
]

about_tab_layout = [
    [sg.Text("About the editor:", text_color="black", font=("Times New Roman", 30), pad=(5, (3, 10)))],
    [sg.Text("This application is a minimalist stardew valley save editor for windows. The code is fully open source and can be found", p=((5, 0), 6), text_color="black", font=("Arial", 14)), sg.Text("here.", tooltip=_Links["github"], p=(1, 6), enable_events=True, key=f"URL {_Links["github"]}", text_color="dark gray", font=("Arial", 14, "underline"))],
    
]

layout = [
    [sg.TabGroup([[
        sg.Tab("Load", load_tab_layout), 
        sg.Tab(Keys._FarmersTab, scrollableColumnWrapper(farmers_tab_layout), visible=False),
        sg.Tab(Keys._SaveTab, save_tab_layout, visible=False),


        sg.Tab(Keys._AboutTab, about_tab_layout, )
        ]], expand_x=True, expand_y=True)]
]







# Importable functions
def enable_farmer_frame(window: sg.Window, farmerName, index):
    window[Keys._FarmerNames[index]].update(farmerName, disabled=False)
    window[Keys._FarmerFrames[index]].update(visible=True)