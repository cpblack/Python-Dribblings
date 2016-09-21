import fs
import re
dictionary = fs.interpret(fs.read("translations.txt"))
print dictionary

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
input = raw_input()
print translate(input)
