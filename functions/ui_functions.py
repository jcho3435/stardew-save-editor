'''
Holds definitions for functions for modifying the UI
'''

import PySimpleGUI as sg
import components.constants as constants, components.vars as vars

def hide_rows(window: sg.Window, keys: list | str):
    if type(keys) == str:
        window[keys].hide_row()
    else:
        for key in keys:
            window[key].hide_row()

def unhide_rows(window: sg.Window, keys: list | str):
    if type(keys) == str:
        window[keys].unhide_row()
    else:
        for key in keys:
            window[key].unhide_row()

def set_visibility(window: sg.Window, keys: list | str, isVisible: bool):
    if type(keys) == str:
        window[keys].update(visible = isVisible)
    else:
        for key in keys:
            window[key].update(visible = isVisible)

def col_contents_changed(window: sg.Window, key: str):
    window.refresh()
    window[key].contents_changed()

