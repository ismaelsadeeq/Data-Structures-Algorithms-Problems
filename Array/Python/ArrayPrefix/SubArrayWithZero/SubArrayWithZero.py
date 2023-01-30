def subArrayWithZero(arr):

  prefixSum = arr[0]
  prefixMap = {}
  prefixMap[prefixSum] = 1

  for i in range(1, len(arr)):
    prefixSum +=arr[i]
    if prefixMap.get(prefixSum) == 1:
      return True
    
    if prefixSum == 0:
      return True
    
    prefixMap[prefixSum] = 1
  

  return False

arr = [-3, 2, 3, 1, 6]
print(subArrayWithZero(arr))