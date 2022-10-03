"""
 Linear Search is an algorthm that takes two input array and Integer"
 It returns the index of the integer in the array or -1 if it does not exist"


@param array is an array of elements
@param number is and element to be searched

"""
def linear_search(array,number):
    

    for i in range(0,len(array)):

        if array[i] == number:
            return i

    return -1


