isRun = True
while isRun == True:
    userInput = None
    print("Product name || V1.0")
    print("Type 'help' for a full list of commands")
    userInput = str(input(""))
    if userInput == "help" or userInput == "Help":
        print("Command list")
    if userInput == "exit" or userInput == "Exit":
        isRun == False