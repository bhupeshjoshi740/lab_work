#create a python program to find out curved surface area,total surface area and volume of cylinder.
import math   # Importing math module to use value of pi

# Taking input from user
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))

# Calculating Curved Surface Area (CSA)
# Formula: 2πrh
csa = 2 * math.pi * radius * height

# Calculating Total Surface Area (TSA)
# Formula: 2πr(r + h)
tsa = 2 * math.pi * radius * (radius + height)

# Calculating Volume
# Formula: πr²h
volume = math.pi * radius * radius * height

# Displaying the results
print("Curved Surface Area (CSA):", csa)
print("Total Surface Area (TSA):", tsa)
print("Volume:", volume)