import datetime
import fs
import os
import epsonprinterpos as printer
config = fs.getconfig()
logFolder = config[2]

global server
server = "No server."
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
	global server
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
	tax = float(tax[5:])/100 * cost
	tip = float(tip[5:])/100 * cost
	total = cost + tax + tip
	print str("\n-- "+name+" --")
	print "Server: "+server
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
	fs.save(logFolder+"/"+filename+copytag+".txt",["Name: "+name,"Date: "+printeddate,"Meal: $"+str(cost),"Tax: $"+str(tax),"Tip: $"+str(tip),"Total: $"+str(total),"Server: "+server])

try:
	server = raw_input("Please enter server name.\n")
	server = server.title()
	while True:
		receipt()
except:
	print("#ERROR: Fatal Error")
