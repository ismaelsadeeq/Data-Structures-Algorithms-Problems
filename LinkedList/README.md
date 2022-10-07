# Linked Lists
A Linked list is a data stucture in which data are collected linearly through the nodes.

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

## Note
All allocated blocks were freed and there is no possibility of a leak. The confirmation was verified from valgrind
