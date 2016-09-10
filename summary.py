import os
import fs
logFolder = "logs"
def readreceipt(name):
	file = fs.read(name)
	name = file[0]
	name = name[6:]
	date = file[1]
	date = date[6:]
	meal = file[2]
	meal = meal[6:]
	tax = file[3]
	tax = tax[5:]
	tip = file[4]
	tip = tip[5:]
	total = file[6]
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
