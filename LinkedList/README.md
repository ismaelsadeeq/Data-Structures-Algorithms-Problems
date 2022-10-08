# Linked Lists
A Linked list is a data stucture in which data are collected linearly through the nodes. To know more about a linked list, check out this [article](https://medium.com/@dilibe/getting-started-with-linked-list-fdf4da268ff9)

# How to run the program
No C program can run with out the main function. 
The GCC (which is what we will be using) will show an error without the main function.
Create your main function to test this. 
Replace it with the section `<main_file>`in the command. 
The linked list accept integers as data inputs.
You can add as much flags or options as you want.
Take a look at the `linked.h` header file to see the prototype to use

### Singly Linked List

```
gcc -Wall -Wextra -Werror -pedantic -std=gnu89 <main_file> PrintLinkedList.c FreeLinkedList.c CreateLinkedList.c -o <name_you_want>
```

### Doubly Linked List

```
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 <main_file> PrintLinkedList.c FreeLinkedList.c CreateLinkedList.c -o <name_you_want>
```

### Circularly Linked List

```
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 <main_file> PrintLinkedList.c FreeLinkedList.c CreateLinkedList.c -o <name_you_want>
```

# How to create the `main_file`

Before a C program is complied, It must contain only one main function.
To create the main file which contains the main function, follow the steps
- The first line must contain `#include "linked.h"`
- After this, other libraries can be declared
- The main function can also be declared. The main function is a very essential part in C programming.
- Prototypes that care included in `linked.h` file can be used as function calls in the main function

[Take a look at my functions to get a clue](https://github.com/Ddilibe/Data-Structures-Algorithms-Problems_ismaelsadeeq/tree/linked/LinkedList/C)

## Note
All allocated blocks were freed and there is no possibility of a leak. The confirmation was verified from valgrind
