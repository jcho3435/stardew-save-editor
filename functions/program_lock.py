import os
import datetime

_lock_file = "tmp\\program.lock"

def is_running():
    if not os.path.isdir("tmp"):
        os.mkdir("tmp")
    if os.path.exists(_lock_file):
        return True
    else:
        open(_lock_file, 'w').close()  # Create the lock file
        return False

def clean_up(e: Exception = None):
    os.remove(_lock_file)
    if e != None:
        raise Exception(e)

def log_closed_run():
    time = datetime.datetime.now()
    file_name = f"y{time.year}_m{time.month}_d{time.day}_h{time.hour}_m{time.minute}_s{time.second}_ms{time.microsecond//1000}_duplicate_run.log"
    f = open(f"logs\\{file_name}", "w")
    f.write(f"Last run: {str(time)}\n")
    f.write("The program was automatically closed due to an instance already being run. \nIf this is a mistake, delete 'tmp/program.lock' then run the program again.\n")
    f.close()