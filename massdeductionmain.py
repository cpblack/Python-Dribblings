import battery
import time
import sheets
import fs
from datetime import datetime
def fullDate():
    date = datetime.now()
    return "%s-%s-%s - %s.%s.%s"%(date.month,date.day,date.year,date.hour,date.minute,date.second)



print "Script Starting"
scheduleT = file.open("schedule.txt","r")
schedule = scheduleT.read().split("\n")
for i,len(schedule):
    schedule[t] = schedule[t].split(":")
scheduleT.close()

while False:
    status = battery.powerStatus()
    sheets.write("b5",status.ACLineStatus)
    fs.save(fullDate()+".txt",status.ACLineStatus)
    print "Sleeping"
    time.sleep(3)

print schedule
