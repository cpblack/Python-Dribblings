import fs
logFolder = "logs"
items = fs.get(logFolder)
global server
server = []
server.append(['Jane',0.00])
def findServer(nameIn):
    global server
    myOutput = False
    t = 0
    while t < len(server):
        target = server[t]
        if myOutput == False and target[0] == nameIn:
            output = t
        t = t + 1

if items != False and len(items) > 0:
    t = 0
    while t < len(items):
        item = fs.readreceipt(logFolder+"/"+items[t])
        print(item[5])
        t = t + 1
    print(str(findServer('Jane')))
else:
    print("#Error: No logs.")
raw_input("Press enter to continue...")
