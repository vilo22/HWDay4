shopping_bag = {}
print( "\n[1] show items\n" "\n[2] add items\n" "\n[3] remove items\n" "\n[4] quit\n"  )
# set a flag to indicate that polling /shopping cart is active.

polling_active = True #this could be customer_acive = TRue

while polling_active:
    #prompt fo the person's name and response / ask if they want to add something to the bag 
    show_items = '1'
    add_items ='2'
    remove_items ='3'
    quit = '4'

    first_q = input ('\n What would you like to do? ')

    if first_q == "4":
         polling_active = False

    elif first_q == "2":
        add_items = input("What would you like to add? ")
        how_many = input("How many would you like to take? ")

    elif first_q == "3":
        remove_items = input("What would you like to remove ")
    
    elif first_q == "1":
        shopping_bag[first_q.title] = how_many 
        print(add_items + how_many)