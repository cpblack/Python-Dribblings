#Caleb Black
#September 5th 2016
#Server Analyzer
import fs
config = fs.getconfig()
global logFolder
logFolder = config[2]
items = fs.get(logFolder)


def analyzeServer(nameIn):
    global llogFolder
    serverTotal = 0.0
    serverTips = 0.0
    if items != False and len(items) > 0:
        t = 0
        while t < len(items):
            item = fs.readreceipt(logFolder+"/"+items[t])
            if item[6] == nameIn:
                serverTotal = serverTotal + float(item[2])
                serverTips = serverTips + float(item[4])
            t = t + 1
    else:
        print("#Error: No logs.")
    return [serverTotal,serverTips]
while True:
    serverTarget = raw_input("Analyze Which Server?\n")
    serverTarget = serverTarget.title()
    serverProceeds = analyzeServer(serverTarget)
    print(serverTarget+" made $"+str(serverProceeds[0])+" for the restaraunt, and $"+str(serverProceeds[1])+" in tips.")
raw_input("Press enter to continue...")
