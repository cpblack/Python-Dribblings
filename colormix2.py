import fs
global red
global blue
global green
global cyan
global magenta
global yellow
global config
global colorKeys
config = ["red","green","blue","magenta","yellow","cyan"]
def interpret(tableIn):
    t = 0
    output = {}
    while t < len(tableIn):
        temp = tableIn[t].split(":")
        output[temp[0]] = temp[1]
        t = t + 1
    return output
def initializeBlends():
    global colorIndex
    global config
    global colorKeys = []
    colorIndex = {}
    t = 0
    while t < len(config):
      colorIndex[config[t]] = interpret(fs.read(config[t]+".txt"))
      colorKeys[t] = config[t]
      t = t + 1
def blend(color1,color2):
  global colorIndex
  global colorKeys
  color1 = color1.lower()
  color2 = color2.lower()
  output = "null"
  key = findColor(color1)
  if key != "null":
    try:
      output = colorIndex[colorKeys[key]][color2]
    catch:
      None
  return output
def findColor(colorName):
  global colorKeys
  t = 0
  output = "null"
  while t < len(colorKeys):
    if colorKeys[t] == colorName:
      output = t
    t = t + 1
  return output


    
    return output
initializeBlends()

while True:
    print colorIndex

    mix = blend(raw_input("What is the first color?\n"),raw_input("What is the second color?\n"))
    print "Your combination is",mix.title()+"!"
    while mix != "restart" and mix != "null":
        mix = blend(mix, raw_input('Enter another color to continue mixing or type "restart".\n'))
        if mix == "null":
            print "Mixing Error."
        else:
            print "Your combination is",mix.title()+"!"
    
