import os
import fs
logFolder = fs.read("config.txt")
logFolder = logFolder[2]
logFolder = logFolder[10:]

if os.path.exists(logFolder):
	logs = [f for f in os.listdir(logFolder) if os.path.isfile(os.path.join(logFolder, f))]
	t = 0
	ftotal = 0.0
	while t < len(logs):
		check = fs.readreceipt(logFolder+"/"+logs[t])
		ftotal = ftotal + float(check[5])
		t = t + 1
	print("Gross: $"+str(ftotal))
else:
	print("Log Folder Non-Existant.")

raw_input("Press Enter to continue...\n")
