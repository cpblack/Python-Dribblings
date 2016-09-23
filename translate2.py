try:
    import fs
except:
    raw_input("FATAL ERROR! fs.py missing, press enter to continue")
from re import sub as re.sub

def getLanguage():
    global language
    language = "this should not be used as a language name"
    while fs.exists("translations/"+language+".txt") == False and language.lower() != "pig latin":
        language = raw_input("Please enter the name of your language file located in the Translations folder\n")
    return 
def getAddAll():
    addAllLocal = ""
    global dictionary
    if "*" in dictionary:
        addAllLocal = dictionary["*"]
        dictionary["*"] = "*"
    return addAllLocal
def smartAddAll(string1, string2):
    cutRepeats = True
    output = string1 + string2
    if cutRepeats and string1[-1:] == string2[0:1]:
        output = string1[:-1] + string2
    return output
def translate(stringIn):
    global dictionary
    global addAll
    global language
    if language.lower() != "pig latin":
        stringIn = re.sub(r'([^\s\w]|_)+', '', stringIn)
        output = ""
        targets = stringIn.split(" ")
        t = 0
        while t < len(targets):
            if targets[t] in dictionary:
                output = output +" "+ dictionary[targets[t]]
            else:
                output = output +" "+ targets[t]
            t = t + 1
        output = output[1:]
    else:
        stringIn = re.sub(r'([^\s\w]|_)+', '', stringIn)
        output = ""
        targets = stringIn.split(" ")
        t = 0
        while t < len(targets):
            lj = targets[t]
            if lj[:1] in "aeiou":
                lj = lj + "way"
            else:
                lj = lj[1:]+lj[:1]+"ay"
            output = output + " " + lj
            t = t + 1
        output = output[1:]
    return output

try:  
    global addAll
    global language
    global dictionary
    if language.lower != "pig latin":
        dictionary = fs.interpret(fs.read("translations/"+getLanguage()+".txt"))
    addAll = getAddAll()
    print dictionary
    while True:
        input = raw_input("Enter a phrase to translate.\n")
        print translate(input)
except:
    raw_input("FATAL ERROR! Press enter to continue...\n")
