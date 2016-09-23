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
def translate(stringIn):
    global dictionary
    global addAll
    stringIn = re.sub(r'([^\s\w]|_)+', '', stringIn)
    output = ""
    targets = stringIn.split(" ")
    t = 0
    while t < len(targets):
        if targets[t] in dictionary:
            output = output +" "+ dictionary[targets[t]] + addAll
        else:
            output = output +" "+ targets[t] + addAll
        t = t + 1
    output = output[1:]
    return output
    
global addAll
global dictionary
dictionary = fs.interpret(fs.read("translations/"+getLanguage()+".txt"))
addAll = getAddAll()
print dictionary
input = raw_input("Enter a phrase to translate.\n")
print translate(input)
