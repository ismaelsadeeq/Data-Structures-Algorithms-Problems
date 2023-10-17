import math
def sumOfRanges(nums,n,Queries):
    
    
    b = int(math.sqrt(n))
    
    nB = int(n/b)+1
    
    
    blocks = []
    
    for i in range(nB):
        blocks.append([])
    
    answers = []
    
    for query in Queries:
        
        start = query[0]
        end = query[1]
        
        valueOfBlocksSkipped = start / b 
        
        blocksSkipped = math.floor(valueOfBlocksSkipped)
        
        elementsSkipped = (valueOfBlocksSkipped - blocksSkipped) * b
         
        left = int(blocksSkipped + elementsSkipped)
        sum = 0
        while( left <= end and (left / b).is_integer()  == False):
            sum += nums[left]
            left+=1
        
        while(left + b <= end ):
            currentBlock = int((left + b) / b)
            if len(blocks[currentBlock -1]) == 0:
                valSum = 0
                i = (currentBlock - 1) * b
                j = i + b
                while(i < j):
                    valSum += nums[i]
                    i+=1
                
                blocks[currentBlock -1].append(valSum)
            
            sum+= blocks[currentBlock -1][0]
            left = left + b
        
        while(left <= end):
            sum += nums[left]
            left+=1
        
        
        answers.append(sum)
        
    
    return answers
    
    
    
nums = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
n = len(nums)

print(sumOfRanges(nums,n,Q))
            
                    