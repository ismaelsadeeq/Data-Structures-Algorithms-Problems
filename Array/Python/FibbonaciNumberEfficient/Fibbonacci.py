
def findFib(n):

  if n < 0:
    return -1

  previousFib = 0
  currentFib = 1

  for i in range(n-1):

    newFib = previousFib + currentFib
    previousFib = currentFib
    currentFib = newFib

  return currentFib
