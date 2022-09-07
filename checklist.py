

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

# Create a class to be able to call the ANSI color codes
class color:
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    yellow = '\033[93m'
    light_purple = "\033[1;35m"


test()


# TODO left off at 4. Writing Helper Functions  @ 'mark_completed'