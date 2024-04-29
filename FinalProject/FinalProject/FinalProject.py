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

# Cart class added here
class Cart:
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
productLine = ProductLine()

# Append products to the product line
productLine.append({"name": "Product 1", "price": 10})
productLine.append({"name": "Product 2", "price": 20})
productLine.append({"name": "Product 3", "price": 30})

# Create a shopping cart linked list
cart = Cart()

# Append products to the shopping cart
cart.append({"name": "Product 1", "price": 10})

# Display the contents of the shopping cart

#------------------

# Multi-purpose commands
def AddItem():
    itemName = str(input("Please enter item name: "))
    itemPrice = str(input("Please enter item price: "))
    print("Adding item...")

def RemoveItem():
    print("Removing item...")

# Single-purpose commands
def UpdateItem():
    print("Updating item...")

def Undo():
    print("Removing most recent addition...")

# General Commands
def DisplayItems(type):
    if type == "c":
        print("Displaying cart...")
        cart.display()

    if type == "d":
        print("Displaying all products...")
        productLine.display()

# Exit executed within the loop

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
        userInput = userInput.lower()  # Makes lowercase

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
                print("cart || Display entire inventory")
                print("")

            print("General commands")
            print("display || Display entire inventory")
            print("help || This menu")
            print("exit || Close application")

        # Multi-purpose commands
        if userInput == "add":
            AddItem()

        if userInput == "remove":
            RemoveItem()

        # Single-purpose commands
        if runIMS == True:
            if userInput == "update":
                UpdateItem()

        if runEcom == True:
            if userInput == "undo":
                break

            if userInput == "cart":
                DisplayItems("c")

        # General Commands
        if userInput == "display":
            DisplayItems("d")

        if userInput == "exit":
            isRun == False
            break
