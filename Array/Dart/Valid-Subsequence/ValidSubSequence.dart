// Valid subsequence algorithm in Dart
bool isValidSubsequence<T>(
    {required List<T> array, required List<T> sequence}) {
  int arrayIndex = 0, sequenceIndex = 0;
  while (arrayIndex < array.length && sequenceIndex < sequence.length) {
    if (array[arrayIndex] == sequence[sequenceIndex]) sequenceIndex++;
    arrayIndex++;
  }
  return sequenceIndex == sequence.length;
}

int main() {
  print("🚩 Testing `isValidSubsequence` function...");
  List<int> firstArray = [5, 1, 22, 25, 6, -1, 8, 10],
      firstSequence = [1, 6, -1, 10];
  List<String> secondArray = [
        "alpha",
        "beta",
        "gamma",
        "delta",
        "tau",
        "psi",
        "omega"
      ],
      secondSequence = ["alpha", "kappa", "phi"];
  print("🔖ARRAY → ${firstArray} 📍SEQUENCE → ${firstSequence}");
  print(
      "ISVALIDSUBSEQUENCE 👉 ${isValidSubsequence<int>(array: firstArray, sequence: firstSequence)}");
  print("⦿⦿⦿⦿⦿⦿⦿⦿⦿⦿⦿⦿⦿⦿⦿");
  print("🔖ARRAY → ${secondArray} 📍SEQUENCE → ${secondSequence}");
  print(
      "ISVALIDSUBSEQUENCE 👉 ${isValidSubsequence<String>(array: secondArray, sequence: secondSequence)}");

  return 0;
}
