import battery
import time
import sheets
import fs
from datetime import datetime
def fullDate():
    date = datetime.now()
    return "%s-%s-%s - %s.%s.%s"%(date.month,date.day,date.year,date.hour,date.minute,date.second)
def saveLog(name,state):
    fs.save(name+".txt",state) 


print "Script Starting"
scheduleT = file.open("schedule.txt","r")
schedule = scheduleT.read().split("\n")
for i,len(schedule):
    schedule[t] = schedule[t].split(":")
scheduleT.close()
while True:
    status = battery.powerStatus()
    sheets.write("b5",status.ACLineStatus)
    saveLog(fullDate(),status.ACLineStatus)
    print "Sleeping"
    time.sleep(3)

