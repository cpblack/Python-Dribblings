import fs
logFolder = "logs"
items = fs.get(logFolder)


def analyzeServer(nameIn):
    serverTotal = 0.0
    serverTips = 0.0
    if items != False and len(items) > 0:
        t = 0
        while t < len(items):
            item = fs.readreceipt(logFolder+"/"+items[t])
            if item[6] == nameIn:
                serverTotal = serverTotal + float(item[3])
                serverTips = serverTotal + float(item[4])
            t = t + 1
    else:
        print("#Error: No logs.")
    return [serverTotal,serverTips]
while True:
    serverTarget = raw_input("Analyze Which Server?\n")
    serverProceeds = analyzeServer(serverTarget)
    print(serverTarget+" made $"+str(serverProceeds[0])+" for the restaraunt,\nand $"+str(serverProceeds[1])+" in tips.")
raw_input("Press enter to continue...")
