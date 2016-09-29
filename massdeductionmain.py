import battery
import time
import sheets
import fs
from datetime import datetime
def saveLog(state):
    date = datetime.now()
    stateFormatted = []
    stateFormatted.append(str(state))

    fs.save("%s-%s-%s - %s.%s.%s.txt"%(date.month,date.day,date.year,date.hour,date.minute,date.second),stateFormatted) 


print "Script Starting"
while True:
    status = battery.powerStatus()
    sheets.write("b5",status.ACLineStatus)
    print "Saving b5 as %s." %(status.ACLineStatus)
    saveLog(status.ACLineStatus)
    print "Sleeping"
    time.sleep(3)
