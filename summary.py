import os
import fs
logFolder = "logs"
def readreceipt(name):
	file = fs.read(name)
	name = file[0]
	name = name[6:]
	return name
print(readreceipt(logFolder+"/"+"9-10-2016 1.27PM Angel"))
