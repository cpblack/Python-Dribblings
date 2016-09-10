import fs
raw_input("Analyze Which Server?")
logFolder = "logs"
items = fs.get(logFolder)


def analyzeServer(nameIn):
        serverTotal = 0.0
    if items != False and len(items) > 0:
        t = 0
        while t < len(items):
            item = fs.readreceipt(logFolder+"/"+items[t])
            if item[6] == nameIn:
                serverTotal = serverTotal + item[5]
            t = t + 1
    else:
        print("#Error: No logs.")
print str(analyzeServer('Jane'))
raw_input("Press enter to continue...")
