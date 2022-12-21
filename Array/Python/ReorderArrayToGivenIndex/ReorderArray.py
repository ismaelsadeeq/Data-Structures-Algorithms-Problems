def reOrder(arr,index,n):
    
    
    for i in range(0,n):
        
        while (index[i] != i):
            
            
            oldValue = arr[index[i]]
            
            oldTarget = index[index[i]]
            
            
            arr[index[i]] = arr[i]
            index[index[i]] = index[i]
            
            
            arr[i] = oldValue
            index[i] = oldTarget
            
    return arr
            