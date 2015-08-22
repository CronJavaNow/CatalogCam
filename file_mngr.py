import os

def createfl(flname):
   if not os.path.exists("Catalog/{}".format(flname)):
       os.makedirs("Catalog/{}".format(flname))
   else:
       print("Seems file {} already exists!".format(flname))
       createfl(flname = input("Please type the name of your category or item specific folder: "))

