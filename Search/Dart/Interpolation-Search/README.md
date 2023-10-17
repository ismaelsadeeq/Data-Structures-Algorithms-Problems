# INTERPOLATION SEARCH
📌 **Time Complexity**: `O(log(log(n)))`
📌 **Space Complexity**: `O(1)`
📌 **Path:** Data-Structures-Algorithms-Problems/Array/Dart/Interpolation-Search/InterpolationSearch.dart

## Interpolation Search
The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

## ⚡ Code
```dart
int interpolationSearch(List arr, int n, int key) {
  int low = 0, high = n - 1;
  while (low <= high && key >= arr[low] && key <= arr[high]) {
    int pos = low +
        (((key - arr[low]) * (high - low)) / (arr[high] - arr[low])).round();
    if (key > arr[pos])
      low = pos + 1;
    else if (key < arr[pos])
      high = pos - 1;
    else 
      return pos;
  }
  return -1;
}
```
## 💡Examples
```Dart
List arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
var n = arr.length;
var key = 5;
interpolationSearch(arr, n, key); // returns 5
```
