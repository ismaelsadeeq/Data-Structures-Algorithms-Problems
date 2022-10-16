# Binary Search algorithm implementation in C

Time complexity - O( Log(n) )
Space Complexity - O(1)

## Implementation of `BinarySearch`

The `BinarySearch` function requires to pass an array of numbers and the number to be found in the array with the lowest possible index and the highest possible index.

It returns the index of the number you searched for if it has found the number or else it returns -1.

```c
BinarySearch(int arr[], int x, int low, int high)
```

## How to run the program

This folder contains the header you can include when compiling your program. You will need to create a C/C++ file with a main function.

Here is how you can do it:

- Create a new c/c++ file

```bash
touch main.c
```

- Include "BinarySearch.h" in your file

```c
#include "BinarySearch.h"
```

- Write a main function

```c

#include "BinarySearch.h"

int main() {
    int nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    int num  = BinarySearch(nums, 0, 5, 10 - 1);

    printf("result: %d", num);

    return 0;
}
```

- Compile and run
  You can use your preferred compiler :D

```bash
clang main.c -o binary_search
./binary_search
```

By running the program, now you can see the result printed as the index of the number in the array.
