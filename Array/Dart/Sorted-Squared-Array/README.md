# SORTED SQUARED ARRAY
📌 **Time complexity:** O(n)
📌 **Space complexity:** O(n)
📌 **Path:** Data-Structures-Algorithms-Problems/Array/Dart/Sorted-Squared-Array/SortedSquaredArray.dart

## Sorted Squared array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## How does it work?
Given an array of integers that are sorted in increasing order, the```Sorted Squared array``` squares all the integers in the array and returns them in a new array, also sorted in increasing order.

## ⚡ Code
```dart
List<int> sortedSquaredarray(List<int> arr) {
  int start = 0, end = arr.length - 1;
  int sortedIndex = arr.length - 1;
  List<int> answer = List.filled(arr.length, 0);

  while (end >= start) {
    if (arr[start].abs() > arr[end].abs()) {
      answer[sortedIndex] = arr[start] * arr[start];
      start += 1;
    } else {
      answer[sortedIndex] = arr[end] * arr[end];
      end -= 1;
    }
    sortedIndex -= 1;
  }

  return answer;
}
```
## 💡Examples
```Dart
sortedSquaredarray([-1, -1, 2, 3, 3, 3, 4])); // returns [1, 1, 4, 9, 9, 9, 16]);
sortedSquaredarray([1, 2, 3, 4, 5, 6, 7]); // returns [1, 4, 9, 16, 25, 36, 49]);
```
