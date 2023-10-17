def majorityElement(A, N):
  #Your code here
  index = 0
  count = 1
  for i in range(N):
    if A[i] == A[index]:
      count+=1
    else:
      count -=1
      if count == 0:
        index = i
        count=1
       
  majCount = 0
  for i in range(N):
   if A[i] == A[index]:
      majCount+=1
    

  if majCount > N/2:
    return A[index]
            
  return -1
