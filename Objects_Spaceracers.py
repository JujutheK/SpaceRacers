import matplotlib
import scipy
import numpy
import math
import Physics_SpaceRacers
import random
import pygame
import Physics_SpaceRacers

Sun = [Physics_SpaceRacers.Physics(1.989e30, 0,0,0,0,696265000, [255, 255, 0])]
planets = [
    Physics_SpaceRacers.Physics(5.972168e24, 0.9833*Physics_SpaceRacers.AU, 0, 0, 30286, 6371000,[0,0,225])
]