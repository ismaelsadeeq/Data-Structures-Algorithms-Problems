#ifndef STACK
#define STACK

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
    int top;
    unsigned capacity;
    int *array;
};

Stack *createStack(unsigned capacity);
int isFull(Stack *stack);
int isEmpty(Stack *stack);
void push(Stack *stack, int item);
int pop(Stack *stack);
int peek(Stack *stack);

#endif
