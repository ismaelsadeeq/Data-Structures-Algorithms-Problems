def findPrefix(arr):
  sum = 0
  for i in range(len(arr)):
    sum += arr[i]
    arr[i] = sum
  return arr

arr = [10, 20, 10, 5, 15]

print(findPrefix(arr))