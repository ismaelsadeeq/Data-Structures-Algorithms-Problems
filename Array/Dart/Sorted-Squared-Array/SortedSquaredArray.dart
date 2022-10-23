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

void main() {
  print(
      sortedSquaredarray([-1, -1, 2, 3, 3, 3, 4])); // [1, 1, 4, 9, 9, 9, 16]);

  print(
      sortedSquaredarray([1, 2, 3, 4, 5, 6, 7])); // [1, 4, 9, 16, 25, 36, 49]);
}
