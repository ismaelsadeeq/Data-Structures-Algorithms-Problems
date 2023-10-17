import math

def sherlockInversion(arr,queries):

  answer = [0] * len(queries)

  queries = list(enumerate(queries))
  n = int(math.sqrt(len(arr))) + 1 
  queries.sort(key=lambda a:[int(a[1][0]/n), -a[1][1]])

  currentL = queries[0][1][0]-1
  currentR = queries[0][1][0]-2
  inversions = []

  for q in queries:
    left = q[1][0]-1
    right = q[1][1]-1

    while(currentR < right):
      currentR+=1
      inversions = incrementR(arr,currentL,currentR,inversions)

    while(currentL < left):
      inversions = decrementL(arr,currentL,inversions)
      currentL+=1

    while(currentR > right):
      inversions = decrementR(arr,currentR,inversions)
      currentR-=1

    while(currentL > left):
      inversions = incrementL(arr,currentL,currentR,inversions)
      currentL-=1
    
    answer[q[0]] = len(inversions)

  return answer


def incrementR(arr,l,r,inv):
  inversions = inv

  for i in range(len(arr[l:r])):
    if arr[i] > arr[r]:
      inversions.append((arr[i],arr[r]))
  return inversions

def incrementL(arr,l,r,inv):
  inversions = inv
  for i in range(len(arr[l+1,r+1])):
    if arr[l] > arr[i]:
      inversions.append((arr[l],arr[i]))
  
  return inversions

def decrementL(arr,l,inversions):
  return list(filter(lambda x:x[0] != arr[l],inversions))

def decrementR(arr,r,inversions):
  return list(filter(lambda x:x[1] != arr[r],inversions))


arr = [7, 9, 3, 5, 1, 6, 4]
q = [[1, 4], [3, 5], [1, 2], [1, 7]]

print(sherlockInversion(arr=arr,queries=q))




      
