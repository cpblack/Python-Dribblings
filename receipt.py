import datetime
import fs
import os
logFolder = fs.read("config.txt")
logFolder = logFolder[2]
logFolder = logFolder[10:]

if not os.path.exists(logFolder):
		try:
			os.makedirs(logFolder)
		except OSError as exc: 
			if exc.errno != errno.EEXIST:
				raise
def isnumber(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def receipt():
	name = ""
	while name == "":
		name = raw_input("What is the name?\n")
	name = name.title()
	cost = "false"
	while isnumber(cost) == False:
		cost = raw_input("What was the cost?\n")
	cost = float(cost)
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
	tax = fs.read("config.txt")
	tip = tax[1]
	tax = tax[0]
	tax = tax[5:] * cost
	tip = tip[5:] * cost
	total = cost + tax + tip
	print str("\n-- "+name+" --")
	print str("Meal  $"+str(cost))
	print str("+Tax  $"+str(tax))
	print str("+Tip  $"+str(tip))
	print str("Ttl:  $"+str(total))
	printeddate = str(thedate.month)+"/"+str(thedate.day)+"/"+str(thedate.year)+", "+str(hour)+":"+str(minute)+dayhalf
	print printeddate
	print "================\n"
	filename = str(thedate.month)+"-"+str(thedate.day)+"-"+str(thedate.year)+" "+str(hour)+"."+str(minute)+dayhalf+" "+name
	copynumber = 0
	copytag = ""
	while os.path.exists(logFolder+"/"+filename+copytag+".txt"):
		copynumber = copynumber + 1
		copytag = " ("+str(copynumber)+")"
	fs.save(logFolder+"/"+filename+copytag+".txt",["Name: "+name,"Date: "+printeddate,"Meal: $"+str(cost),"Tax: $"+str(tax),"Tip: $"+str(tip),"Total: $"+str(total)])
try:
	while True:
		receipt()
except:
	print("#ERROR: Fatal Error")
