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
product_line.display()

#------------------

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
        break
        
def AddProd():
    print("Adding product...")
    
def RemoveProd():
    print("Removing product...")
    
def UpdateProd():
    print("Updating product...")
    
def DisplayProd():
    print("Displaying all products...")