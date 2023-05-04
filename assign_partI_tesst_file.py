#import list_function
#import inventory_item
with open("inventory.txt") as file:

def think():
    print(f"1. purchase item")
    print(f"2. quit")

    choice = input(f"Enter 1-2 to select")
    while choice != "1" and choice != "2":
        print(f"olny accept to type 1-2")
        choice = input(f"Enter 1-2 to select ")
    return choice

#def readFile(filename, inventory_list):
#    print("In function read_file(filename, inventory_list)")

#def writeFile(filename, inventory_list):
#    print("In function write_file(filename, inventory_list)")

#def template(inventory_list):
#    print("In function display _vending_machine(inventory_list)")


think()


