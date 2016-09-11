# Dependant on Library found Here: https://github.com/python-escpos/python-escpos
def printReceipt(tableIn):
	t = 0
	while t < len(tableIn):
		p.text(tableIn[t]+"\n")
		t = t + 1
	p.cut()
