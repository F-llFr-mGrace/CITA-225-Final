"""
CITA 225
Deliverable 1
Final Project
Comments provided by ChatGPT
"""

class Product:
    """
    Product class represents individual products with attributes like productId, name, price, and quantity.
    """
    def __init__(self, productId, name, price, quantity):
        self.productId = productId
        self.name = name
        self.price = price
        self.quantity = quantity


class InventoryManagementSystem:
    """
    InventoryManagementSystem class manages products and provides functionalities like adding, removing,
    updating quantities, displaying inventory, and managing a cart.
    """
    def __init__(self):
        self.products = []       # List to store products
        self.productDict = {}    # Dictionary to store products by productId
        self.cart = ProductLine() # Linked list to manage cart
        self.undoStack = []       # Stack to manage undo functionality

    def add_product(self, product):
        """
        Add a new product to the inventory.
        """
        self.products.append(product)
        self.productDict[product.productId] = product
        self.cart.append(product)

    def remove_product(self, productId):
        """
        Remove a product from the inventory by productId.
        """
        for index, product in enumerate(self.products):
            if product.productId == productId:
                self.undoStack.append(product)
                del self.products[index]
                del self.productDict[productId]
                break

    def update_product_quantity(self, productId, new_quantity):
        """
        Update the quantity of a product in the inventory.
        """
        if productId in self.productDict:
            self.productDict[productId].quantity = new_quantity

    def display_inventory(self):
        """
        Display all products in the inventory.
        """
        print("Inventory:")
        for product in self.products:
            print(f"Product ID: {product.productId}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def add_to_cart(self, product):
        """
        Add a product to the cart.
        """
        pass  # Implement linked list for cart and add product node

    def remove_from_cart(self):
        """
        Remove a product from the cart.
        """
        pass  # Implement removal from linked list and push to stack

    def undo_remove_from_cart(self):
        """
        Undo the last remove operation from the cart.
        """
        pass  # Implement pop from stack and add back to cart

    def display_cart(self):
        """
        Display products in the cart.
        """
        pass  # Implement traversal of linked list and display products


class Node:
    """
    Node class represents individual nodes for a linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class ProductLine:
    """
    ProductLine class manages a linked list of products.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a new node to the end of the linked list.
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
        """
        Display all nodes in the linked list.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next


def CLI():
    """
    Command Line Interface to interact with the InventoryManagementSystem.
    """
    ims = InventoryManagementSystem()

    isRun = True
    while isRun:
        print("\nProduct Manager || V1.0")
        print("Type 'help' for a full list of commands")
        userInput = str(input(""))

        if userInput.lower() == "help":
            print("Command list:")
            print("add || Add a new product")
            print("remove || Remove a product")
            print("update || Update a specific product price")
            print("display || Display entire inventory")
            print("help || this menu")
            print("exit || close application")

        elif userInput.lower() == "add":
            productName = input("Enter product name: ")
            productPrice = float(input("Enter product price: "))
            product = Product(productName, productPrice)
            ims.add_product(product)
            print(f"{productName} added to inventory.")

        elif userInput.lower() == "remove":
            productName = input("Enter product name to remove: ")
            ims.remove_product(productName)
            print(f"{productName} removed from inventory.")

        elif userInput.lower() == "update":
            productName = input("Enter product name to update: ")
            newPrice = float(input("Enter new price: "))
            ims.update_product(productName, newPrice)
            print(f"{productName} price updated.")

        elif userInput.lower() == "display":
            ims.display_inventory()

        elif userInput.lower() == "exit":
            isRun = False
            print("Exiting application...")
            break


if __name__ == "__main__":
    CLI()
