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
    if runIMS == True:
        # Get the ID of the product to remove
        product_id = int(input("Please enter product ID to remove: "))
        current_product = productLine.head
        prev_product = None
        current_cart = cart.head
        prev_cart = None

        # Traverse the product line to find the product with the given ID
        while current_product:
            if current_product.data.get("id") == product_id:
                if prev_product:  # If the node to remove is not the head
                    prev_product.next = current_product.next
                else:  # If the node to remove is the head
                    productLine.head = current_product.next
                print("Product removed from the product line.")
                break
            prev_product = current_product
            current_product = current_product.next

        # Traverse the cart to find the product with the given ID
        while current_cart:
            if current_cart.data.get("id") == product_id:
                if prev_cart:  # If the node to remove is not the head
                    prev_cart.next = current_cart.next
                else:  # If the node to remove is the head
                    cart.head = current_cart.next
                print("Product removed from the cart.")
                break
            prev_cart = current_cart
            current_cart = current_cart.next

        # If the product with the given ID is not found in either the product line or the cart
        if not current_product:
            print("Product not found in the product line.")
        if not current_cart:
            print("Product not found in the cart.")

    if runEcom == True:
        # Get the ID of the product to remove from the cart
        product_id = int(input("Please enter product ID to remove from the cart: "))
        current = cart.head
        prev = None

        # Traverse the cart to find the product with the given ID
        while current:
            if current.data.get("id") == product_id:
                if prev:  # If the node to remove is not the head
                    prev.next = current.next
                else:  # If the node to remove is the head
                    cart.head = current.next
                print("Product removed from the cart.")
                return
            prev = current
            current = current.next

        # If the product with the given ID is not found in the cart
        print("Product not found in the cart.")

# Single-purpose commands
def UpdateItem():
    if runIMS == True:
        # Get the ID of the product to update
        product_id = int(input("Please enter the ID of the product to update: "))
        current_product = productLine.head

        # Traverse the product line to find the product with the given ID
        while current_product:
            if current_product.data.get("id") == product_id:
                # Display the current details of the product
                print("Current details of the product with ID {}: {}".format(product_id, current_product.data))
                
                # Allow the user to update the fields other than the ID
                prodName = str(input("Enter updated product name: "))
                prodPrice = None
                while prodPrice == None:
                    try:
                        prodPrice = float(input("Enter updated product price: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        prodPrice = None

                # Update the fields of the product
                current_product.data["name"] = prodName
                current_product.data["price"] = prodPrice
                print("Product updated successfully.")

                # Update the corresponding entry in the cart if it exists
                current_cart = cart.head
                while current_cart:
                    if current_cart.data.get("id") == product_id:
                        current_cart.data["name"] = prodName
                        current_cart.data["price"] = prodPrice
                        print("Corresponding entry in the cart updated successfully.")
                        break
                    current_cart = current_cart.next
                return

            current_product = current_product.next

        # If the product with the given ID is not found in the product line
        print("Product not found in the product line.")

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