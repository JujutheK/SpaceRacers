    # I am using vectors for most of the physics and coordinates
# Forgot how to read the vecotrs? [0] = x-direction ;  [1] = y-direction
# Mainain consistent Units:
# dsitance = m , mass = kg , velocity = m/s , acceleration = m/s^2

import matplotlib
import scipy
import numpy
import pygame
import math
import random
import pygame
pygame.init()
info = pygame.display.Info()
    # -------------------------------------------------
    # Game Settings
    # -------------------------------------------------

    # Screen dimensions
Scale = 2.7e-9
WIDTH = 2736
HEIGHT = 1824
timesteps = 12*3600 # Every second is 12 hours

class Camera:
    def __init__(self, camera_width, camera_height, zoom):
        self.camera_width = camera_width
        self.camera_height = camera_height
        self.camera_position = numpy.array((0,0) , dtype=float)  
        self.zoom = zoom
    def Peter (self, dx, dy):#Pan
        self.camera_position += numpy.array([dx,dy])
    def Skype(self, zoomfactor): #JK skype got discontinued, we Zoom now (teams actually better but ya know, jokes n stuff)
        self.zoom *= zoomfactor
        self.zoom = max(Scale, min(self.zoom, 2.16e-3) ) # min Zoom fits the entire solarsystem whil max zoom fits earth+GEO
    def update(self, Camera, keybind):
        key = pygame.key.get_pressed

    #--------------------------------------------
    # Physics
    #--------------------------------------------

G = 6.77430e-11 # Gravitational constant
AU = 149.6e9

    # ------------------------------------------------------------------
    #                     Celestial Bodies
    # -------------------------------------------------------------------

class Physics:
    def __init__(self, mass, position_x,position_y, velocity_x, velocity_y, Radius,colour):
            self.mass = mass
            self.position = numpy.array((position_x, position_y), dtype=float)
            self.velocity = numpy.array((velocity_x,velocity_y), dtype=float)
            self.footprint = Radius * Scale
            self.color = colour     
                        
    def update(self, CelestialBodies):
            total_gravitationalAcceleration = numpy.array((0,0), dtype=float)
            for CelestialBody in CelestialBodies:
                if CelestialBody is self:
                     continue             
                gravitational_direction = CelestialBody.position - self.position        
                x_distance = CelestialBody.position[0] - self.position[0]
                y_distance = CelestialBody.position[1] - self.position[1]
                distance_CelestialBodies = math.sqrt(x_distance**2 + y_distance**2)
                if distance_CelestialBodies <= self.footprint + CelestialBody.footprint:
                    distance_CelestialBodies = self.footprint + CelestialBody.footprint
                gravitational_force = (G * self.mass * CelestialBody.mass) / (distance_CelestialBodies**2)
                gravitational_acceleration = (gravitational_direction/distance_CelestialBodies)*(gravitational_force/self.mass)
                total_gravitationalAcceleration += gravitational_acceleration
            self.velocity += total_gravitationalAcceleration * timesteps
            self.position += self.velocity * timesteps
        
# if you are looking here then its because you probably because of capitalization. 
# Sucks to suck but you gave a bunch of shitty names at the start.   ¯\_(ツ)_/¯ 
# Camera = class =/= camera 
    def draw(self, surface, camera):
            center_width = camera.camera_width//2
            center_height = camera.camera_height//2
            screen_x = center_width + (self.position[0] - camera.camera_position[0]) * camera.zoom
            screen_y = center_height + (self.position[1] - camera.camera_position[1]) * camera.zoom
            screen_position = numpy.array([screen_x, screen_y])
            screen_radius = max(1, int((self.footprint/Scale)*camera.zoom))
            pygame.draw.circle(surface,self.color, screen_position, int(screen_radius))

# SPace ships as subcalss

class Spaceship(Physics):
        def __init__(self, mass, thrust,position_x,position_y, velocity_x, velocity_y, Radius,colour,turn_rate, angle):
            super().__init__(mass,position_x,position_y, velocity_x, velocity_y, Radius,colour)
            self.angle = angle
            self.thrust = thrust
            self.turn_rate= turn_rate

        def thrust_acceleration(self, Accelerate_MrSulu):
            direction = numpy.array([math.cos(self.angle), math.sin(self.angle)])
            Accelerate_MrSulu = self.thrust / self.mass
            self.velocity += direction * Accelerate_MrSulu * timesteps

        def Turn(self, turn_rate):
            self.angle += turn_rate

        def update(self, CelestialBodies, keybind=None ):
            if keybind:
            #controls
                key = pygame.key.get_pressed
                if key [keybind[pygame.K_UP]]:
                    if self.thrust <=1:
                        self.thrust += 0.05
                    else:
                        self.thrust += 0
                if key [keybind[pygame.K_DOWN]]:
                    if self.thrust >= -1:
                        self.thrust -=0.05
                    else:
                        self.thrust -=0
                if key [keybind[pygame.K_LEFT]]:
                    if self.turn_rate >=-1:
                        self.turn_rate-= 0.05
                    else:
                        self.turn_rate -= 0
            
                if key [keybind[pygame.K_RIGHT]]:
                    if self.turn_rate <= 1:
                        self.turn_rate += 0.05
                    else:
                        self.turn_rate += 0 
            super().update(CelestialBodies)