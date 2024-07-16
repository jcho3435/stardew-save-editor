import datetime
import traceback

def log_exceptions(e: Exception, starttime):
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

def log_events(events: str, starttime: datetime.datetime):
    closetime = datetime.datetime.now()
    fname = f"EventLog_{starttime.year}-{starttime.month}-{starttime.day}.log"
    f = open(f"logs\\{fname}", "a")
    f.write(events)
    f.write(f"Closed {closetime} - - - - - - - - -\n\n")
    f.close()