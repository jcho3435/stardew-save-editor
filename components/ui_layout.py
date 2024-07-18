import PySimpleGUI as sg
from components.constants import Keys

def generateFarmersFrames(farmers_tab_layout: list):
    for i in range(8):
        frame_layout = [[sg.Text("Farmer Name:"), sg.Input(key=Keys._FarmerNames[i])]]
        farmers_tab_layout.append([sg.Frame(f"Farmer {i+1} Profile", frame_layout, key=Keys._FarmerFrames[i], pad=(5, (3, 40)), expand_x=True, visible=False)])

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

layout = [
    [sg.TabGroup([[
        sg.Tab("Load", load_tab_layout), 
        sg.Tab(Keys._FarmersTab, scrollableColumnWrapper(farmers_tab_layout), visible=False),
        sg.Tab(Keys._SaveTab, save_tab_layout, visible=False)
        ]], expand_x=True, expand_y=True)]
]
