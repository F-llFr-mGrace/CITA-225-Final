import decimal
from math import prod


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ProductLine:
    def __init__(self):
        self.head = None
        self.productIdCounter = 1  # Initialize a counter for unique product IDs

    def append(self, productData):
        # Add a unique product ID to the product data
        productData['id'] = self.productIdCounter
        self.productIdCounter += 1
        
        new_node = Node(productData)
        if not self.head:
            self.head = new_node
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

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

# Append products to the product line with unique product IDs
productLine.append({"id": 1, "name": "Product A", "price": float(10)})
productLine.append({"id": 2, "name": "Product B", "price": float(20)})
productLine.append({"id": 3, "name": "Product C", "price": float(30)})

# Create a shopping cart linked list
cart = Cart()

#------------------

# Multi-purpose commands
def AddItem():
    if runIMS == True:
        prodName = str(input("Enter product name: "))
        
        prodPrice = None
        while prodPrice == None:
            try:
                prodPrice = float(input("Enter a product price: "))
                print("Input is a float:", prodPrice)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                prodPrice = None
        
        if prodName != "" and prodPrice != None:
            productLine.append({"id": 1, "name": prodName, "price": prodPrice})

    if runEcom == True:
        product_id = int(input("Please enter product ID: "))  # Ask for the product ID
        current = productLine.head
        while current:
            if current.data.get("id") == product_id:  # Check if the current product has the matching ID
                cart.append(current.data)  # Append the product to the cart
                print("Product added to cart.")
                return
            current = current.next
        print("Product not found in the product line.")  # If product ID doesn't match any product

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
authCode = ""

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

        if userInput == "help":
            print("Command list")
            print("")

            if runIMS == True:
                print("IMS specific")
                print("add || Add a new product by ID")
                print("remove || Remove a product")
                print("update || Update a specific product")
                print("")

            if runEcom == True:
                print("Cart specific")
                print("add || Add a product to your cart by ID")
                print("remove || Remove a product from your cart")
                print("undo || Remove a product from your cart based on most recently added")
                print("cart || Display entire inventory")
                print("")

            print("General commands")
            print("display || Display entire inventory")
            print("help || This menu")
            print("logout || change user")
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
            
        if userInput == "logout":
            userAuthenticate = str(input("Owner or Customer? (O/C)"))
            userAuthenticate = userAuthenticate.lower()
            if userAuthenticate == "o":
                userCode = str(input("Enter password: "))
                if authCode == userCode:
                    runIMS = True
                    runEcom = False
                else:
                    runEcom = True
                    runIMS = False
                    print("Wrong password, returning to eCommerce")
            elif userAuthenticate == "c":  # Changed from if to elif
                runEcom = True
                runIMS = False
            else:
                runIMS = False
                runEcom = False

        if userInput == "exit":
            isRun == False
            break