'''Level 1 Task 30 - Capstone Project 4 - Object Oriented Programming
Create a programe that does the following for the Nike warehouse stock taking list:
Search products by code.
Determine the product with the lowest quantity and restock it.
Determine the product with the highest quantity.
Calculate the value of each item entry, based on the quantity and cost of the
item. The value is calculated by multiplying the cost by the quantity for each
item entered.
'''
# Create Shoe class
class Shoes(object):

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # create method to return cost
    def get_cost(self):
        self.cost
    # create method to return quantity
    def get_quanty(self):
        self.quantity 
    # create method to return class attributes
    # as a string
    def __str__(self):
        return f'country= {self.country}, code= {self.code}, product = {self.product}, cost= {self.cost}, quantity= {self.quantity}'

# create lists for cost and quantity to determine value
cost_list =[]
quantity_list = []
# read data from inventory file and 
# append the cost and quantity list
with open('inventory.txt', 'r', encoding ='utf-8-sig') as f:
    for i, line in enumerate (f):
        if i > 0:
            cost = line.strip('\n').split(',')[3]
            quantity = line.strip('\n').split(',')[4]
            cost_list.append((cost))
            quantity_list.append((quantity))
 
    # change from string to integer  
    cost_list = [int(i) for i in cost_list]
    quantity_list = [int(i) for i in quantity_list]
       
# Create a shoe list
shoes = []
# Create a function to read shoe data
# and create Shoe objects saved in the shoes list
# Allow for scenario if file does not exist
def read_shoes_data():
    file = None
    try:
        file = open('inventory.txt', 'r', encoding ='utf-8-sig')
        for i, line in enumerate(file):
            if i > 0:
                data = line.strip('\n').split(',')
                country = data[0]
                code = data[1]
                product = data[2]
                cost = int(data[3])
                quantity = int(data[4])

                shoe = Shoes(country, code, product, cost, quantity)
                shoes.append(shoe)
        print(shoes)
           
    except FileNotFoundError:
        print("The file you are trying to open does not exist")   
    finally:
        if file is not None:
            file.close()
# Create a function to capture new shoes
# addpend the shoe, cost and quantity lists
def capture_shoes():
    country = input("Enter country name: "). capitalize()
    code = input("Enter product code: ").upper()
    product = input("Enter product name: ").capitalize()
    cost = int(input("Enter product cost: "))
    quantity = int(input("Enter product quantity: "))
    shoe_info = Shoes(country, code, product, cost, quantity)
    shoes.append(shoe_info)
    cost_list.append(shoe_info.cost)
    quantity_list.append(shoe_info.quantity)
    # Display the shoes list
    print(shoes)

# Create a function to view 
# all shoes in the shoes list     
def view_all():
    for shoe in shoes:
        print(shoe.__str__())
             
# Create a function that  allows a user 
# to restock shoes with lowest quantity
def re_stock():
    for shoe, quantity in zip(shoes, quantity_list):
        if quantity == min(quantity_list):
            print(shoe)  
            add_stock = input("Do you want to restock this shoe? (yes or no): ").lower()
            if add_stock == 'yes':
                search_text = 'Vietnam,SKU95000,Air Mag,2000,2'
                quantity =(input("Enter new quantity: "))
                replace_text = 'Vietnam,SKU95000,Air Mag,2000,'+ quantity
                with open(r'inventory.txt', 'r') as f:
                    data = f.read()
                    data = data.replace(search_text, replace_text)
                with open(r'inventory.txt', 'w') as f:   
                    f.write(data)
                            
        else:
            pass 

# Create a function that  allows 
# a user to search for a shoe   
def search_shoe():
    code = input("Enter shoe code: ").upper()
    for shoe in shoes:
        if code == shoe.code:
            find_shoe = print(shoe)
            return find_shoe
       
# Create a function that shows the value of a shoes
# value = cost * quantity        
def value_per_item():
    # create empty list called shoe_value
    shoe_value = []
    # calculate value
    for cost, quantity in zip(cost_list, quantity_list):
        shoe_value.append(cost*quantity)
    
    # combine shoe object with value     
    result = {shoe.product.__str__(): value for shoe, value in zip(shoes, shoe_value)} #zip function: Geeksforgeeks.org
    print (result)
    
# Create a function that shows the shoe
# with the highest quantity       
def highest_qty():
    for shoe, quantity in zip(shoes, quantity_list):
        if quantity == max(quantity_list):
            print(shoe.product) 
    
    print("This shoe is for sale")        

# Use logic to call all functions created
# create a menu called user_choice
user_choice = ""

while user_choice != "quit":
    user_choice = input('''What would you like to do - 
    rd - read shoe data
    cs - capture shoes
    va - view all shoes
    rs - restock shoes
    ss - search for shoes
    vi - get value per item
    hq - get highest quantity
    quit -  exit the program \n''').lower()

    if user_choice == "rd":
        read_shoes_data()
        
    elif user_choice == "cs":
        capture_shoes()
  
    elif user_choice == "va":
        view_all()

    elif user_choice == "rs":
        re_stock()

    elif user_choice == "ss":
        search_shoe()

    elif user_choice == "vi":
        value_per_item()

    elif user_choice == "hq":
        highest_qty()

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
