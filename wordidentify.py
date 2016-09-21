def check(input):
    output = "Other/Error"
    if input.isalpha():
        output = "error"
        if len(input) == 1:
            output = "letter"
        else:
            output = "word"
    else:
        try:
            int(input)
            output = "interger"
        except:
            try:
                float(input)
                output = "float"
            except:
                "other"
    return output
while True:
    print "Type: "+check(raw_input("Please enter something.\n"))
