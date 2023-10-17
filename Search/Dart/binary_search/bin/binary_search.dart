import 'package:binary_search/binary_search.dart' as binary_search;

void main(List<String> arguments) {
  List<int> array = [3, 4, 5, 6, 7, 8, 9];
  int findNumber = 4;
  int low = 0;
  int high = array.length - 1;

  int results = binary_search.binary_search(array, findNumber, low, high);
  print("returning $results");
}
