# MOORE'S VOTING ALGORIGHM
📌 **Time Complexity:** O(n) <br>
📌 **Space Complexity:** O(1) <br>
📌 **Path:** Data-Structures-Algorithms-Problems/Array/Dart/Moore-Voting-Algorithm/MooreVotingAlgorithm.dart

## What is majorityElement Algorithm?

The Boyer-Moore``majorityElement`` method is a popular optimal technique for determining the majority element among provided array items with more than N/ 2 occurrences.

## How does it work?
``majorityElement`` in an array ``mooreArray`` of size n is an element that appears more than n/2 times (and hence there is at most one such element).


## ⚡ Code
```dart
int majorityElement(List<int> array, int n) {
  array.sort();
  var count = 1, max = -1, temporary = array[0], ele = 0, f = 0;
  for (int i = 1; i < n; i++) {
    if (temporary == array[i]) {
      count++;
    } else {
      count = 1;
      temporary = array[i];
    }
    if (max < count) {
      max = count;
      ele = array[i];
      if (max > (n / 2)) {
        f = 1;
        break;
      }
    }
  }
  return (f == 1 ? ele : -1);
}
```
## 💡Example
```Dart
List<int> arr = [1, 1, 2, 1, 3, 5, 1];
int n = arr.length;
majorityElement(arr, n); // returns 1    
