

checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    # Check that the index is within the range of the list
    if index < len(checklist):
        return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        text = (f"{index} {list_item}")
        # The items are listed by color and type "purple sock"
        # If we split the item string into a list of it's two components, we
        # can check for the color in the list, then set the color property to that color
        # so that the item will be printed to the terminal in it's color.
        if 'red' in list_item.split(" "):
            print(color.red, text)
        elif 'orange' in list_item.split(" "):
            print(color.orange, text)
        elif 'yellow' in list_item.split(" "):
            print(color.yellow, text)
        elif 'green' in list_item.split(" "):
            print(color.green, text)
        elif 'blue' in list_item.split(" "):
            print(color.blue, text)
        elif 'purple' in list_item.split(" "):
            print(color.purple, text)
        else:
            print(color.light_purple, text)
            
        index += 1

# Create a class to be able to call the ANSI color codes
class color:
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    yellow = '\033[93m'
    light_purple = "\033[1;35m"
    
# Mark an item as completed by adding '√' to the beginning of the 'item' string then updating the checklist list with this new string
def mark_completed(index):
    checked_item = "√" + checklist[index] 
    update(index, checked_item)

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):

    if function_code == "A":
        #Create item in checklist
        create(user_input("Add to list: "))

    elif function_code == "R":
        # Remove item from checklist
        destroy(int(user_input("Which item to delete? ")))

    elif function_code == "U":
        index_to_update = int(user_input("Which item to update? "))
        updated_item = user_input("What would you like to change it to? ")
        update(index_to_update, updated_item)

    elif function_code == "C":
        mark_completed(int(user_input("Which item would you like to mark as completed? ")))

    elif function_code == "P":
        # Print all items 
        list_all_items()

    elif function_code == "Q":
        # If the user chooses 'Q', 'False' will be returned, stopping the loop
        return False
    else:
        #Catch all
        print("Unknown Option")
    return True

# Testing code
def test():
    create("purple sox")
    create("red cloak")
    create("yellow shoe")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    # destroy(1)

    print(read(0))
    print(read(1))

    list_all_items()
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

    user_value = user_input("Please Enter a value:")
    print(user_value)


test()


running = True
while running:
    selection = user_input(
        "Press A to add to list, R to remove, U to update item, C to mark as completed, P to show list, and Q to quit: ")
    running = select(selection)

# TODO start at "Finish things up"