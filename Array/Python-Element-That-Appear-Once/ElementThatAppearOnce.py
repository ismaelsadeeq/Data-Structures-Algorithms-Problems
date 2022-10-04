"""
Given an array of items find the element that occurred once
"""

def occurredOnce(array):

    # Dictionary of items
    items = {}

    for i in range(0,len(array)):

        # items has array[i] as key?
        if(items.get(array[i])):
            # if yes increments its value by 1
            items[array[i]] = items[array[i]] +1
        else:
            # It does not has the key, create it with 1 as the value
            items[array[i]] = 1

        
    # loop through  items to get the key with 1 as value
    for item in items:
        # check if one is the value of item
        if items[item] == 1:
            # if yes return the item
            return item

    # there is no value with 1 return -1
    return -1