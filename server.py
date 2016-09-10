import fs
items = fs.get("logs")
if items != False:
  print items[0]
