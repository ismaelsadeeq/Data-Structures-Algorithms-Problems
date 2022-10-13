class Solution:
    def maxArea(self, height):
        if len(height)<2:
            return 0
        
        maxWater = 0
        left = 0
        right = len(height)-1
        for i in range(0,len(height)):
            length = (right+1)-(left+1)
            tall = 0 
            if(height[left]< height[right]):
                tall = height[left]
            else:
                tall = height[right]                              
            temp = length * tall
            if temp > maxWater:
                maxWater = temp
            if height[left] > height[right]:
                right-=1
            else:
                left+=1

        return maxWater



