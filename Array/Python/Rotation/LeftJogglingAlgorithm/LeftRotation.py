def rotate(arr,r):
  n = len(arr)
  if n == 0:
    return
  gcd = findGcd(n,r)

  for i in range(0,gcd):
    temp = arr[i]
    j = i
    while True:
      k = (j+r) % n
      if k == i:
        break
      arr[j] =  arr[k]
      j = k
    arr[j] = temp 



def findGcd(a,b):
  if b == 0:
    return a
  else:
    return findGcd(b,a%b)