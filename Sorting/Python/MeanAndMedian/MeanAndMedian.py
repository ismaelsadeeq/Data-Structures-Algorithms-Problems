def findMeanAndMedian(arr):
  n = len(arr)
  arr.sort()
  mean = sum(arr) / n
  arr.sort()
  median = 0
  if n % 2 != 0:
    median = arr[n//2]
  else:
    median = (arr[int(n/2)] + arr[int((n/2)-1)]) / 2

  return [mean,median]



arr = [1, 3, 4, 2, 6, 5, 8, 7]

print(findMeanAndMedian(arr))



