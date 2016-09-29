#LIBRARY FOUND HERE: https://github.com/burnash/gspread
import gspread

gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("Where is the money Lebowski?").sheet1

wks.update_acell('B2', "it's down there somewhere, let me take another look.")
