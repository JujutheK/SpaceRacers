import matplotlib
import scipy
import numpy
import math
import Physics_SpaceRacers
import random
import pygame
import Objects_Spaceracers
pygame.init()
info = pygame.display.Info()

pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
screen = pygame.display.set_mode((Physics_SpaceRacers.WIDTH, Physics_SpaceRacers.HEIGHT))
clock = pygame.time.Clock()
Objects=Objects_Spaceracers.Sun+Objects_Spaceracers.planets + Objects_Spaceracers.Players
camera = Physics_SpaceRacers.Camera(Physics_SpaceRacers.WIDTH, Physics_SpaceRacers.HEIGHT, Physics_SpaceRacers.Scale)



gamerunning=True
while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                camera.Skype (1.1)
            elif event.button == 5:
                camera.Skype (0.9)
    camera.camera_position = numpy.copy(Objects_Spaceracers.Players[0].position)
    for all in Objects:
        all.update(Objects)
    screen.fill((0,0,0))
    for all in Objects:
        all.draw(screen, camera)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()