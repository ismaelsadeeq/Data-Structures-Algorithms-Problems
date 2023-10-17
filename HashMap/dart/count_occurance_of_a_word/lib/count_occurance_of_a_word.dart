import 'dart:collection';

/***
 * The purpose is to use hashmap and count the number of times a word appears in a phrase also called word frequency
 * for example:
 * 1. hello world::
 * hello: 1
 * world: 1
 * 2. the cat ate the dog
 * the: 2
 * cat: 1
 * ate: 1
 * dog: 1
 * 
 * Using HashMap to store the words and count the numbers
 * first we need to tokenize the phrase
 * 
 * method should take the sentence and return a hashmap
 */

Map<String, int> hashmap(String sentence) {
  final Map<String, int> map = HashMap();
  List<String> tokenize = sentence.split(" ");
  for (int i = 0; i < tokenize.length; i++) {
    String word = tokenize[i].toLowerCase();
    print("word $word");
    if (map.containsKey(word)) {
      int count = map[tokenize[i]] ?? 0;
      var data = <String, int>{word: count + 1};
      map.addAll(data);
    } else {
      var data = <String, int>{word: 1};
      map.addAll(data);
    }
  }
  return map;
}
