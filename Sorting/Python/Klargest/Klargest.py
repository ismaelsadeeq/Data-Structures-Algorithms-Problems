def findKLargest(arr,k):

  arr.sort()
  ans = []
  n = len(arr)
  while(k!=0):
    ans.append(arr[n-1])
    n-=1
    k-=1
  
  return ans


print(findKLargest([1, 23, 12, 9, 30, 2, 50],3))
print(findKLargest([11, 5, 12, 9, 44, 17, 2],2))
