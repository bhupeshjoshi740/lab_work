#create a module that contains the functions to perform all the operation on threedfigures(cube,cuboid,cylinder,cone,sphere,hemisphere).
import math   # To use value of pi

# -------- CUBE --------
def cube_surface_area(a):      # a = side of cube
    return 6 * a * a           # Formula: 6a²

def cube_volume(a):            # a = side
    return a ** 3              # Formula: a³


# -------- CUBOID --------
def cuboid_surface_area(l, b, h):   # l=length, b=breadth, h=height
    return 2 * (l*b + b*h + l*h)    # Formula: 2(lb + bh + lh)

def cuboid_volume(l, b, h):
    return l * b * h                # Formula: l × b × h


# -------- CYLINDER --------
def cylinder_csa(r, h):        # r=radius, h=height
    return 2 * math.pi * r * h # Formula: 2πrh

def cylinder_volume(r, h):
    return math.pi * r * r * h # Formula: πr²h


# -------- CONE --------
def cone_volume(r, h):         
    return (1/3) * math.pi * r * r * h  # Formula: 1/3 πr²h


# -------- SPHERE --------
def sphere_surface_area(r):
    return 4 * math.pi * r * r        # Formula: 4πr²


# -------- HEMISPHERE --------
def hemisphere_volume(r):
    return (2/3) * math.pi * r ** 3   # Formula: 2/3 πr³