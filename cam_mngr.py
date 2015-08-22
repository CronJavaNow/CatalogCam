import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

camlst = dict(enumerate(pygame.camera.list_cameras()))
#pickcam = input("Would you like a list of connected cameras? \n please type:|Yes or press Enter| ")

def user_camsnap():
    print(camlst)
    usercam = int(input("Please enter the id/number of the camera you would like to use: "))
    cam = pygame.camera.Camera(camlst[usercam], (352,288))
    cam.start()
    image= cam.get_image()
    #list dir selc in main and put here
    pygame.image.save(image,'images/101.jpg')
    cam.stop()

def default_camsnap():
    cam = pygame.camera.Camera(camlst[0], (352,288))
    cam.start()
    image= cam.get_image()
    #list dir selc in main and put here
    pygame.image.save(image,'images/101.jpg')
    cam.stop()