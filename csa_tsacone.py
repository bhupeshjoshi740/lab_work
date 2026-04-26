#create a python program to find out curved surface area ,total surface areaand volume .
import math   # To use the value of pi

# Taking input from user
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

# Curved Surface Area (CSA)
# Formula: 2πrh
csa = 2 * math.pi * r * h

# Total Surface Area (TSA)
# Formula: 2πr(r + h)
tsa = 2 * math.pi * r * (r + h)

# Volume
# Formula: πr²h
volume = math.pi * r * r * h

# Displaying the results
print("Curved Surface Area:", csa)
print("Total Surface Area:", tsa)
print("Volume:", volume)