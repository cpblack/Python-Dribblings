import fs
global colors
colors = fs.interpret(fs.read("colors.txt"))
def askColor():
    global colors
    colorReturn = "Do not make this a color name"
    while not colorReturn in colors:
        colorReturn = raw_input("Please enter a color.\n").lower()
    return colorReturn
def nearestColor(colorIn):
    global colors
    keys = colors.keys()
    smallest = ["superwhite",256,256,256]
    t = 0
    while t < len(keys):
        check = colors[keys[t]]
        check = [check[0],float(check[1]),float(check[2]),float(check[3])]
        checkDifference = abs(check[1] - colorIn[0]) + abs(check[2] - colorIn[1]) + abs(check[3] - colorIn[2])
        currentDifference = abs(smallest[1] - colorIn[0]) + abs(smallest[2] - colorIn[1]) + abs(smallest[3] - colorIn[2])
        if checkDifference < currentDifference:
            smallest = check
        t = t + 1;
    return smallest


#Run
currentColor = [127.5,127.5,127.5]
print "Colors:",", ".join(colors).title()
print "Starting Color: Grey"
while True:
    addColor = askColor()
    currentColor = [(currentColor[0]+float(colors[addColor][1]))/2,(currentColor[1]+float(colors[addColor][2]))/2,(currentColor[2]+float(colors[addColor][3]))/2]
    colorName = nearestColor(currentColor)
    colorName = colorName[0]
    print "Color:",colorName.title(),str(int(currentColor[0]/255*100))+"%,"+str(int(currentColor[1]/255*100))+"%,"+str(int(currentColor[2]/255*100))+"%"
