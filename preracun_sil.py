import numpy as np

def mass():
     return np.sum([M_FRONT_LEFT, M_FRONT_RIGHT, M_REAR_LEFT, M_REAR_RIGHT])
def fi():
     return np.arcsin(DH/a)
def z():
    return x*np.cos(fi())

# Constants

g = 9.81


# Input data

M_DRIVER = 100
b = 1000
a = 1550
DH = 200
    # Static test of measurement of mass with all wheels on horizontal surface with driver
    # in monocoque 
M_FRONT_LEFT = 50
M_FRONT_RIGHT = 50
M_REAR_LEFT = 75
M_REAR_RIGHT = 75
    # Static test of measurement of mass with all wheels on surface under incident angle
    # [Defined with a lifting off front axle from the horizontal surface]
M_FRONT_LEFT_ANGLE = 20
M_FRONT_RIGHT_ANGLE = 20
M_REAR_LEFT_ANGLE = 95
M_REAR_RIGHT_ANGLE = 95

mg = mass()*g

# Calculation of forces on each wheel

F_FRONT_LEFT_NORMAL = M_FRONT_LEFT * g
F_FRONT_RIGHT_NORMAL = M_FRONT_RIGHT * g
F_REAR_LEFT_NORMAL = M_REAR_LEFT * g
F_REAR_RIGHT_NORMAL = M_REAR_RIGHT * g

F_FRONT_LEFT_ANGLE = M_FRONT_LEFT_ANGLE * g
F_FRONT_RIGHT__ANGLE = M_FRONT_RIGHT_ANGLE * g 
F_REAR_LEFT_ANGLE = M_REAR_LEFT_ANGLE * g
F_REAR_RIGHT_ANGLE = M_REAR_RIGHT_ANGLE * g

# Calculation of CoG
# a) Latheral location of CoG

b1 = ((F_REAR_RIGHT_NORMAL + F_FRONT_RIGHT_NORMAL)/mg) * b
print(b1)

# a) Longitudinal location of CoG

a1 = ((F_FRONT_RIGHT_NORMAL + F_FRONT_LEFT_NORMAL)/mg) * a
print(a1)

# a) Vertical location of CoG

x = ((F_FRONT_LEFT_ANGLE + F_FRONT_LEFT_ANGLE) * (a * np.cos(fi())))/(mg)
print(x)

print(z())