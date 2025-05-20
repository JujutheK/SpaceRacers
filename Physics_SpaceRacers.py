    # I am using vectors for most of the physics and coordinates




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
timesteps = 86400 # Every second is a day

class Camera:
    def __init__(self, camera_width, camera_height, zoom):
        self.camera_width = camera_width
        self.camera_height = camera_height
        self.camera_position = numpy.array((0,0) , dtype=float)  
        self.zoom = zoom
    def Peter (self, dx, dy):#Pan
        camera_position += numpy.array([dx,dy])
    def Skype(self, zoomfactor): #JK skype got discontinued, we Zoom now (teams actually better but ya know, jokes n stuff)
        self.zoom *= zoomfactor
        self.zoom = max(Scale, min(self.zoom, 2.16e-5) ) # min Zoom fits the entire solarsystem whil max zoom fits earth+GEO
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
        
    def gravitational_force(self, other):
            x_distance = other.position - self.position
            y_distance = other.position - self.position
            distance_CelestialBodies = math.sqrt(x_distance**2 + y_distance**2)
            if distance_CelestialBodies <= self.radius + other.radius:
                distance_CelestialBodies = self.radius + other.radius
            self.gravitational_force = (G * self.mass * other.mass) / (distance_CelestialBodies**2)
            
    def update(self, CelestialBodies):
            for CelestialBody in CelestialBodies:
                total_gravitationalAcceleration = numpy.array((0,0), dtype=float)
                if not self:   
                    total_gravitationalAcceleration += self.gravitational_force(CelestialBody)
            self.velocity += total_gravitationalAcceleration * timesteps
            self.position += self.velocity * timesteps
        
# if you are looking here then its because you probably because of capitalization. 
# Sucks to suck but you gave a bunch of shitty names at the start.   ¯\_(ツ)_/¯ 
# Camera = class =/= camera 
    def draw(self, surface, camera):
            center_width = camera.camera_width//2
            center_height = camera.camera_height//2
            self.x = int(center_width + (self.position[0] - camera.camera_position[0]) * Scale)
            self.y = int(center_height + (self.position[1] - camera.camera_position[1]) * Scale)
            self.radius = max(1, int(self.footprint))
            pygame.draw.circle(surface,self.color, (self.x, self.y), float(self.footprint))

# SPace ships as subcalss

class Spaceship(Physics):
        def __init__(self, mass, thrust,position_x,position_y, velocity_x, velocity_y, Radius,colour,turn_rate, angle):
            super().__init__(self, mass,position_x,position_y, velocity_x, velocity_y, Radius,colour)
            self.angle = angle
            self.thrust = thrust
            self.turn_rate= turn_rate

        def thrust_acceleration(self, Accelerate_MrSulu):
            direction = numpy.array([math.cos(self.angle), math.sin(self.angle)])
            Accelerate_MrSulu = self.thrust / self.mass
            self.velocity += direction * Accelerate_MrSulu * timesteps

        def Turn(self, turn_rate):
            self.angle += turn_rate

        def update(self, CelestialBodies, keybind ):
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
            super.update(CelestialBodies)