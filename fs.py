def read(name):
	try:
		with open('C:/path/numbers.txt','r') as f:
    	lines = f.read().splitlines()
    f.close()
		return lines
	except:
		print("#ERROR @ FS.read")
		return "#ERROR"

def save(name,parameters)
	try:
		f = open(name,"w")
		for i,1   
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
