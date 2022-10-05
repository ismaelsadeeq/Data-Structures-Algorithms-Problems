"""
Given 2 non-empty arrays of integers, check wether the second  array is a valid subsequence of the first one

A subsequence array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array

For example:
  a = [1, 2, 3, 4, 5]
  b = [1, 3]
  c = [4, 2, 1]

  > b is a valid subsequence of a
  > c is not a valid subsequence of a
"""

def isValidSubsequence(array, sequence):
    
    for i in sequence:
        if i in array:
            ind = array.index(i)
            array = array[ind + 1:]
        else:
            return False
    return True