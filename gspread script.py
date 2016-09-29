#GSPREAD LIBRARY FOUND HERE: https://github.com/burnash/gspread
#OAUTH2 LIBRARY FOUND HERE: https://github.com/google/oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
pluggedInSheetKey = "1npB50U4RIShkm-DCEiwCy50fIaXajTYscdyRHh5T4hY"
def initialize(keyIn):
	global gc
	global wks
	global spreadsheet
	global initialized
	scope = ['https://spreadsheets.google.com/feeds']
	
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
	
	gc = gspread.authorize(credentials)
	
	spreadsheet = gc.open_by_key(keyIn)
	wks = spreadsheet.sheet1
	initialized = True
def read(cell):
	global wks
	global spreadsheet
	global initialized
	global gc
	while initialized != True:
		print "Initializing."
		initialize(pluggedInSheetKey)
	val = wks.acell(cell).value
def write(cell,content):
	global wks
	global spreadsheet
	global initialized
	global gc
	while initialized != True:
		print "Initializing."
		initialize(pluggedInSheetKey)
	wks.update_acell(cell,content)
if __name__ == "__main__":
	while True:
		write(raw_input("Please enter a cell\n"),raw_input("Write what?\n"))
	
