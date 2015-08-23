import os
import cam_mngr
import file_mngr

def start():
    if not os.path.exists("Catalog"):
        os.makedirs("Catalog")
        user_welcome()
    else:
        user_welcome()

def user_welcome():
    print("Welcome to CatalogCam!")
    usernput = input("Type new to create category/item folder or press Enter for Catalog \n Please type |New or Enter|: ")

    if usernput.lower() == "new":
        file_mngr.createfl(i=input("Please type the name of your category or item specific folder: "))
    else:
        catalogdir = dict(enumerate(os.listdir("Catalog")))
        print(catalogdir)
        cam_mngr.ask_user(i=catalogdir[int(input("Please enter the id/number of the directory you would like to use: "))])

start()
