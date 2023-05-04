def template(invenory_list):
    counter = 1
    print(" ", " "*50, sep="")
    print("|", ""*50, "I", sep="")
    print("|", format("*** ACME Vending Machine ***", "*50s"), "|", sep="")
    print("|", ""*50, "I", sep="")
    print("|", ""*50, "I", sep="")
    for product in invenory_list:
        name = product.get_product_name()
        prize = "$.2f" % (product.get_product_prize())
        print("| ", format(counter, ">2d"), ", ", format(product.get_product_name(), ""))
        print("")