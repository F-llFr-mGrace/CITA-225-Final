"""
IMS and eCommerce system by Grace Fowler
CITA 225
Comments and bug-fixing assistance by ChatGPT
"""

import decimal
from math import prod


'''
Defines a class to represent a node in a linked list.
'''
class Node:
    """A class to represent a node in a linked list."""
    def __init__(self, data=None):
        """Initialize the node with data."""
        self.data = data  # Assigns the data to the node
        self.next = None  # Initializes the next pointer to None

'''
Defines a class to represent the product line.
'''
class ProductLine:
    """A class to represent the product line."""
    def __init__(self):
        """Initialize an empty product line with a product ID counter."""
        self.head = None  # Initializes the head of the product line to None
        self.productIdCounter = 1  # Initialize a counter for unique product IDs

    def append(self, productData):
        """
        Append a product to the product line.

        Args:
            productData (dict): The data of the product to be appended.
        """
        # Add a unique product ID to the product data
        productData['id'] = self.productIdCounter  # Assigns a unique ID to the product data
        self.productIdCounter += 1  # Increments the product ID counter
        
        new_node = Node(productData)  # Creates a new node with the product data
        if not self.head:  # If the product line is empty
            self.head = new_node  # Sets the new node as the head
            return
        lastNode = self.head  # Initializes a pointer to traverse the product line
        while lastNode.next:  # Traverses to the last node in the product line
            lastNode = lastNode.next
        lastNode.next = new_node  # Appends the new node to the end of the product line

    def display(self):
        """Display all products in the product line."""
        current = self.head  # Initializes a pointer to traverse the product line
        while current:  # Iterates through the product line
            print(current.data)  # Prints the data of the current node
            current = current.next  # Moves to the next node in the product line

'''
Defines a class to represent the shopping cart.
'''
class Cart:
    """A class to represent the shopping cart."""
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.head = None  # Initializes the head of the shopping cart to None

    def append(self, data):
        """
        Append a product to the shopping cart.

        Args:
            data (dict): The data of the product to be appended.
        """
        new_node = Node(data)  # Creates a new node with the product data
        if not self.head:  # If the shopping cart is empty
            self.head = new_node  # Sets the new node as the head
            return
        last_node = self.head  # Initializes a pointer to traverse the shopping cart
        while last_node.next:  # Traverses to the last node in the shopping cart
            last_node = last_node.next
        last_node.next = new_node  # Appends the new node to the end of the shopping cart

    def display(self):
        """Display all products in the shopping cart."""
        current = self.head  # Initializes a pointer to traverse the shopping cart
        while current:  # Iterates through the shopping cart
            print(current.data)  # Prints the data of the current node
            current = current.next  # Moves to the next node in the shopping cart

'''
Creates an instance of the ProductLine class to represent the product line.
'''
productLine = ProductLine()

'''
Appends products to the product line with unique product IDs.
'''
productLine.append({"id": 1, "name": "Product A", "price": float(10)})
productLine.append({"id": 2, "name": "Product B", "price": float(20)})
productLine.append({"id": 3, "name": "Product C", "price": float(30)})

'''
Creates an instance of the Cart class to represent the shopping cart.
'''
cart = Cart()

'''
Creates an empty stack to store the IDs of items added to the cart for undo functionality.
'''
stackUndo = []

#------------------

'''
This function handles the addition of a new product to the product line or the cart.
If the system is running in IMS mode, the user can add a new product to the product line.
If the system is running in eCommerce mode, the user can add an existing product from the product line to the cart.
'''
def AddItem():
    if runIMS:
        '''
        Prompt the user to enter the name and price of the product.
        '''
        prodName = str(input("Enter product name: "))
        
        prodPrice = None
        '''
        Validate the input for the product price.
        '''
        while prodPrice == None:
            try:
                prodPrice = float(input("Enter a product price: "))
                print("Input is a float:", prodPrice)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                prodPrice = None
        
        '''
        If both product name and price are provided, append the product to the product line.
        '''
        if prodName and prodPrice:
            productLine.append({"id": 1, "name": prodName, "price": prodPrice})

    if runEcom:
        '''
        If running in eCommerce mode, prompt the user to enter the product ID.
        '''
        productId = int(input("Please enter product ID: "))  # Ask for the product ID
        current = productLine.head
        '''
        Iterate through the product line to find the product with the matching ID.
        '''
        while current:
            if current.data.get("id") == productId:  # Check if the current product has the matching ID
                '''
                If a product with the given ID is found, append it to the cart.
                '''
                cart.append(current.data)  # Append the product to the cart
                print("Product added to cart.")
                return
            current = current.next
        '''
        If no product with the given ID is found, print a message indicating that.
        '''
        print("Product not found in the product line.")  # If product ID doesn't match any product

'''
This function handles the removal of a product from the product line or the cart.
If the system is running in IMS mode, the user can remove a product from the product line.
If the system is running in eCommerce mode, the user can remove a product from the cart.
'''
def RemoveItem():
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
                # If the node to remove is not the head
                if prevProduct:
                    prevProduct.next = currentProduct.next
                # If the node to remove is the head
                else:
                    productLine.head = currentProduct.next
                print("Product removed from the product line.")
                break
            prevProduct = currentProduct
            currentProduct = currentProduct.next

        # Traverse the cart to find the product with the given ID
        while currentCart:
            if currentCart.data.get("id") == productId:
                # If the node to remove is not the head
                if prevCart:
                    prevCart.next = currentCart.next
                # If the node to remove is the head
                else:
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
                # If the node to remove is not the head
                if prev:
                    prev.next = current.next
                # If the node to remove is the head
                else:
                    cart.head = current.next
                print("Product removed from the cart.")
                return
            prev = current
            current = current.next

        # If the product with the given ID is not found in the cart
        print("Product not found in the cart.")

# Single-purpose commands
'''
This function updates the details of a product in the product line.
If the system is running in IMS mode, the user can update the name and price of a product in the product line.
'''
def UpdateItem():
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

'''
This function removes the most recently added product from the cart if there are items in the undo stack.
'''
def Undo():
    if stackUndo:
        # Get the ID of the most recently added item from the stack
        undo_id = stackUndo.pop()
        
        # Remove the item from the cart
        current = cart.head
        prev = None
        while current:
            if current.data.get("id") == undo_id:
                # If the node to remove is not the head
                if prev:
                    prev.next = current.next
                # If the node to remove is the head
                else:
                    cart.head = current.next
                print("Most recently added product removed from the cart.")
                return
            prev = current
            current = current.next
    else:
        print("No items to undo.")

# General Commands
'''
This function displays either the product line or the shopping cart based on the specified type.
'''
def DisplayItems(type):
    """
    Display either the product line or the shopping cart.

    Args:
        type (str): The type of items to display. 'c' for cart, 'd' for product line.
    """
    if type == "c":
        # Display the shopping cart
        print("Displaying cart...")
        cart.display()

    if type == "d":
        # Display all products in the product line
        print("Displaying all products...")
        productLine.display()

# Initialize variables to control program mode and authentication
runIMS = False
runEcom = False
authCode = ""

# Prompt user to select owner or customer mode
userAuthenticate = str(input("Owner or Customer? (O/C)"))
userAuthenticate = userAuthenticate.lower()

# If owner mode is selected
if userAuthenticate == "o":
    # Ask for authentication code
    authCode = ""
    userCode = str(input("Enter password: "))
    
    # If authentication code matches, switch to IMS mode
    if authCode == userCode:
        runIMS = True

# If customer mode is selected
if userAuthenticate == "c":
    # Switch to eCommerce mode
    runEcom = True

'''
This loop controls the main functionality of the program based on the selected mode (IMS or eCommerce).
'''
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

        # Get user input and convert it to lowercase
        userInput = str(input(""))
        userInput = userInput.lower()

        print("")

        # Display help menu
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
            
        # Log out or change user
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

        # Exit the application
        if userInput == "exit":
            isRun = False
            break
