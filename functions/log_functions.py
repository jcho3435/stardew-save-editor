import datetime
import traceback
from functions.functions import get_current_time

def log_exceptions(e: Exception, starttime) -> str:
    time = datetime.datetime.now()
    file_name = f"y{time.year}_m{time.month}_d{time.day}_h{time.hour}_m{time.minute}_s{time.second}_ms{time.microsecond//1000}_{type(e).__name__}.log"
    f = open(f"logs\\{file_name}", "w")
    f.write("An exception has occurred!\n")
    f.write(f"Last run: {starttime} - Exception occurred at {time}\n\n")
    f.write(f"Exception type: {type(e).__name__}\n")
    f.write(f"Exception message: {e}\n")
    f.write(f"Exception args: {e.args}\n\n")
    f.write(f"Stack trace: {e.__traceback__}\n")
    f.write(f"{traceback.format_tb(e.__traceback__)}".replace("\\n", "\n"))
    f.close()

    event_log = f"[{get_current_time()}] [ERROR] An exception has occurred!\n"
    event_log += f"{' '*19}Exception type: {type(e).__name__}\n"
    event_log += f"{' '*19}Exception message: {e}\n"
    event_log += f"{' '*19}See error log \"logs/{file_name}\" for more details.\n\n"

    return event_log

def log_events(events: str, starttime: datetime.datetime):
    closetime = datetime.datetime.now()
    fname = f"EventLog_{starttime.year}-{starttime.month}-{starttime.day}.log"
    f = open(f"logs\\{fname}", "a")
    f.write(events)
    f.write(f"Closed {closetime} - - - - - - - - -\n\n")
    f.close()