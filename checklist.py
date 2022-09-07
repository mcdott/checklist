
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

# Testing code
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

test()


