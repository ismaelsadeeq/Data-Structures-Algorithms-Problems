"""
The function that checks whether there are two numbers
that makes up a sum in an array
using two pointer approach
"""

def two_pointer(array,x):

    array.sort()

    left = 0

    right = 0
    for i in range(0,len(array)-1):

        sum = array[left] + array[right]
        if sum == x:
            return True
        elif sum > x:
            right-=1
        elif sum < x:
            left+=1

    return False
