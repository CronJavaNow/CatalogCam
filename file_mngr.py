import os

def createfl(i):
   if not os.path.exists("Catalog/{}".format(i)):
       os.makedirs("Catalog/{}".format(i))
   else:
       print("Seems file {} already exists!".format(i))
       createfl(i = input("Please type the name of your category or item specific folder: "))

