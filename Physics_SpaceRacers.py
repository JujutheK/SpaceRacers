    # I am using vectors/matrices for most of the physics and coordinates
# Forgot how to read the vecotrs? For this project:  [0] = x-direction/coordinate ;  [1] = y-direction/coordinate
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
Scale = 3.05e-10
WIDTH = 1200#2736
HEIGHT = 850# 1824
timesteps = 1440 # Every second is 1 day (60 ticks/sec * 60 Minutes * 24H) NOTE: I tried doing 3600, ie a second is a day, so at some timestep > 1440 the game breaks
# timestep 1440 works pretty well, also with ease of control for the spaceship.

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
        self.zoom = max(Scale, min(self.zoom, 2.16e-2) ) # min Zoom fits the entire solarsystem whil max zoom fits earth+GEO
    def update(self, Camera, keybind):
        key = pygame.key.get_pressed()

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
        
# if you are looking here then its brobably because of capitalization. 
# Sucks to suck but you gave a bunch of shitty names at the start.   ¯\_(ツ)_/¯ 
# Camera = class =/= camera 
    def draw(self, surface, camera):
            center_width = camera.camera_width//2
            center_height = camera.camera_height//2
            screen_x = center_width + (self.position[0] - camera.camera_position[0]) * camera.zoom
            screen_y = center_height + (self.position[1] - camera.camera_position[1]) * camera.zoom
            screen_position = numpy.array([screen_x, screen_y])
            screen_radius = max(1, int((self.footprint/Scale)*camera.zoom)) #limits the size of da ship
            pygame.draw.circle(surface,self.color, screen_position, int(screen_radius))

# SPace ships as subcalss of physics

class Spaceship(Physics):
        def __init__(self, mass, thrust,position_x,position_y, velocity_x, velocity_y, Radius,colour,turn_rate, angle):
            super().__init__(mass,position_x,position_y, velocity_x, velocity_y, Radius,colour)
            self.angle = 0
            self.max_thrust = thrust
            self.current_thrust = 0
            self.turn_rate= turn_rate

        def thrust_acceleration(self):
            direction = numpy.array([math.cos(self.angle), math.sin(self.angle)])
            Accelerate_MrSulu = self.current_thrust / self.mass
            self.velocity += direction * Accelerate_MrSulu * timesteps

        def Turn(self, turn_rate):
            self.angle += turn_rate

        def draw(self, surface, camera): 
            #gotta define the position of the spacecraft w.r.t the camera, otherwise you wont see a thing
            center_width = camera.camera_width // 2
            center_height = camera.camera_height // 2
            screen_x = center_width + (self.position[0] - camera.camera_position[0]) * camera.zoom
            screen_y = center_height + (self.position[1] - camera.camera_position[1]) * camera.zoom
            visual_scale=max(1, int((self.footprint / Scale) * camera.zoom)) * 5 # without this the spaceship is the size of three pixels, and due to scale these pixels dont always point in the exact direction, hence, we scale the "appearance"
#Arya, you stick 'em with the   
            pointyend = (screen_x + visual_scale * math.cos(self.angle), screen_y + visual_scale * math.sin(self.angle))
            leftend = (screen_x + visual_scale * math.cos(self.angle + 3*math.pi/4), screen_y + visual_scale * math.sin(self.angle + 3*math.pi/4))
            rightend = (screen_x + visual_scale * math.cos(self.angle - 3*math.pi/4), screen_y + visual_scale * math.sin(self.angle - 3*math.pi/4))
            pygame.draw.polygon(surface, (255,255,255), [pointyend, leftend, rightend])
            #confused what I did here? I made the spaceship an equilateral triangle!
            # But wait, Juju, the angles of an equilateral triangle are pi/3 ! 
            #Yes but we are using the outer angles of the vertice-pointy end, so its 2pi/3. 
            # But juju, the user won't know which way is forward with an equilateral triangle! 
            #sigh.... sh*t
            # ----> that was the story behind why I am using an isoceles instead of equilateral triangle, its not eventfull, but it did take a few hours
 
             
        def update(self, CelestialBodies, controls, keys):
            #controls
            if keys[controls["left"]]:
                self.Turn(-self.turn_rate)
            if keys[controls["right"]]:
                self.Turn(self.turn_rate)
            if keys[controls["up"]]:
                self.current_thrust = min(self.current_thrust + 0.02*self.max_thrust, 5*self.max_thrust) 
                #limit max thrust to two times the thrust value. 
                # Why not just double the thrust value you ask? Because 200 % sounds cooler than 100%. 
            elif keys[controls["down"]]:
                self.current_thrust = min(self.current_thrust - 0.02*self.max_thrust, -5*self.max_thrust) 
            else: 
                 self.current_thrust = 0
                        
            self.thrust_acceleration()
            super().update(CelestialBodies)
            
