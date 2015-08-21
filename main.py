import pygame
import pygame.camera

pygame.init()
pygame.camera.init()


lstcams = raw_input("Would you like to list connected cameras? \n please type:|Yes or press Enter| ")

if lstcams == ("yes") or ("Yes"):
    camlist = pygame.camera.list_cameras()
    print (camlist)
else:
    print("Item Cam will now find the first camera it can & connect to it!")
    cam = pygame.camera.Camera("/dev/video0",(352,288))
    cam.start()
    image= cam.get_image()
    pygame.image.save(image,'images/101.jpg')
    cam.stop()