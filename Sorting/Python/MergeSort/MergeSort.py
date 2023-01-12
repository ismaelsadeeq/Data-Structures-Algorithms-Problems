def mergeSort(arr):
  n = len(arr)
  if(n>1):
    mid = n//2
    L = arr[:mid]
    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)

    i=j=k=0
    while(i<len(L) and j<len(R)):
      if L[i] <= R[j]:
        arr[k] = L[i]
        i+=1
      else:
        arr[k] = R[j]
        j+=1
      k+=1
      
    while(i< len(L)):
      arr[k] = L[i]
      i+=1
      k+=1
    
    while(j<len(R)):
      arr[k] = R[j]
      j+=1
      k+=1
    
arr = [1,2,3,4,1,2,2,1,4,1]

mergeSort(arr)
print(arr)