import time
from datetime import datetime

def timeSection():
    delay = 10  # Seconds
    now = datetime.now()
    timestamp = "%0.2d:%0.2d:%0.2d" % (now.hour, now.minute, now.second)
    print(timestamp)
    f = open("output.txt", "a")
    f.write("Now Time is " + timestamp + "\n")
    f.close()
    time.sleep(delay)
    timeSection()
timeSection()