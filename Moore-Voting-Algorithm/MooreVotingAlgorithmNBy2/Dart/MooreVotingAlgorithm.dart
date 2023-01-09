// Moore's Voting Algorithm Implementation in Dart
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

void main() {
  List<int> arr = [1, 1, 2, 1, 3, 5, 1];
  int n = arr.length;
  print(
    majorityElement(arr, n),
  );
}
