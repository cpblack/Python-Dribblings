import os
import fs
logFolder = "logs"
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
	return [name,date,meal,tax,tip,total]

logs = [f for f in os.listdir(logFolder) if os.path.isfile(os.path.join(logFolder, f))]
t = 0
ftotal = 0.0
while t < len(logs):
        check = readreceipt(logFolder+"/"+logs[t])
        ftotal = ftotal + float(check[5])
        t = t + 1
print "Gross: $"+str(ftotal)
