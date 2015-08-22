import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

camlst = pygame.camera.list_cameras()
pickcam = input("Would you like to list connected cameras? \n please type:|Yes or press Enter| ")

if pickcam.lower() == ("yes"):
    print(camlst)

def user_camsnap():
    print("Soon something cool will take place!")

def default_camsnap():
    cam = pygame.camera.Camera(camlst[0], (352,288))
    cam.start()
    image= cam.get_image()
    pygame.image.save(image,'images/101.jpg')
    cam.stop()