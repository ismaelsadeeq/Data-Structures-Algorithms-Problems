def findPivot(A,l,r):
    
    if l > r:
        return -1
        
    mid = (l + r) // 2
    
    if A[mid] < A[mid -1] :
        return mid
    
    if A[mid] > A[mid+1] :
        return mid+1 
    
    if A[mid] < A[l]:
        return findPivot(A,l,mid-1)
    return findPivot(A,mid+1,r)
    
def checkSum(A,l,r,x):
    
    
    pivot = findPivot(A,l,r)
    
    if pivot != -1:
        l = pivot
        r = pivot -1
        
        for i in range(0, len(A)):
            sum = A[l] + A[r]
            if sum == x:
                print(True)
                return True
            elif sum > x:
                r -= 1
            elif sum < x:
                l +=1
                if l == len(A):
                    l = 0
                    break 
    
    for i in range(0,len(A)):
        sum = A[l] + A[r]
        if sum == x:
            print(True)
            return True
        if l == r:
            print(False)
            return False
        if sum > x:
            r -= 1
        if sum < x:
            l +=1
    

array = [11, 15, 26, 38, 9, 10]
checkSum(array,0,6,45)
    