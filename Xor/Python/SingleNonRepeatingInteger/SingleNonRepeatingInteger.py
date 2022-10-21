def singleNonRepeating(nums):

    value = nums[0]

    for i in range(0,len(nums)):

        value = value ^ nums[i]

    
    return nums