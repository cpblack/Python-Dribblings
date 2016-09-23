import fs
from re import sub as re.sub

def getLanguage():
    language = "this should not be used as a language name"
    while fs.exists("translations/"+language+".txt") == False:
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
    stringIn = re.sub(r'([^\s\w]|_)+', '', stringIn)
    output = ""
    targets = stringIn.split(" ")
    t = 0
    while t < len(targets):
        if targets[t] in dictionary:
            output = output +" "+ smartAddAll(dictionary[targets[t]], addAll)
        else:
            output = output +" "+ smartAddAll(targets[t],addAll)
        t = t + 1
    output = output[1:]
    return output

try:  
    global addAll
    global dictionary
    dictionary = fs.interpret(fs.read("translations/"+getLanguage()+".txt"))
    addAll = getAddAll()
    print dictionary
    while True:
        input = raw_input("Enter a phrase to translate.\n")
        print translate(input)
except:
    raw_input("FATAL ERROR! Press enter to continue...\n")
