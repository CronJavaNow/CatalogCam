import random
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

camlst = dict(enumerate(pygame.camera.list_cameras()))

def ask_user(i):
    pickcam = input("Would you like a list of connected cameras? \n please type:|Yes or press Enter| ")
    if pickcam.lower() == "yes":
        user_camsnap(i=i)
    else:
        default_camsnap(i=i)

def user_camsnap(i):
    print(camlst)
    usercam = int(input("Please enter the id/number of the camera you would like to use: "))
    cam = pygame.camera.Camera(camlst[usercam], (352,288))
    cam.start()
    image= cam.get_image()
    #still needs some work!
    pygame.image.save(image, "Catalog/{}/101.jpg".format(i))
    cam.stop()

def default_camsnap(i):
    cam = pygame.camera.Camera(camlst[0], (352,288))
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, "Catalog/{}/{}_{}.jpg".format(i, i, random.sample(range(99, 9999), 1)))
    cam.stop()
    print("Snap Complete!")
    val = input("would you like to take more?: \n Please type yes or press Enter to exit ")
    if val.lower() == "yes":
        default_camsnap(i)
    else:
        import main
        main.user_welcome()
