def findSumOfIndex(arr,Q):

  sum = 0
  for i in range(len(arr)):
    sum+=arr[i]
    arr[i] = sum

  print(arr)
  ans = []
  for i in range(len(Q)):
    l = Q[i][0]-1
    r = Q[i][1]-1
    if l > 0:
      ans.append(arr[r] - arr[(l-1)])
    else:
      ans.append(arr[r])

  return ans

arr = [3, 6, 2, 8, 9, 2]
Q = [[2, 3], [4, 6], [1, 5], [3, 6]]
print(findSumOfIndex(arr,Q))