# LIBRARY DOCS https://github.com/tejado/pgoapi/wiki/
global loggedIn
global api
global settings
settings = {"logintype":"google","username":"tomatojerky@gmail.com","password":"thisisnottherealpassword"}
api = pgoapi.PGoApi()

def login():
	if settings.logintype != "ptc" and settings.logintype != "google":
		print("ERROR: Invalid Login Type!")
	else:
		rawLogin(settings.logintype,settings.username,settings.password)
def rawLogin(type,user,pass):
	global api
	api.login(type,user,pass)
