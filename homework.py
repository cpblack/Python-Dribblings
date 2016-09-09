import datetime
import fs
thetime = datetime.datetime.now().time()
thedate = datetime.datetime.now().date()
hour = thetime.hour
dayhalf = "AM"
if hour > 12:
    hour = hour - 12
    dayhalf = "PM"
minute = thetime.minute
if minute < 10:
    minute = "0"+str(minute)

name = raw_input("What is the name?\n")
cost = input("What was the cost?\n")
print str(name+":")
print str("Meal $"+str(cost))
print str("+Tax $"+str(cost*0.07))
print str("+Tip $"+str(cost*0.15))
print str("Ttl: $"+str(cost*0.22))
print str(thedate.month)+"/"+str(thedate.day)+"/"+str(thedate.year)+", "+str(hour)+":"+minute,dayhalf
fs.save(thedate.month+"-"+thedate.day+"-"+thedate.year,name+".txt")
