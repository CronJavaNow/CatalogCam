import pygame
import pygame.camera
from collections import Counter

pygame.init()
pygame.camera.init()
cnt = Counter()

camlst = pygame.camera.list_cameras()

pickcam = input("Would you like a list connected cameras? \n please type:|Yes or press Enter| ")

def user_camsnap():
    print("Something cool will take place soon!")
    print(camlst)

def default_camsnap():
    cam = pygame.camera.Camera(camlst[0], (352,288))
    cam.start()
    image= cam.get_image()
    pygame.image.save(image,'images/101.jpg')
    cam.stop()

if pickcam.lower() == ("yes"):
    user_camsnap()
else:
    default_camsnap()