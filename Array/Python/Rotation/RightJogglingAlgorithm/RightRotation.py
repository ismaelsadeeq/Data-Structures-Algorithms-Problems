def rotate(arr,r):
  n = len(arr)

  gcd = findGcd(n,r)

  r = n-r
  for i in range(0,gcd):
    temp = arr[n-i-1]
    j = n - i - 1
    while True:
      k = (j + r) % n
      if k == (n - i -1):
        break
      arr[j] = arr[k]
      j = k
    arr[j] = temp 


def findGcd(a,b):
  if b == 0:
    return a
  else:
    return findGcd(b,a%b)