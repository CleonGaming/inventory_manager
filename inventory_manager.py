import mysql.connector  # type: ignore
import os

# Utility function to clear the screen for a better output
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Connect to the MySQL database
try:
    db = mysql.connector.connect(
        host="localhost", 
        user="Cleo", 
        password="forbot101", 
        database="ims"
    )
    mycursor = db.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Admin Startup Menu
def admin_startup():
    """Displays the admin interface and handles admin actions."""

    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

    print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
    print("◄ Welcome To Inventory Management System *Admin Mode ►")
    print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n")
    option = input(
        """➤Enter The Action You Want To Perform:
      1. Add new item
      2. Update item
      3. Delete item
      4. Search for an item
      5. Update item quantity
      6. View inventory
      7. Generate reports
      8. View by category
      9. Sort inventory 
      10. Exit 
      ┈➤ """
    )
    print()

    # Redirects To Respective Functions (8)
    if option == "1":
        add_item()  
    elif option == "2":
        update_item()  
    elif option == "3":
        delete_item() 
    elif option == "4":
        search_item(0)
    elif option == "5":
        update_quantity(0)
    elif option == "6":
        view_inventory(0)
    elif option == "7":
        generate_reports(0)
    elif option == "8":
        view_by_category(0)
    elif option == "9":
        sort_inventory(0)
    elif option == "10":
        exit()
    else:
        print("╰┈➤ Invalid Input")
        input("Hit Enter To Continue")
        admin_startup()

# User Startup Menu
def user_startup():
    """Displays the user interface and handles user actions."""

    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

    print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
    print(" 「 ✦ Welcome To Inventory Management System ✦ 」")
    print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n")
    option = input(
        """➤Enter The Action You Want To Perform:
      1. Search for an item
      2. Update item quantity
      3. View inventory
      4. Generate reports
      5. View by category
      6. Sort inventory
      7. Enter Admin Mode
      8. Exit 
      ┈➤ """
    )
    print()

    # Redirects To Respective Functions (6)
    if option == "1":
        search_item(1)
    elif option == "2":
        update_quantity(1)
    elif option == "3":
        view_inventory(1)
    elif option == "4":
        generate_reports(1)
    elif option == "5":
        view_by_category(1)
    elif option == "6":
        sort_inventory(1)
    elif option == "7":
        auth()  
    elif option == "8":
        exit()
    else:
        print("╰┈➤ Invalid Input")
        input("Hit Enter To Continue")
        user_startup()

# Authentication for Admin Mode
def auth():
    """Authenticates the user to enter admin mode."""

    name = "admin"
    passwd = "root"

    usr_name = input("ENTER NAME: ")
    usr_passwd = input("ENTER PASSWORD: ")

    # Matching credentials using a guard clause
    if usr_name != name or usr_passwd != passwd:
        print("WRONG CREDENTIALS")
        input("Hit Enter To Continue")
        user_startup()

    admin_startup()

# Add Item Function
def add_item():
    """Adds a new item to the inventory."""

    # Gathering Details
    usr_item = input("Enter Item ➤ ")
    usr_price = float(input("Enter Price ➤ "))
    usr_stock = int(input("Enter Stock ➤ "))
    usr_category = input(
        "\n('Computers','Laptops','Desktops','All-in-One PCs','Computer Accessories','Monitors','Keyboards','Mice','Headsets','Speakers','Webcams','Printers','Scanners','Projectors','Storage Devices','Networking','Office Electronics','Copiers','Fax Machines','Calculators','Office Supplies','Paper','Pens','Binders','Stationery','Furniture','Chairs','Desks','Cabinets','Misc')\n\n\n➤ "
    )

    # Preparing the query
    query = "INSERT INTO inventory (Item, Price, Stock, Category) VALUES (%s, %s, %s, %s)"
    values = (usr_item, usr_price, usr_stock, usr_category)
    
    # Executing & Commiting query
    try:
        mycursor.execute(query,values)
        db.commit()
        print("EXECUTED!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    input("Hit Enter To Continue")
    admin_startup()

# Update Item Function
def update_item():
    """Function for updating Name, Price, Stock or Category of an item."""

    option1 = input("Update Name, Price, Stock or Category? ")

    # Checking user option

    if option1.strip().lower() == "name":

        # Asking for name changes
        usr_id = int(input("Enter Id "))
        new_name = input("Enter Name ")
        query = "UPDATE inventory SET Item = %s WHERE Id = %s"
        values = (new_name, usr_id)
        
    elif option1.strip().lower() == "price":

        # Asking for price changes
        usr_id = int(input("Enter Id "))
        new_price = float(input("Enter Price "))
        query = "UPDATE inventory SET Price = %s WHERE Id = %s"
        values = (new_price, usr_id)

    elif option1.strip().lower() == "stock":

        # Asking for stock changes
        usr_id = int(input("Enter Id "))
        new_stock = int(input("Enter Stock "))
        query = "UPDATE inventory SET Stock = %s WHERE Id = %s"
        values = (new_stock, usr_id)

    elif option1.strip().lower() == "category":

        # Asking for category changes
        usr_id = int(input("Enter Id "))
        new_category = int(input("Enter Category "))
        query = "UPDATE inventory SET Category = %s WHERE Id = %s"
        values = (new_category, usr_id) 

    # Executing & Commiting query
    try:
        mycursor.execute(query,values)
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    input("Hit Enter To Continue")
    admin_startup()

# Delete Item Function
def delete_item():
    """Function for deleting an item by Id."""

    usr_id = int(input("Enter Id "))

    # Showing item
    query = "SELECT * FROM inventory WHERE Id = %s "
    values = (usr_id,)
    mycursor.execute(query,values)
    
    print("-" * 70)
    print(f"{'ID':<5} {'Item':<25} {'Price':<10} {'Stock':^10} {'Category':<15}")
    print("-" * 70)
    
    for i in mycursor:
        print(i)

    confirmation = input("Delete Y/N?")

    if confirmation.strip().lower() == "n" or confirmation.strip().lower() != "y":
        return None

    # Changing query
    query = "DELETE FROM inventory WHERE Id = %s"
    values = (usr_id,)

    # Executing & Commiting query
    try:
        mycursor.execute(query,values)
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    input("Hit Enter To Continue")
    admin_startup()

# Search Item Function
def search_item(mode):
    """Function for searching for an item by name or id."""

    option = input("Search By Name or Id ")

    # Setting query according to user selection
    if option.strip().lower() == "id":
        usr_input = int(input("Enter Id: "))
        query = "SELECT * FROM inventory WHERE Id = %s"
        values = (usr_input,)

    elif option.strip().lower() == "name":
        usr_input = input("Enter Item Name: ")
        query = "SELECT * FROM inventory WHERE Item LIKE %s"
        values = ('%' + usr_input + '%',)

    else:
        print("Invalid Input")
        input("Hit Enter To Continue")
        if mode == 1:
            user_startup()
        else:
            admin_startup()

    # Executing query
    try:
        mycursor.execute(query,values)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    # Showing Results
    print("-" * 70)
    print(f"{'ID':<5} {'Item':<25} {'Price':<10} {'Stock':^10} {'Category':<15}")
    for i in mycursor:
        id, name, price, stock, category = i
        dash = len(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")
        print("-" * 70)
        print(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")

    print("-" * 70)
    input("Hit Enter To Continue")
    if mode == 1:
        user_startup()
    else:
        admin_startup()

# Update Item Function
def update_quantity(mode):
    """Function for updating item quantity/stock."""

    option1 = input("Update By Id or Name ")

    # Setting query according to user selection
    if option1.strip().lower() == "id":
        usr_id = int(input("Enter Id "))
        new_stock = int(input("Enter Stock "))
        query = "UPDATE inventory SET Stock = %s WHERE Id = %s"
        values = (new_stock, usr_id)


    elif option1.strip().lower() == "name":
        usr_name = int(input("Enter Name "))
        new_stock = int(input("Enter Stock "))
        query = "UPDATE inventory SET Stock = %s WHERE Item LIKE %s"
        values = (new_stock, '%' + usr_name + '%')

    # Executing & Commiting query
    try:
        mycursor.execute(query,values)
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    input("Hit Enter To Continue")
    if mode == 1:
        user_startup()
    else:
        admin_startup()

# View Inventory Function
def view_inventory(mode):
    """Function to view the entire inventory"""

    query = "SELECT * FROM inventory"
    mycursor.execute(query)

    # Showing Results
    print("-" * 70)
    print(f"{'ID':<5} {'Item':<25} {'Price':<10} {'Stock':^10} {'Category':<15}")
    
    for i in mycursor:
        id, name, price, stock, category = i
        dash = len(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")
        print("-" * 70)
        print(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")

    print("-" * 70)
    input("Hit Enter To Continue")
    if mode == 1:
        user_startup()
    else:
        admin_startup()

# Generate Reports Function
def generate_reports(mode):
    """Function to generate entire inventory into .txt file """

    # Obtaining inventory
    query = "SELECT * FROM inventory"
    mycursor.execute(query)

    # Setting File Path
    file_path = f"{os.getcwd()}/report.txt"

    # Writing Data
    if os.path.exists(file_path):

        with open(r"" + file_path, "a") as f:

            f.writelines("*" * 10 + "\n")

            for i in mycursor:
                f.writelines(str(i) + "\n")
            f.writelines("*" * 10 + "\n")

    else:

        with open(r"" + file_path, "w") as f:

            f.writelines("*" * 10 + "\n")

            for i in mycursor:
                f.writelines(str(i) + "\n")
            f.writelines("*" * 10 + "\n")

    input("Hit Enter To Continue")
    if mode == 1:
        user_startup()
    else:
        admin_startup()

# View By Category Function
def view_by_category(mode):
    """Function to view inventory items filtered by category"""
    
    print("\nAvailable Categories:")
    # Get unique categories from database
    query = "SELECT DISTINCT Category FROM inventory ORDER BY Category"
    try:
        mycursor.execute(query)
        categories = [category[0] for category in mycursor]
        
        # Display available categories
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
            
        # Get category choice from user
        usr_choice = input("\nEnter Category Name ➤ ")
        
        # Query items in selected category
        query = "SELECT * FROM inventory WHERE Category = %s"
        values = (usr_choice,)
        mycursor.execute(query, values)
        
        # Display results
        items_found = False

        print("-" * 70)
        print(f"{'ID':<5} {'Item':<25} {'Price':<10} {'Stock':^10} {'Category':<15}")
        print("-" * 70)
        
        for i in mycursor:
            items_found = True
            id, name, price, stock, category = i
            print(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")
            
        if not items_found:
            print("No items found in this category!")
        print("-" * 70)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    input("Hit Enter To Continue")
    if mode == 1:
        user_startup()
    else:
        admin_startup()

# Sort Function
def sort_inventory(mode):
    """Function to view inventory sorted by different criteria"""
    
    print("\nSort inventory by:")
    print("1. Name")
    print("2. Price (Low to High)")
    print("3. Price (High to Low)")
    print("4. Quantity (Low to High)")
    print("5. Quantity (High to Low)")
    
    sort_choice = input("\n➤ Enter your choice (1-5): ")
    
    # Define the query based on user's choice
    if sort_choice == "1":
        query = "SELECT * FROM inventory ORDER BY Item"
        sort_by = "Name"
    elif sort_choice == "2":
        query = "SELECT * FROM inventory ORDER BY Price"
        sort_by = "Price (Low to High)"
    elif sort_choice == "3":
        query = "SELECT * FROM inventory ORDER BY Price DESC"
        sort_by = "Price (High to Low)"
    elif sort_choice == "4":
        query = "SELECT * FROM inventory ORDER BY Stock"
        sort_by = "Quantity (Low to High)"
    elif sort_choice == "5":
        query = "SELECT * FROM inventory ORDER BY Stock DESC"
        sort_by = "Quantity (High to Low)"
    else:
        print("Invalid choice!")
        input("Hit Enter To Continue")
        if mode == 1:
            user_startup()
        else:
            admin_startup()
        return
    
    try:
        # Execute the query
        mycursor.execute(query)
        
        # Display results
        print(f"\nInventory Sorted by: {sort_by}")
        print("-" * 70)
        print(f"{'ID':<5} {'Item':<25} {'Price':<10} {'Stock':^10} {'Category':<15}")
        print("-" * 70)
        
        for i in mycursor:
            id, name, price, stock, category = i
            print(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")
            
        print("-" * 70)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    input("Hit Enter To Continue")
    if mode == 1:
        user_startup()
    else:
        admin_startup()

def exit():
    """
    Function to show end screen
    """
    print("\n\n╭┈┈┈┈┈┈┈┈┈┈┈┈┈╮")
    print("   Thank You")
    print("╰┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
    return None

if __name__ == "__main__":
    user_startup()