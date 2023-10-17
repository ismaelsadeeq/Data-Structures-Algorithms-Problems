int interpolationSearch(List arr, int n, int key) {
  int low = 0, high = n - 1;
  while (low <= high && key >= arr[low] && key <= arr[high]) {
    /* Calculate the nearest possible position of key */
    int pos = low +
        (((key - arr[low]) * (high - low)) / (arr[high] - arr[low])).round();
    if (key > arr[pos])
      low = pos + 1;
    else if (key < arr[pos])
      high = pos - 1;
    else /* Found */
      return pos;
  }
  /* Not found */
  return -1;
}

int main() {
  List arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  var n = arr.length;
  var key = 5;
  print("I want to found $key at $arr");
  var index = interpolationSearch(arr, n, key);
  print("Element found at position: $index");
  return 0;
}
