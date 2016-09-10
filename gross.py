import os
import fs
logFolder = fs.read("config.txt")
logFolder = logFolder[2]
logFolder = logFolder[10:]
def readreceipt(name):
	myfile = fs.read(name)
	name = myfile[0]
	name = name[6:]
	date = myfile[1]
	date = date[6:]
	meal = myfile[2]
	meal = meal[7:]
	tax = myfile[3]
	tax = tax[6:]
	tip = myfile[4]
	tip = tip[6:]
	total = myfile[5]
	total = total[8:]
	server = myfile[6]
	server = server[8:]
	return [name,date,meal,tax,tip,total,server]

if os.path.exists(logFolder):
	logs = [f for f in os.listdir(logFolder) if os.path.isfile(os.path.join(logFolder, f))]
	t = 0
	ftotal = 0.0
	while t < len(logs):
		check = readreceipt(logFolder+"/"+logs[t])
		ftotal = ftotal + float(check[5])
		t = t + 1
	print("Gross: $"+str(ftotal))
else:
	print("Log Folder Non-Existant.")

raw_input("Press Enter to continue...\n")
