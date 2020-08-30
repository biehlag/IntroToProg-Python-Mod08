# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Austin Biehl, 08.29.2020, Added code to assignment 8 starter to create classes
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products'
ProductObjects = []

class Product:

    # Constructor
    def __init__(self, prod_name: str, prod_price: float):
        # Attributes
        self.__product_name = prod_name
        self.__product_price = prod_price
    # Properties
    @property
    def product_name(self):
        return str(self.__product_name).title

    @property
    def product_price(self):
        return float(self.__product)

    # Methods
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.__product_name + ',' + self.__product_price

# End Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name):

        lstProducts = []
        file = open(file_name, "r")
        for line in file:
            line = line.strip()
            fproduct_name,fproduct_price = line.split(",")
            objP = Product(fproduct_name, fproduct_price)
            lstProducts.append(objP)
        file.close()
        return lstProducts, 'Success'

    def write_data_to_file(file_name, lstProducts):

        objFile = open(file_name, "w")
        for row in lstProducts:
          objFile.write(str(row)+'\n')
        objFile.close()
        print('Your data was saved to the file')
        return

    def add_productObject_to_list(newProd_name, newProd_price, lstProducts):

        objP = Product(newProd_name,newProd_price)
        lstProducts.append(objP)
        return lstProducts

# End Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    def __doc__(self):
        return 'The Product class has products and their prices'

    @staticmethod
    def print_menu():

        print('''
            Menu of Options
            1) Add a New Product
            2) Save Product List changes to file
            3) Reload Product List from file        
            4) Exit Program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():

        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def new_product_info():

        NewProd_Name = str(input('What product would you like to add?: '))
        NewProd_Price = str(input('What price do you want to assign it?: '))
        return NewProd_Name, NewProd_Price

# End Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
#
# Load data from file into a list of the products when the script starts #
print('This is the docstring for Products')
print(Product.__doc__)
booContinue = True
prod_name = ''
prod_price = ''
print("Here are your stored items:")
ProductObjects = []
ProductObjects, strStatus = FileProcessor.read_data_from_file(strFileName)
for x in range(len(ProductObjects)):
    print (ProductObjects[x])

# Show the menu of options
while (booContinue == True):
    IO.print_menu()
    strChoice = IO.input_menu_choice()
    if strChoice == '1':           # Add product
        prod_name, prod_price = IO.new_product_info()
        ProductObjects = FileProcessor.add_productObject_to_list(prod_name, prod_price, ProductObjects)
        print('The new product list is:')
        for x in range(len(ProductObjects)):
            print(ProductObjects[x])
    elif strChoice == '2':         # Save to file
        FileProcessor.write_data_to_file(strFileName, ProductObjects)
    elif strChoice == '3':           # User wants to add a product
        ProductObjects = []
        ProductObjects, strStatus = FileProcessor.read_data_from_file(strFileName)
        print('The current products in your list are:')
        for x in range(len(ProductObjects)):
            print(ProductObjects[x])
    elif strChoice == '4':
        print('Have a nice day!')
        booContinue = False
# Main Body of Script  ---------------------------------------------------- #