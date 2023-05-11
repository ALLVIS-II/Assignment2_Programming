#
#  PSP Assignment 2 - Provided file (Part I - list_function.py).
#  Remove this and place appropriate file comments here.
#
#  Modify this file to include your code solution.
#
#
# Write your function definitions in this file.
# Place your own comments in this file also.
#


# Function size() - place your own comments here...  : )
def size(my_list):

   

    count = 0
    for item in my_list:
        count += 1
    return item


# Function to_string() - place your own comments here...  : )
def to_string(my_list, sep=', '):
    result =''
    for n in range(size(my_list)): 
        result += my_list[n]
        return result
        





# Function add() - place your own comments here... : )
def add(my_list, value):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function add()")

    # Place your code and comments here

    
# Function count() - place your own comments here...  : )
def count(my_list, value):
    
    
    for i in enumerate(size(my_list)):
        if my_list[i] == value:
            count+=1
            if count < 0: return count
            else: return -1
            

    # Place your code and comments here


# Function insert() - place your own comments here...  : )
def insert(my_list, value, position):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function insert()") 
    
    if isinstance(value, str):
        # REMOVE this line and replace with your code
        print("value is a string")
    elif isinstance(value, list):
        # REMOVE this line and replace with your code
        print("value is a list")



# Function remove() - place your own comments here...  : )
def remove(my_list, position):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function remove()")
    

