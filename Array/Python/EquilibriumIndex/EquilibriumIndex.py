# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
   
    if n==0 :
        return -1
    if n == 1:
        return 1
    arrSum = sum(a)
    tempSum = a[0]
    for i in range(1,n):
  
        currSum = tempSum + a[i]
        if tempSum == (arrSum - currSum):
            return i
        else:
            tempSum = currSum
    
    return - 1
