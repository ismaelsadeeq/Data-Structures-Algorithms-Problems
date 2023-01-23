
def findKSubArr(arr,k):
    
    sums = []
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            subArrSum = sum(arr[i:j+1])
            sums.append(subArrSum)
        
    sums.sort()
    
    j = len(sums) - 1
    ans = []
    for i in range(k):
        ans.append(sums[j])
        j-=1
        
    return ans
    
arr = [4, -8, 9, -4, 1, -8, -1, 6]
k = 4
k2 = 3
arr2 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(findKSubArr(arr,k))
print(findKSubArr(arr2,k2))
