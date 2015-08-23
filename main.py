import os
import cam_mngr
import file_mngr



def wlcome():
    print("Welcome to CatalogCam!")
    if not os.path.exists("Catalog"):
        os.makedirs("Catalog")
    wlcnput = input("Type new to create category/item folder or press Enter for Catalog \n Please type |New or Enter|: ")
    if wlcnput.lower() == "new":
        file_mngr.createfl(i = input("Please type the name of your category or item specific folder: "))
    else:
        catalogdir = dict(enumerate(os.listdir("Catalog")))
        print(catalogdir)
        cam_mngr.catalog_directory(i = catalogdir[int(input("Please enter the id/number of the directory you would like to use: "))])

wlcome()