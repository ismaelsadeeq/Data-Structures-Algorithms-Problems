class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()


        maxSum = 0
        for i in range(0, len(nums)-2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum = nums[i] + nums[left] + nums[right]
    
                if i == 0 and sum > 0:
                    maxSum = sum
            
                if sum == target:
                    return sum
                if target < 0:
                    if target - sum > target - maxSum:
                        maxSum = sum 
                else:    
                    if target - sum < target - maxSum:
                        maxSum = sum 
                if sum > target:
                    right-=1
                if sum < target:
                    left+=1

        return maxSum