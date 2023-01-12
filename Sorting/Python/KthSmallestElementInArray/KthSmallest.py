def findKLargest(arr,k):

  arr.sort()
  
  return arr[k-1]


print(findKLargest([7, 10, 4, 3, 20, 15],3))
print(findKLargest([7, 10, 4, 3, 20, 15],4))
