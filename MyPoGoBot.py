# LIBRARY DOCS https://github.com/tejado/pgoapi/wiki/
global loggedIn
global api
global settings
global loggedIn = False
from time import sleep
settings = {"logintype":"google","username":"reallyisfakeIthink@gmial.com","password":"thisisnottherealpassword"}
api = pgoapi.PGoApi()

def login():
	output = False
	if settings.logintype != "ptc" and settings.logintype != "google":
		print("ERROR: Invalid Login Type!")
		output = False
	else:
		success = rawLogin(settings.logintype,settings.username,settings.password)
		if success:
			output = True
			print "Login Success!"
		else:
			output = False
			print "Login Failure!"
	return output
	
def rawLogin(type,user,pass):
	global api
	return api.login(type,user,pass)
def recycle():
	req = api.create_request()
	req.release_pokemon(pokemon_id = <your_input>)
	req.release_pokemon(pokemon_id = <your_input>)
	req.release_pokemon(pokemon_id = <your_input>)
	response = req.call()
	

#########################################
#########################################
loginAttempts = 0
while loggedIn == False and loginAttempts < 6:
	loginAttempts = loginAttemps + 1
	print "Attemping Log In"
	loggedIn = login()
	if loggedIn == False:
		print "Login Failure, Sleeping!"
		sleep(10)
if loggedIn:
	print "Login Success! Starting Script"
	
else:
	print "Complete Login Failure!"
