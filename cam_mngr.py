import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

camlst = dict(enumerate(pygame.camera.list_cameras()))

def catalog_directory(i):
    ask_user()
    return  i

def ask_user():
    pickcam = input("Would you like a list of connected cameras? \n please type:|Yes or press Enter| ")
    if pickcam.lower() == "yes":
        user_camsnap()
    else:
        default_camsnap()

def user_camsnap():
    print(camlst)
    usercam = int(input("Please enter the id/number of the camera you would like to use: "))
    cam = pygame.camera.Camera(camlst[usercam], (352,288))
    cam.start()
    image= cam.get_image()
    #still needs some work!
    pygame.image.save(image,'Catalog/{}/101.jpg'.format(catalog_directory()))
    cam.stop()

def default_camsnap():
    cam = pygame.camera.Camera(camlst[0], (352,288))
    cam.start()
    image= cam.get_image()
    #still need some work
    pygame.image.save(image,'Catalog/{}/101.jpg'.format(catalog_directory()))
    cam.stop()