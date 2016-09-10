import fs
logFolder = "logs"
items = fs.get(logFolder)
if items != False and len(items) > 0:
    t = 0
    while t < len(items):
        item = fs.readreceipt(logFolder+"/"+items[t])
        print(item[5])
        t = t + 1
else:
    print("#Error: No logs.")
raw_input("Press enter to continue...")
