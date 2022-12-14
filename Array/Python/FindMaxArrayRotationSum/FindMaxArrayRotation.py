
def findMaxValueOfSum(A):
    
    
    arrSum = 0
    currValue = 0
    n = len(A)
    for i in range(0,n):
        arrSum += A[i]
        currValue += i * A[i]
        
    maxSum = currValue
    for i in range(1,n):
        currValue = currValue + arrSum - (n * A[n-i])
        if currValue > maxSum:
            maxSum = currValue
            
    
    
    return maxSum
        
        
array1 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array2 = [1, 20, 2, 10]
print(findMaxValueOfSum(array1))
print(findMaxValueOfSum(array2))