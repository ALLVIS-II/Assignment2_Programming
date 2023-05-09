import File.list_function as list_function, inventory_list
    
#main menu
def display_main_menu():
    print(f"1. purchase item")
    print(f"2. quit")

    choice = input(f"Enter 1 or 2 to select")
    while choice != "1" and choice != "2":
        print(f"olny accept to type 1-2")
        choice = input(f"_Error_ please selet 1 or 2")
    return choice


#read file
def readFile(filename, inventory_list):
    infile = open("inventory.txt", "r")
    
    line = infile.readline().strip()
    
    while line != "":
        product_detail = line.split(",")
        print(product_detail)
        return line
#The follwing function 

 


def writeFile(filename, inventory_list):
    print("In function write_file(filename, inventory_list)")

def template(inventory_list):
    print("In function template(inventory_list)")

def accept_money(product_price):
    print("In function accept_money(product_price)")
    
def purchase_product(inventory_list):
    print("In function purchase_product(inventory_list)")
    
def main():
    inventory_list = []
    readFile("inventory.txt")
#think()


main()