import math


def powerFulArray(nums, query):


  n = int(math.sqrt(len(nums))) + 1

  answer = [0] * len(query)

  q = list(enumerate(query))

  q.sort(key=lambda a:[int(a[1][0]/n),-a[1][1]])

  F = [0] * (max(nums) +1)

  currentL = q[0][1][0]-1
  currentR = q[0][1][0]-2

  count = 0

 
  for i in q:
    left = i[1][0]-1
    right = i[1][1] -1

    while(currentR < right):
      currentR+=1
      if F[nums[currentR]] > 0:
        count-= (F[nums[currentR]] ** 2 ) * nums[currentR]
      F[nums[currentR]]+=1
      count+= (F[nums[currentR]] ** 2 ) * nums[currentR]
    
    while(currentL < left):
      count-= (F[nums[currentL]] ** 2 ) * nums[currentL]
      F[nums[currentL]]-=1
      count+= (F[nums[currentL]]**2) * nums[currentL]
      currentL+=1
    
    while(currentR > right):
      count-= (F[nums[currentR]] **2) * nums[currentR]
      F[nums[currentR]]-=1
      count+= (F[nums[currentR]]**2) * nums[currentR]
      currentR-=1

    while(currentL > left):
      if F[nums[currentL]] > 0:
        count-= (F[nums[currentL]]**2) * nums[currentL]
      F[nums[currentL]]+=1
      count+= (F[nums[currentL]]**2) * nums[currentL]
      currentL-=1

    answer[i[0]] = count

  return answer



# nums = [1, 2, 1]
# q = [[1,2],[1,3]]


nums = [1 ,1, 2, 2, 1, 3, 1, 1]
q = [[2,7],[1,6],[2,7]]

print(powerFulArray(nums,q))

      


