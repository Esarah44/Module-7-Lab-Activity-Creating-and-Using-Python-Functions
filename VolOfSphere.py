# Create Python fucntion VolOfSphere
# Sara Hernandez
# 11/7/2022
# Write a function VolOfSphere(r) which returns the volume of a sphere of radius r.

import math

def VolOfSphere(r):
    result = (4/3) * math.pi * r*r*r
    return result

radius = int(input("Enter a radius of a sphere:"))

volume = VolOfSphere(radius)

print("The volume of sphere is ", volume)
