int binary_search(List<int> array, int findNumber, int low, int high) {
  while (low <= high) {
    double middle = (low + (high - low) / 2);
    int mid = middle.toInt();
    if (findNumber == array[mid]) {
      return mid;
    } else if (findNumber >= array[mid]) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
