import matplotlib
import scipy
import numpy
import math
import Physics_SpaceRacers
import random
import pygame

Sun = [Physics_SpaceRacers.Physics(1.989e30, 0,0,0,0,696265000, [255, 255, 0])]
planets = [ # mass , distance peri x, distance peri y, velocity x , velocity y, radius and color
    Physics_SpaceRacers.Physics(3.3011e23, 0.387 * Physics_SpaceRacers.AU, 0, 0, 47360, 2439700, [169, 169, 169]), # Mercury
    Physics_SpaceRacers.Physics(4.8675e24, 0.723 * Physics_SpaceRacers.AU, 0, 0, 35020, 6051800, [255, 223, 196]),  # Venus
    Physics_SpaceRacers.Physics(5.972168e24, 0.9833 * Physics_SpaceRacers.AU, 0, 0, 30286, 6371000, [0, 0, 225]),  # Earth (AT PERICENTER)
    Physics_SpaceRacers.Physics(6.4171e23, 1.524 * Physics_SpaceRacers.AU, 0, 0, 24077, 3389500, [255, 69, 0]), # Mars
    Physics_SpaceRacers.Physics(1.8982e27, 5.204 * Physics_SpaceRacers.AU, 0, 0, 13070, 69911000, [255, 215, 0]), # Jupiter
    Physics_SpaceRacers.Physics(5.6834e26, 9.582 * Physics_SpaceRacers.AU, 0, 0, 9680, 58232000, [218, 165, 32]), # Saturn
    Physics_SpaceRacers.Physics(8.6810e25, 19.201 * Physics_SpaceRacers.AU, 0, 0, 6800, 25362000, [173, 216, 230]), # Uranus
    Physics_SpaceRacers.Physics(1.02413e26, 30.07 * Physics_SpaceRacers.AU, 0, 0, 5430, 24622000, [0, 0, 139])   # Neptune
]
Moons = [# mass , distance peri x, distance peri y, velocity x , velocity y, radius and color
        Physics_SpaceRacers.Physics(7.3477e22, 0.98587 * Physics_SpaceRacers.AU, 0, 0, 31308, 1737000, [169, 169, 169]), # Luna
]
Players = [Physics_SpaceRacers.Spaceship(1e9, 8e7, 0.98358*Physics_SpaceRacers.AU,0,0, 33360.6,10000,[255,255,255], 0.1,0)] #Supposed to starts in GEO around earth
