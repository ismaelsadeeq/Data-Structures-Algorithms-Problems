"""
Given an array of items find the element that occurred once
"""

def occurredOnce(array):

    items = {}

    for i in range(0,len(array)):

        if(items.get(array[i])):
            items[array[i]] = items[array[i]] +1
        else:
            items[array[i]] = 1

        
    
    for item in items:
        if items[item] == 1:
            return item
    
    return -1