"""
In this case, a "special" array is given that contains 
either integers or a sub-array. The Product Sum is the 
sum of elements inside the array (or sub-array) multiplied by 
the level of depth

The depth is how far nested the array is.
"""

def productSum(array, depth=1):
    currentSum = 0
    for el in array:
        if type(el) is int:
            currentSum += el
            continue
        currentSum += productSum(el, depth + 1)
    return depth * currentSum