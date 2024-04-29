class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ProductLine:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Create a product line linked list
product_line = ProductLine()

# Append products to the product line
product_line.append({"name": "Product 1", "price": 10})
product_line.append({"name": "Product 2", "price": 20})
product_line.append({"name": "Product 3", "price": 30})

# Display the product line

#------------------

def AddProd():
    print("Adding product...")
    
def RemoveProd():
    print("Removing product...")
    
def UpdateProd():
    print("Updating product...")
    
def DisplayProd():
    print("Displaying all products...")
    product_line.display()

runIMS = False
runEcom = False

userAuthenticate = str(input("Owner or Customer? (O/C)"))
userAuthenticate = userAuthenticate.lower()
if userAuthenticate == "o":
    authCode = ""
    userCode = str(input("Enter password: "))
    if authCode == userCode:
        runIMS = True 
        
if userAuthenticate == "c":
    runEcom = True

if runIMS == True or runEcom == True:
    isRun = True
    while isRun == True:
        userInput = None
        print("----------------------------------------")
        
        if runIMS == True:
            print("Grace Corp IMS || V1.0")
            
        if runEcom == True:
            print("Grace Corp eCommerce || V1.0")    
            
        print("Type 'help' for a full list of commands")
        print("")

        userInput = str(input(""))
        userInput = userInput.lower() #Makes lowercase
        
        print("")
    
        if userInput == "help" or userInput == "Help":
            print("Command list")
            print("")
            
            if runIMS == True:
                print("IMS specific")
                print("add || Add a new product")
                print("remove || Remove a product")
                print("update || Update a specific product")
                print("")
                
            if runEcom == True:
                print("Cart specific")
                print("add || Add a product to your cart")
                print("remove || Remove a product from your cart")
                print("undo || Remove a product from your cart")
                print("based on most recently added")
                print("display cart || Display entire inventory")
                print("")
                
            print("General commands")
            print("display || Display entire inventory")
            print("help || this menu")
            print("exit || close application")
        
        if userInput == "add":
            AddProd()
    
        if userInput == "remove":
            RemoveProd()
    
        if userInput == "update":
            UpdateProd()
    
        if userInput == "display":
            DisplayProd()
    
        if userInput == "exit":
            isRun == False
            break