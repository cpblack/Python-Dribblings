import fs
import re
dictionary = fs.interpret(fs.read("translations/"+getLanguage()+".txt"))
print dictionary


def getLanguage()
    language = "in valid"
    while fs.exists("translations/"+language+".txt") == False:
        language = raw_input("Please enter the name of your language file located in the Translations folder, the name must be alphanumeric.\n")
    return language
def translate(stringIn):
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
    return output
input = raw_input("Enter a phrase to translate.\n")
print translate(input)
