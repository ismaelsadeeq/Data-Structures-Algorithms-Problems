import math

def solveQueries( nums, Queries, k):
    #Code here
    answers= [0] *len(Queries)
      
    count = {}
    n = int(math.sqrt(len(nums)))+1
    q = list(enumerate(Queries))
     
    q.sort(key=lambda a:[int(a[1][0]/n),-a[1][1]])
    currentL=0
    currentR=-1
    ans = 0
       
    for i in q:
        left =i[1][0]-1
        right =i[1][1]-1
        
        while(currentR<right):
            currentR+=1
            count[nums[currentR]]=count.get(nums[currentR],0)+1
            if count[nums[currentR]]==k:
                ans+=1
                    
        while(currentL<left):
            count[nums[currentL]]-=1
                
            if count[nums[currentL]]==k-1:
                ans-=1
                currentL+=1
       
        while(currentR>right):
            count[nums[currentR]]-=1
            if count[nums[currentR]]==k-1:
                ans-=1
            currentR-=1
        while(currentL>left):
            currentL-=1
            count[nums[currentL]]=count.get(nums[currentL],0)+1
            if count[nums[currentL]]==k:
                ans+=1
            
        answers[i[0]]=ans
            
    return answers
            