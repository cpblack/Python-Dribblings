import datetime
import fs
import os
logFolder = "logs"

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
	tax = cost * 0.07
	tip = cost * 0.15
	total = cost + tax + tip
	print str(name+":")
	print str("Meal  $"+str(cost))
	print str("+Tax  $"+str(tax))
	print str("+Tip  $"+str(tip))
	print str("Ttl:  $"+str(total))
	printeddate = str(thedate.month)+"/"+str(thedate.day)+"/"+str(thedate.year)+", "+str(hour)+":"+str(minute)+dayhalf
	print printeddate
	filename = logFolder+str(thedate.month)+"⧸"+str(thedate.day)+"⧸"+str(thedate.year)+" "+str(hour)+"꞉"+str(minute)+" "+name+".txt"
	fs.save(filename,["Name: "+name,"Date: "+printeddate,"Meal: $"+str(cost),"Tax: $"+str(tax)+"Tip: $"+str(tip),"Total: $"+str(total)])
try:
	while True:
		receipt()
except:
	print("#ERROR: Fatal Error")
