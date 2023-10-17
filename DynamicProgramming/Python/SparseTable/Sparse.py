import math
def create_sparse(arr,n):
    
    
    sparse = [[]] * n
    
   
    
    for i in range(n):
        
        sparse[i] = [i]
    
    j = 1
    
    while(pow(2,j) < n):
        
        k = 0
        while (k + pow(2,j-1) < n and j - 1 < len(sparse[k + pow(2,j-1)]) ):
            first = sparse[k][j-1]
            inc = k + pow(2,j-1)
            second = sparse[inc][j-1]
            if arr[ first ] < arr[ second ]:
            	sparse[k].append(sparse[k][j-1])
            else:
            	sparse[k].append(sparse[inc][j-1])
            	
            k = k+1
            
        j = j+1


    return sparse

def rmq(low,high,sparse):
    
    l = (high-low) +1
    k = math.floor(math.log2(l))
    firstElement = arr[sparse[low][k]]
    secondElement = arr[sparse[low + (l - pow(2,k))][k]]
    
    return min(firstElement,secondElement)
    
    
    
# arr = [4,6,1,5,7,3]
# n =  len(arr)
# sparse = create_sparse(arr,n)
# print(rmq(3,5,sparse))
# print(rmq(0,5,sparse))
# print(rmq(0,3,sparse))



    
arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]

n = len(arr)
sparse = create_sparse(arr,n)
print(rmq(0,4,sparse))
print(rmq(4,7,sparse))
print(rmq(7,8,sparse))