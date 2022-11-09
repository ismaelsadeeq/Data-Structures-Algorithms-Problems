from LeftRotation import findGcd
from LeftRotation import rotate


def test_gcd():
  assert findGcd(0,6) == 6
  assert findGcd(2,3) == 1
  assert findGcd(3,6) == 3



def test_positive_integers_rotation():
  arr = [1,2,3,4,5,6]
  pivot = 2
  result = [3,4,5,6,1,2]
  rotate(arr,pivot)
  assert  arr == result

def test_negative_integers_rotation():
  arr = [-1,-2,-3,-4,-5,-6]
  pivot = 2
  result = [-3,-4,-5,-6,-1,-2]
  rotate(arr,pivot)
  assert  arr == result


def test_single_item_rotation():
  arr = [6]
  pivot = 2
  result = [6]
  rotate(arr,pivot)
  assert  arr == result
  
def test_empty_array_rotation():
  arr = []
  pivot = 2
  result = []
  rotate(arr,pivot)
  assert  arr == result


