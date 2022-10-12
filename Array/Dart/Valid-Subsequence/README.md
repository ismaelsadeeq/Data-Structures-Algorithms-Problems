# VALID SUBSEQUENCE ALGORIGHM

📌 **Time Complexity:** O(n) <br>
📌 **Space Complexity:** O(1) <br>
📌 **Path:** Data-Structures-Algorithms-Problems/Array/Dart/Valid-Subsequence/ValidSubSequence.dart

## What is ValidSubSequence Algorithm?

``ValidSubSequence`` Algorithm is a algorithm to check if a sequence is valid or not in an array
## How does it work?

``ValidSubSequence`` Algorithm takes two parameters first one is the array and the second one is the sequence and it returns a boolean value
## ⚡ Code
```dart
bool isValidSubsequence<T>(
    {required List<T> array, required List<T> sequence}) {
  int arrayIndex = 0, sequenceIndex = 0;
  while (arrayIndex < array.length && sequenceIndex < sequence.length) {
    if (array[arrayIndex] == sequence[sequenceIndex]) sequenceIndex++;
    arrayIndex++;
  }
  return sequenceIndex == sequence.length;
}
```
## 💡Examples
```Dart
List<int> arrayA = [5,1,22,25,6,-1,8,10] 
List<int> sequenceA = [1,6,-1,10]
isValidSubSequence<int>(arrayA,sequenceA) // returns true
List<String> arrayB = ["alpha","beta","gamma","delta","tau","psi","omega"]
List<String> sequenceB = ["alpha","kappa","phi"]
isValidSubSequence<String>(array,sequence) // returns false
```
