# Create Python function CheckRange(number)
# Sara Hernandez
# 11/13/2022
# Print how many times a number is in a given range

import random

z=0

def CheckRange(number):
    c=0
    if y >= 1 and y <= 10:
        c=1
    return c

for i in range(1,20):
    y = random.randrange(1,15)
    z = z + CheckRange(y)

print (z)

