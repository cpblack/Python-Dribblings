# Dependant on Library found Here: https://github.com/python-escpos/python-escpos
from escpos.printer import Usb
def config():
	from escpos import config
	c = config.Config()
	c.load()
def setup():
	return None
def printReceipt(tableIn):
	t = 0
	while t < len(tableIn):
		p.text(tableIn[t]+"\n")
		t = t + 1
	p.cut()
