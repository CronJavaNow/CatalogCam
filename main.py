import os
import cam_mngr
import file_mngr



def wlcome():
    print("Welcome to CatalogCam!")
    if not os.path.exists("Catalog"):
        os.makedirs("Catalog")
    wlcnput = input("Type new to create category/item folder or press Enter for Catalog \n Please type |New or Enter|: ")
    if wlcnput.lower() == "new":
        file_mngr.createfl(flname = input("Please type the name of your category or item specific folder: "))
    else:
        print(os.listdir("Catalog"))



wlcome()