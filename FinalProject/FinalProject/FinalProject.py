isRun = True
while isRun == True:
    userInput = None
    print("Product name || V1.0")
    print("Type 'help' for a full list of commands")
    userInput = str(input(""))
    if userInput == "help" or userInput == "Help":
        print("Command list")
        print("add || Add a new product")
        print("remove || Remove a product")
        print("update || Update a specific product")
        print("display || Display entire inventory")
        print("help || this menu")
        print("exit || close application")
    if userInput == "exit" or userInput == "Exit":
        isRun == False
        
def AddProd():
    print("Adding product...")
    
def RemoveProd():
    print("Removing product...")
    
def UpdateProd():
    print("Updating product...")
    
def DisplayProd():
    print("Displaying all products...")