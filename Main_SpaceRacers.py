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
font = pygame.font.SysFont("Arial", 14)
screen = pygame.display.set_mode((Physics_SpaceRacers.WIDTH, Physics_SpaceRacers.HEIGHT))
clock = pygame.time.Clock()
Objects=Objects_Spaceracers.Sun+Objects_Spaceracers.planets + Objects_Spaceracers.Players + Objects_Spaceracers.Moons
camera = Physics_SpaceRacers.Camera(Physics_SpaceRacers.WIDTH, Physics_SpaceRacers.HEIGHT, Physics_SpaceRacers.Scale)
player_controls = [
    {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, "fire": pygame.K_SPACE},  # Player 1 Arrows
    {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d, "fire": pygame.K_f},            # Player 2 WASD
]


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
    keys= pygame.key.get_pressed()
    for all in Objects:
        if isinstance(all, Physics_SpaceRacers.Spaceship):
            all.update(Objects,player_controls[0], keys)
        else:
            all.update(Objects)
    camera.camera_position = numpy.copy(Objects_Spaceracers.Players[0].position) # This line has to be after the update function, otherwise the camera lags behind the spacecraft!
    screen.fill((0,0,0))
    for all in Objects:
        all.draw(screen, camera)
#------------------------------------------------------------------
# UI 
# ------------------------------------------------------------------------
    x_velocity = Objects_Spaceracers.Players[0].velocity[0]
    y_velocity = Objects_Spaceracers.Players[0].velocity[1]
    x_velocity_text =font.render(f'x-velocity = {x_velocity}', True, [255,255,255])
    y_velocity_text = font.render(f'y-velocity = {y_velocity}', True, [255,255,255])
    #position_textx = Physics_SpaceRacers.WIDTH -x_velocity_text.get_width() -10
    #positiontexty = Physics_SpaceRacers.HEIGHT- x_velocity_text.get_height() - y_velocity_text.get_height() - 20
    screen.blit(x_velocity_text, (10,10))
    screen.blit(y_velocity_text, (10,10 + x_velocity_text.get_height()))
    throttle_text = font.render(f'Throttle: {Objects_Spaceracers.Players[0].current_thrust:.2f}', True, (255,255,255))
    screen.blit(throttle_text, (10, 30 + y_velocity_text.get_height()))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()