import math 


def distinctElements(nums,query):

    n = int(math.sqrt(len(nums))) + 1

    query = list(enumerate(query))

    query.sort(key= lambda a:[int(a[1][0]/n),-a[1][1]])

    ans = [0] * len(query)

    maxVal = max(nums)
    
    F = [0] * (maxVal+1)

    count = 0

    start = query[0][1][0]-1
    end = query[0][1][0]-2

    for q in query:
        
        left = q[1][0]-1
        right = q[1][1]-1
        
        while(end < right):
            end+=1
            val = nums[end]
            F[val] +=1
            if F[val] == 1:
                count+=1
            

        while(start < left):
            val = nums[start]
            F[val]-=1
            if F[val] == 0:
                count-=1

            start +=1
        
        while (end > right):
            val = nums[end]
            F[val] -=1
            if F[val] == 0:
                count-=1
            
            end-=1

        while(start > left):
            val = nums[start]
            F[val]+=1
            if F[val] == 1:
                count+=1
            
            
            start+=1
            
            
        


        ans[q[0]] = count

    return ans



        
nums = [1, 1, 2, 1, 3]
q = [[1, 5],[2, 4],[3, 5]]

print(distinctElements(nums,q))
# 