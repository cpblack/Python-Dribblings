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
tax = cost * 0.07
tip = cost * 0.15
total = cost + tax + tip
print str(name+":")
print str("Meal $"+str(cost))
print str("+Tax $"+str(tax))
print str("+Tip $"+str(tip))
print str("Ttl: $"+str(total))
print str(thedate.month)+"/"+str(thedate.day)+"/"+str(thedate.year)+", "+str(hour)+":"+minute,dayhalf
fs.save(thedate.month+"-"+thedate.day+"-"+thedate.year,name+".txt",["Name: "+name,"Date: "+str(thedate.month)+"/"+str(thedate.day)+"/"+str(thedate.year)+", "+str(hour)+":"+minute,dayhalf,"Meal: $"+str(cost),"Tax: $"+str(tax)"Tip: $"+str(tip),"Total: $"+str(total)])
