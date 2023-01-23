def maxSubArray(arr):

  maxSum = arr[0]
  currSum = 0

  for n in arr:
    if currSum < 0:
      currSum = 0
    currSum += n
    maxSum = max(maxSum,currSum)

  return maxSum

arr = [4, -8, 9, -4, 1, -8, -1, 6]
print(maxSubArray(arr))