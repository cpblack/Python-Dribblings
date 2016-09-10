def read(name):
	try:
		with open(name,'r') as f:
			lines = f.read().splitlines()
		f.close()
		return lines
	except:
		print("#ERROR @ FS.read")
		return "#ERROR"

def save(name,parameters):
	try:
			if not os.path.exists(os.path.dirname(name)):
		try:
			os.makedirs(os.path.dirname(name))
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
