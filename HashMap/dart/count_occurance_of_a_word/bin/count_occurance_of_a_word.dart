import 'package:count_occurance_of_a_word/count_occurance_of_a_word.dart'
    as hashmap;

void main(List<String> arguments) {
  String sentence = "The cat ate the dog";
  Map<String, int> results = hashmap.hashmap(sentence);
  print("results $results");
}
