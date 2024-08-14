import mysql.connector # type: ignore
import os 

#Clearing screen for windows or linux
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

#Connecting to database
try:
  db = mysql.connector.connect(
      host="localhost",
      user="root",
      database="ims"
  )
  mycursor = db.cursor() 

except mysql.connector.Error as err:
  print(f"Error: {err}")


def admin_startup():
  """
  Interface Screen In Terminal For Admin
  """

  if os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")

  print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
  print("◄ Welcome To Inventory Management System *Admin Mode ►")
  print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n")
  option = input("""➤Enter The Action You Want To Perform:
      1. Add new item
      2. Update item
      3. Delete item
      4. Search for an item
      5. Update item quantity
      6. View inventory
      7. Generate reports
      8. Exit 
      ┈➤ """)
  print()

  #Redirects To Respective Functions (8)
  if option == "1":
    add_item()          #EXTRA
  elif option == "2":
    update_item()       #EXTRA
  elif option == "3":
    delete_item()       #EXTRA
  elif option == "4":
    search_item(0)
  elif option == "5":
    update_quantity(0)
  elif option == "6":
    view_inventory(0)
  elif option == "7":
    generate_reports(0)
  elif option == "8":
    exit()
  else:
    print("╰┈➤ Invalid Input")
    input("Hit Enter To Continue")
    admin_startup()

def user_startup():
  """
  Interface Screen In Terminal For Default User
  """

  if os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")

  print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
  print(" 「 ✦ Welcome To Inventory Management System ✦ 」")
  print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n")
  option = input("""➤Enter The Action You Want To Perform:
      1. Search for an item
      2. Update item quantity
      3. View inventory
      4. Generate reports
      5. Enter Admin Mode
      6. Exit 
      ┈➤ """)
  print()

  #Redirects To Respective Functions (6)
  if option == "1":
    search_item(1)
  elif option == "2":
    update_quantity(1)
  elif option == "3":
    view_inventory(1)
  elif option == "4":
    generate_reports(1)
  elif option == "5":
    auth()                #EXTRA
  elif option == "6":
    exit()
  else:
    print("╰┈➤ Invalid Input")
    input("Hit Enter To Continue")
    user_startup()

def auth():
  """
  Authentication for entering admin mode
  """

  name = "admin"
  passwd = "root"

  usr_name = input("ENTER NAME: ")
  usr_passwd = input("ENTER PASSWORD: ")

  #Matching credentials using a guard clause
  if usr_name != name or usr_passwd != passwd:
    print("WRONG CREDENTIALS")
    input("Hit Enter To Continue")
    user_startup()

  admin_startup()

def add_item():
  """
  Function for adding an item in admin mode 
  """

  #Gathering Details
  usr_item = input("Enter Item ➤ ")
  usr_price = float(input("Enter Price ➤ "))
  usr_stock = int(input("Enter Stock ➤ "))
  usr_category = input("\n('Computers','Laptops','Desktops','All-in-One PCs','Computer Accessories','Monitors','Keyboards','Mice','Headsets','Speakers','Webcams','Printers','Scanners','Projectors','Storage Devices','Networking','Office Electronics','Copiers','Fax Machines','Calculators','Office Supplies','Paper','Pens','Binders','Stationery','Furniture','Chairs','Desks','Cabinets','Misc')\n\n\n➤ ")

  #Preparing the query
  query = f"INSERT INTO inventory(Item, Price, Stock, Category) VALUES ('{usr_item}', {usr_price}, {usr_stock}, '{usr_category}')"
  
  #Executing & Commiting query 
  try:
    mycursor.execute(query)
    db.commit()
    print("EXECUTED!")
  except mysql.connector.Error as err:
    print(f"Error: {err}")
  
  input("Hit Enter To Continue")
  admin_startup()

def update_item():
  """
  Function for updating Name, Price, Stock or Category of an item
  """

  option1 = input("Update Name, Price, Stock or Category ")
  
  #Checking user option
  
  if option1.strip().lower() == "name":
    
    #Asking for name changes
    usr_id = int(input("Enter Id "))
    new_name = input("Enter Name ")
    query = f"UPDATE inventory SET Item = {new_name} WHERE Id = {usr_id}"

  elif option1.strip().lower() == "price":

    #Asking for price changes
    usr_id = int(input("Enter Id "))
    new_price = float(input("Enter Price "))
    query = f"UPDATE inventory SET Price = {new_price} WHERE Id = {usr_id}"

  elif option1.strip().lower() == "stock":

    #Asking for stock changes
    usr_id = int(input("Enter Id "))
    new_stock = int(input("Enter Stock "))
    query = f"UPDATE inventory SET Stock = {new_stock} WHERE Id = {usr_id}"

  elif option1.strip().lower() == "category":

    #Asking for category changes
    usr_id = int(input("Enter Id "))
    new_category = int(input("Enter Category "))
    query = f"UPDATE inventory SET Category = {new_category} WHERE Id = {usr_id}"

  #Executing & Commiting query
  try: 
    mycursor.execute(query)
    db.commit()
  except mysql.connector.Error as err:
    print(f"Error: {err}")  

  input("Hit Enter To Continue")
  admin_startup()
  
def delete_item():
  """
  Function for deleting an item by Id
  """  

  usr_id = int(input("Enter Id "))
  
  #Showing item
  query = f"SELECT * FROM inventory WHERE Id = {usr_id} "
  mycursor.execute(query)
  for i in mycursor: print(i)

  confirmation = input("Delete Y/N?")
  
  if confirmation.strip().lower() == "n" or confirmation.strip().lower() != "y" :
    return None
  
  #Changing query
  query = f"DELETE FROM inventory WHERE Id = {usr_id}"

  #Executing & Commiting query 
  try:
    mycursor.execute(query)
    db.commit()
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  input("Hit Enter To Continue")
  admin_startup()

def search_item(mode):
  """
  Function for searching for an item by name or id
  """

  option = input("Search By Name or Id ")

  #Setting query according to user selection
  if option.strip().lower() == "id":
    usr_input = int(input("Enter Id: "))
    query = f"SELECT * FROM inventory WHERE Id = {usr_input}"
  
  elif option.strip().lower() == "name":
    usr_input = input("Enter Item Name: ")
    query = f"SELECT * FROM inventory WHERE Item LIKE '%{usr_input}%'"

  else: 
    print("Invalid Input")
    input("Hit Enter To Continue")
    if mode == 1: user_startup()
    else: admin_startup()

  #Executing query
  try:
    mycursor.execute(query)
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  #Showing Results
  for i in mycursor:
    id, name, price, stock, category = i
    dash = len(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")
    print("-"*70)
    print(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")
  

  print("-"*70)
  input("Hit Enter To Continue")
  if mode == 1: user_startup()
  else: admin_startup()

def update_quantity(mode):
  """
  Function for updating item quantity/stock
  """

  option1 = input("Update By Id or Name ")
  
  #Setting query according to user selection
  if option1.strip().lower() == "id":
    usr_id = int(input("Enter Id "))
    new_stock = int(input("Enter Stock "))
    query = f"UPDATE inventory SET Stock = {new_stock} WHERE Id = {usr_id}"

  elif option1.strip().lower() == "name":
    usr_name = int(input("Enter Name "))
    new_stock = int(input("Enter Stock "))
    query = f"UPDATE inventory SET Stock = {new_stock} WHERE Item LIKE '%{usr_name}%'"

  #Executing & Commiting query
  try:
    mycursor.execute(query)
    db.commit()
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  input("Hit Enter To Continue")
  if mode == 1: user_startup()
  else: admin_startup()

def view_inventory(mode):
  """
  Function to view the entire inventory
  """

  query = "SELECT * FROM inventory"
  mycursor.execute(query)
  
  #Showing Results
  for i in mycursor:
    id, name, price, stock, category = i
    dash = len(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")
    print("-"*70)
    print(f"{id:<5} {name:<25} ${price:<10.2f} {stock:^10} {category}")

  print("-"*70)
  input("Hit Enter To Continue")
  if mode == 1: user_startup()
  else: admin_startup()

def generate_reports(mode):
  """
  Function to generate entire inventory into .txt file
  """

  #Obtaining inventory
  query = "SELECT * FROM inventory"
  mycursor.execute(query)

  #Setting File Path
  file_path = f"{os.getcwd()}/report.txt"
  
  #Writing Data
  if os.path.exists(file_path):

    with open(r""+file_path,"a") as f:
      
      f.writelines("*"*10 + "\n")
      
      for i in mycursor:
        f.writelines(str(i) + "\n")
      f.writelines("*"*10 + "\n")
      
  else:
    
    with open(r""+file_path,"w") as f:
      
      f.writelines("*"*10 + "\n")
      
      for i in mycursor:
        f.writelines(str(i) + "\n")
      f.writelines("*"*10 + "\n")


  input("Hit Enter To Continue")
  if mode == 1: user_startup()
  else: admin_startup()

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
  