from datetime import datetime
import time
import subprocess
import os

sleeptime = 0
lastChime = datetime(year=2000,month=1,day=1)
period = 15

while True:

    if sleeptime > 0:
        print("Sleeping for %d minutes and %d seconds" % (sleeptime / 60, sleeptime % 60))
        time.sleep(sleeptime)

    s = datetime.now()
    hrs = s.hour
    mins = s.minute
    secs = s.second
    print("It is currently %d:%02d:%02d" % (hrs,mins,secs))

    if hrs < 7:
        sleeptime = 3600
        continue
    
    diff = s - lastChime
    e = os.environ
    e['PULSE_SINK'] = "0"
    
    if mins % period == 0 and diff.total_seconds() > ((period-1) * 60):
        if s.minute == period:
            subprocess.run(args=["cvlc", "%s/etc/chimer/marimba2.wav" % os.environ['HOME']], env=e)
        elif s.minute == (period * 2):
            subprocess.run(args=["cvlc", "%s/etc/chimer/marimba3.wav" % os.environ['HOME']], env=e)
        elif s.minute == (period * 3):
            subprocess.run(args=["cvlc", "%s/etc/chimer/marimba4.wav" % os.environ['HOME']], env=e)
        else:
            subprocess.run(args=["cvlc", "%s/etc/chimer/marimba1.wav" % os.environ['HOME']], env=e)
        lastChime = s
        sleeptime = (period-1) * 60 + 59
        continue
    
    sleeptime = (period - (mins % period) - 1) * 60 + (60-secs)
