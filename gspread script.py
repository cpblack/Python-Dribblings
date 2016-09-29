#GSPREAD LIBRARY FOUND HERE: https://github.com/burnash/gspread
#OAUTH2 LIBRARY FOUND HERE: https://github.com/google/oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_key("1npB50U4RIShkm-DCEiwCy50fIaXajTYscdyRHh5T4hY")
wks = spreadsheet.sheet1

wks.update_acell('B2', "it's down there somewhere, let me take another look.")
