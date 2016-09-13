#Caleb Black
#September 5th 2016
#Gross Calculator
import os
import fs
config = fs.getconfig()
logFolder = config[2]

if os.path.exists(logFolder):
	logs = [f for f in os.listdir(logFolder) if os.path.isfile(os.path.join(logFolder, f))]
	t = 0
	ftotal = 0.0
	while t < len(logs):
		check = fs.readreceipt(logFolder+"/"+logs[t])
		ftotal = ftotal + float(check[3])
		t = t + 1
	print("Income (w/o tips & sales tax): $"+str(ftotal))
else:
	print("Log Folder Non-Existant.")

raw_input("Press Enter to continue...\n")
