import decimal
from math import prod


class Node:
    """A class to represent a node in a linked list."""
    def __init__(self, data=None):
        """Initialize the node with data."""
        self.data = data
        self.next = None

class ProductLine:
    """A class to represent the product line."""
    def __init__(self):
        """Initialize an empty product line with a product ID counter."""
        self.head = None
        self.productIdCounter = 1  # Initialize a counter for unique product IDs

    def append(self, productData):
        """
        Append a product to the product line.

        Args:
            productData (dict): The data of the product to be appended.
        """
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
        """Display all products in the product line."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

class Cart:
    """A class to represent the shopping cart."""
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.head = None

    def append(self, data):
        """
        Append a product to the shopping cart.

        Args:
            data (dict): The data of the product to be appended.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """Display all products in the shopping cart."""
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

# Create a stack to store the IDs of items added to the cart for undo functionality
stackUndo = []

#------------------

# Multi-purpose commands
def AddItem():
    """
    Add a new product to the product line or the cart.

    If the system is running in IMS mode, the user can add a new product to the product line.
    If the system is running in eCommerce mode, the user can add an existing product from the product line to the cart.
    """
    if runIMS:
        prodName = str(input("Enter product name: "))
        
        prodPrice = None
        while prodPrice == None:
            try:
                prodPrice = float(input("Enter a product price: "))
                print("Input is a float:", prodPrice)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                prodPrice = None
        
        if prodName and prodPrice:
            productLine.append({"id": 1, "name": prodName, "price": prodPrice})

    if runEcom:
        productId = int(input("Please enter product ID: "))  # Ask for the product ID
        current = productLine.head
        while current:
            if current.data.get("id") == productId:  # Check if the current product has the matching ID
                cart.append(current.data)  # Append the product to the cart
                print("Product added to cart.")
                return
            current = current.next
        print("Product not found in the product line.")  # If product ID doesn't match any product

def RemoveItem():
    """
    Remove a product from the product line or the cart.

    If the system is running in IMS mode, the user can remove a product from the product line.
    If the system is running in eCommerce mode, the user can remove a product from the cart.
    """
    if runIMS:
        # Get the ID of the product to remove
        productId = int(input("Please enter product ID to remove: "))
        currentProduct = productLine.head
        prevProduct = None
        currentCart = cart.head
        prevCart = None

        # Traverse the product line to find the product with the given ID
        while currentProduct:
            if currentProduct.data.get("id") == productId:
                if prevProduct:  # If the node to remove is not the head
                    prevProduct.next = currentProduct.next
                else:  # If the node to remove is the head
                    productLine.head = currentProduct.next
                print("Product removed from the product line.")
                break
            prevProduct = currentProduct
            currentProduct = currentProduct.next

        # Traverse the cart to find the product with the given ID
        while currentCart:
            if currentCart.data.get("id") == productId:
                if prevCart:  # If the node to remove is not the head
                    prevCart.next = currentCart.next
                else:  # If the node to remove is the head
                    cart.head = currentCart.next
                print("Product removed from the cart.")
                break
            prevCart = currentCart
            currentCart = currentCart.next

        # If the product with the given ID is not found in either the product line or the cart
        if not currentProduct:
            print("Product not found in the product line.")
        if not currentCart:
            print("Product not found in the cart.")

    if runEcom:
        # Get the ID of the product to remove from the cart
        productId = int(input("Please enter product ID to remove from the cart: "))
        current = cart.head
        prev = None

        # Traverse the cart to find the product with the given ID
        while current:
            if current.data.get("id") == productId:
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
    """
    Update details of a product in the product line.

    If the system is running in IMS mode, the user can update the name and price of a product in the product line.
    """
    if runIMS:
        # Get the ID of the product to update
        productId = int(input("Please enter the ID of the product to update: "))
        currentProduct = productLine.head

        # Traverse the product line to find the product with the given ID
        while currentProduct:
            if currentProduct.data.get("id") == productId:
                # Display the current details of the product
                print("Current details of the product with ID {}: {}".format(productId, currentProduct.data))
                
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
                currentProduct.data["name"] = prodName
                currentProduct.data["price"] = prodPrice
                print("Product updated successfully.")

                # Update the corresponding entry in the cart if it exists
                currentCart = cart.head
                while currentCart:
                    if currentCart.data.get("id") == productId:
                        currentCart.data["name"] = prodName
                        currentCart.data["price"] = prodPrice
                        print("Corresponding entry in the cart updated successfully.")
                        break
                    currentCart = currentCart.next
                return

            currentProduct = currentProduct.next

        # If the product with the given ID is not found in the product line
        print("Product not found in the product line.")

def Undo():
    """
    Remove the most recently added product from the cart.
    """
    if stackUndo:
        # Get the ID of the most recently added item from the stack
        undo_id = stackUndo.pop()
        
        # Remove the item from the cart
        current = cart.head
        prev = None
        while current:
            if current.data.get("id") == undo_id:
                if prev:  # If the node to remove is not the head
                    prev.next = current.next
                else:  # If the node to remove is the head
                    cart.head = current.next
                print("Most recently added product removed from the cart.")
                return
            prev = current
            current = current.next
    else:
        print("No items to undo.")

# General Commands
def DisplayItems(type):
    """
    Display either the product line or the shopping cart.

    Args:
        type (str): The type of items to display. 'c' for cart, 'd' for product line.
    """
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

if runIMS or runEcom:
    isRun = True
    while isRun:
        userInput = None
        print("----------------------------------------")

        if runIMS:
            print("Grace Corp IMS || V1.0")

        if runEcom:
            print("Grace Corp eCommerce || V1.0")

        print("Type 'help' for a full list of commands")
        print("")

        userInput = str(input(""))
        userInput = userInput.lower()

        print("")

        if userInput == "help":
            print("Command list")
            print("")

            if runIMS:
                print("IMS specific")
                print("add || Add a new product by ID")
                print("remove || Remove a product")
                print("update || Update a specific product")
                print("")

            if runEcom:
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
        if runIMS:
            if userInput == "update":
                UpdateItem()

        if runEcom:
            if userInput == "undo":
                Undo()

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
            elif userAuthenticate == "c":
                runEcom = True
                runIMS = False
            else:
                runIMS = False
                runEcom = False

        if userInput == "exit":
            isRun = False
            break
