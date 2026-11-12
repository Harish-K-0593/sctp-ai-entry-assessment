# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

Inventory = []

# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

def addItem(itemName):                                  # Function is defined with one parameter: itemName.
    if itemName in Inventory:                           # Check if the itemName already exists in the Inventory list.
        print(f"{itemName} is already in inventory.")   # If it exists, print a message indicating that the item is already in inventory.
    else:                                               # If the itemName does not exist in the Inventory list, proceed to add it.
        Inventory.append(itemName)                      # Add the itemName to the Inventory list.

# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

def listInventory():                                    # Function is defined without parameters.
    if not Inventory:                                   # Check if the Inventory list is empty.
        print(f"Inventory is empty.")                   # If it is empty, print a message indicating that the inventory is empty.
    else:
        print(f"Inventory: {Inventory}")                # If the Inventory list is not empty, print the list of items in the inventory.

# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()                                         

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
