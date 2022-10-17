import 'package:linear_search/linear_search.dart';
import 'package:test/test.dart';

void main() {
  test('linearSearch', () {
    List<int> arrays = [9, 1, 8, 2, 7, 3, 6, 4, 5];
    int findElement = 7;
    expect(linearSearch(arrays, findElement), 4);
  });
}
