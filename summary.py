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
	meal = meal[6:]
	tax = myfile[3]
	tax = tax[5:]
	tip = myfile[4]
	tip = tip[5:]
	total = myfile[6]
	total = total[6:]
	return [name,date,meal,tax,tip,total]

logs = [f for f in os.listdir(logFolder) if os.path.isfile(os.path.join(logFolder, f))]
t = 0
total = 0.0
while t < len(logs):
        check = readreceipt(logs[t])
        total = total + check[4]
        t = t + 1
print "Gross: "+total
