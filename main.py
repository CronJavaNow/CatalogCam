import os
import cam_mngr
import file_mngr

def user_welcome():
    #issue msg to user.
    print("Welcome to CatalogCam!")
    #if catalog directory does not exists create~>
    if not os.path.exists("Catalog"):
        #create Catalog
        os.makedirs("Catalog")
    #issue msg with input(1) to user
    welcnput = input("Type new to create category/item folder or press Enter for Catalog \n Please type |New or Enter|: ")
    #look for user input(1)
    if welcnput.lower() == "new":
        #if user input(1) = new | request file_mngr.createfl | take user input(2) to file_mngr
        file_mngr.createfl(i = input("Please type the name of your category or item specific folder: "))
    else:
        #load up file directories in the catalog file
        catalogdir = dict(enumerate(os.listdir("Catalog")))
        #issue msg to user~> list file directories with enumerate keys i.e 0,1,2,3
        print(catalogdir)
        #issue input(3) and allow user to pick a directory {STILL NEEDS WORK}
        cam_mngr.ask_user(i = catalogdir[int(input("Please enter the id/number of the directory you would like to use: "))])

user_welcome()