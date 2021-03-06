#Caleb Black
#September 5th 2016
#Script Core
import os
def getconfig():
	if exists("config.txt") == False:
		save("config.txt",["tax: 7","tip: 15", "Log-Path: logs"])
	config = read("config.txt")
	tax = config[0]
	tax = tax[5:]
	tip = config[1]
	tip = tip[5:]
	logFolder = config[2]
	logFolder = logFolder[10:]
	return [tax,tip,logFolder]
def read(name):
	try:
		with open(name,'r') as f:
			lines = f.read().splitlines()
		f.close()
		return lines
	except:
		print("#ERROR @ FS.read")
		return "#ERROR"
def get(folder):
	output = False
	if os.path.exists(folder):
		output = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
	return output
def readreceipt(name):
	myfile = read(name)
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

def save(name,parameters):
	try:
		c = os.path.dirname(name)
		if not os.path.exists(c) and c != '':
			try:
				os.makedirs(c)
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise
		f = open(name,"w")
		t = 0
		while t < len(parameters):
			f.write(parameters[t]+"\n")
			t = t + 1
		f.close()
		return "#Success!"
	except:
		print("#ERROR @ FS.save")
		return("#ERROR")
def exists(pathIn):
	try:
		output = os.path.isfile(pathIn)
		return output
	except:
		print("#ERROR @ FS.exists")
		return "#ERROR"
