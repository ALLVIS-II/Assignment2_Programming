    
#main menu
def display_main_menu():
    print(f"\n1. purchase item")
    print(f"2. quit")

    choice = input(f"Enter 1 or 2 to select")
    while choice != "1" and choice != "2":
        print(f"olny accept to type 1-2")
        choice = input(f"_Error_ please selet 1 or 2")
    return choice


#read file
def readFile(filename, inventory_list):
    infile = open(filename, "r")
    
    line = infile.readline().strip()
    
    while line != "":
        product_detail = line.split(",")
        name  = product_detail[0]
        price = "{:.2f}".product_detail[1]
        qty = product_detail[2]
        product = inventory_list.InventoryItem(int(name), float(price),int(qty))
        inventory_list.append(product)
        return line
    
    infile.close()
#Implement Function display_vending_machine()
def template(inventory_list):
    print(" ", "_" * 50, sep="")
    print("|", " "*50, "|", sep="")
    print("|", format("*** ACME VENDING MACHINE ***", "^50s"), "|", sep="")
    print("|", "_"*50, "|", sep="")
    print("|", " "*50, "|", sep="")
    
    print("|", "_"*50, "|", sep="")
    print("|", " "*50, "|", sep="")
    print("|", format("\___________________________________/"), "^50s")
    print("|", " "*50, "|", sep="")
    
    item_no = 1
    for product in inventory_list:
        product_name = product.get_product_name()
        product_price = product.get_product_price()
        product_qty = product.get_product_quantity()

        print("|", 
              format(item_no, ">2d"), ". ",
              format(product_name,".<38s"), "$", 
              format(str(product_price), "<6s"),
              "|", sep=""
              
              )
        
        
        item_no+=1


# Implementing Function accept_money()
def accept_money(product_price):
    money = 0
    coinChoice = ['Ten cents', 'Twenty cents', 'Fifty cents','One dollar', 'Cancel']
    userInput = input("Please continue to enter coins until amount reached.")

    if coinChoice[0] == 1:
        return 'Ten Cents' 
    if coinChoice[1] == 2:
        return 'Twenty Cents'
    if coinChoice[2] == 3:
        return 'Fifty cents'
    if coinChoice[3] == 4:
        return 'One dollar'
    else:
        return False
    for coin in coins:
        print(input("Please continue to enter coins until amount reached"))
        print("Valid choices for coins are:")

    
def purchase_product(inventory_list):
    print("In function purchase_product(inventory_list)")
    
def main():
    inventory_list = []
    readFile("inventory.txt", inventory_list)
    choice = display_main_menu()
    print(f"you chose {choice}")
#think()


main()