#create a python program to find out curved surface area,total surface area and volime of cuboid.
#Take input from user
l = float(input("Enter length of cuboid: "))
b = float(input("Enter breadth of cuboid: "))
h = float(input("Enter height of cuboid: "))

# Curved Surface Area (Lateral Surface Area)
# Formula: 2h(l + b)
csa = 2 * h * (l + b)

# Total Surface Area
# Formula: 2(lb + bh + lh)
tsa = 2 * (l*b + b*h + l*h)

# Volume
# Formula: l × b × h
volume = l * b * h

# Displaying results
print("Curved Surface Area (Lateral Surface Area):", csa)
print("Total Surface Area:", tsa)
print("Volume:", volume)