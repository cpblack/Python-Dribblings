import fs
global red
global blue
global green
global cyan
global magenta
global yellow
def interpret(tableIn):
    t = 0
    output = {}
    while t < len(tableIn):
        temp = tableIn[t].split(":")
        output[temp[0]] = temp[1]
        t = t + 1
    return output

def initializeBlends():
    global red
    global blue
    global green
    global cyan
    global magenta
    global yellow
    red = fs.read("red.txt")
    blue = fs.read("blue.txt")
    green = fs.read("green.txt")
    cyan = fs.read("cyan.txt")
    magenta = fs.read("magenta.txt")
    yellow = fs.read("yellow.txt")
    red = interpret(red)
    blue = interpret(blue)
    green = interpret(green)
    cyan = interpret(cyan)
    magenta = interpret(magenta)
    yellow = interpret(yellow)

def blend(color1,color2):
    color1 = color1.lower()
    color2 = color2.lower()
    output = "null"
    if color1 == "red":
        try:
            output = red[color2]
        except:
            None
    elif color1 == "blue":
        try:
            output = blue[color2]
        except:
            None
    elif color1 == "green":
        try:
            output = green[color2]
        except:
            None
    elif color1 == "cyan":
        try:
            output = cyan[color2]
        except:
            None
    elif color1 == "magenta":
        try:
            output = magenta[color2]
        except:
            None
    elif color1 == "yellow":
        try:
            output = yellow[color2]
        except:
            None


    if output == "null":
        if color2 == "red":
            try:
                output = red[color1]
            except:
                None
        elif color2 == "blue":
            try:
                output = blue[color1]
            except:
                None
        elif color2 == "green":
            try:
                output = green[color1]
            except:
                None
        elif color2 == "cyan":
            try:
                output = cyan[color1]
            except:
                None
        elif color2 == "magenta":
            try:
                output = magenta[color1]
            except:
                None
        elif color2 == "yellow":
            try:
                output = yellow[color1]
            except:
                None


    
    return output
initializeBlends()
while True:
    print "red:",red
    print "blue:",blue
    print "green:",green
    print "cyan:",cyan
    print "yellow:",yellow
    print "magenta",magenta
    mix = blend(raw_input("What is the first color?\n"),raw_input("What is the second color?\n"))
    mix = mix.title()
    print "Your combination is",mix+"!"

