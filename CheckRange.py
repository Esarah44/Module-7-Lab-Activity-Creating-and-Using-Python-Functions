# Create Python function CheckRange(number)
# Sara Hernandez
# 11/13/2022
# Print how many times a number is in a given range

import random

#z=0

#This function only works for checking the passed number is in range or not
def CheckRange(number):
    #c=0
    #if y >= 1 and y <= 10:
    #    c=1
    if number in range(1, 10):
        return True
    else:
        return False

    #return c

#use main function to test CheckRange function.
def main():
    count = 0
    for i in range(20):
        y = random.randrange(1,15)
        if CheckRange(y):  #if the function returns True, then increase he count by 1.
            count += 1
        else:
            pass
    print("The number is in range for {} times.".format(count))
    
main()
 #   z = z + CheckRange(y)

#print (z)

