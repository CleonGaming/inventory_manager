import inventory_manager as im
import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

im.user_startup()

