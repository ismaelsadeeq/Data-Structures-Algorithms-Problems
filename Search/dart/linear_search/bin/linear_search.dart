import 'package:linear_search/linear_search.dart' as linear_search;

void main(List<String> arguments) {
  List<int> arrays = [9, 1, 8, 2, 7, 3, 6, 4, 5];
  int findElement = 7;
  int results = linear_search.linearSearch(arrays, findElement);
  print("results $results");
}
