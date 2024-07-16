import os
import datetime

def init_directories():
    if not os.path.isdir("backups"):
        os.mkdir("backups")
    if not os.path.isdir("logs"):
        os.mkdir("logs")

def get_current_time(include_microseconds = False):
    return datetime.datetime.now().time() if include_microseconds else datetime.datetime.now().time().replace(microsecond=0)

def create_backup(folderpath):
    pass