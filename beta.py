import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((800, 700))


cam = pygame.camera.Camera('/dev/video0', (800, 600), 'RGB')
cam.start()

while 1:
    image = cam.get_image()
    screen.blit(image, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            sys.exit()
