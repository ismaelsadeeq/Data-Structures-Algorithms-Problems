/** 
 * ! Linear Search::
 * find element = 7
 * loop through array
 * if element array[i] == elemenet
 * return index
 * 
 * 
 */

linearSearch(List<int> arrays, findElement) {
  for (int i = 0; i < arrays.length; i++) {
    if (arrays[i] == findElement) {
      return i;
    }
  }
}
