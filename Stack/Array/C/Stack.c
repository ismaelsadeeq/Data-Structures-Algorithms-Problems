#include "Stack.h"

/**
 * createStack - creates stack of given capacity
 * @capacity: capacity of the stack
 * Return: returns pointer to new stack otherwise NULL 
 */ 
Stack *createStack(unsigned capacity)
{
    Stack *stack = malloc(sizeof(Stack));
    if (stack == NULL)
	    return NULL;
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = malloc(stack->capacity * sizeof(int));
    return stack;
}

/**
 * isFull - check if stack is full
 * @stack: pointer to the stack to check
 * Return: returns true if stack is full otherwise false
 */ 
int isFull(Stack *stack)
{
    return stack->top == stack->capacity - 1;
}

/**
 * isEmpty - check if stack is empty
 * @stack: pointer to the stack to check
 * Return: returns true if stack is empty otherwise false
 */
int isEmpty(Stack *stack)
{
    return stack->top == -1;
}

/**
 * push - add an item to the top of the stack
 * @stack: pointer to the stack to check
 * @item: item to add
 */
void push(Stack *stack, int item)
{
    if (isFull(stack))
        return;
    stack->array[++stack->top] = item;
    printf("%d pushed to stack\n", item);
}

/**
 * pop - removes the top item
 * @stack: pointer to the stack to check
 * Return: returns the removed item or 
 * minimum int value if stack is empty
 */
int pop(Stack *stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top--];
}

/**
 * peek - returns top item without removing it
 * @stack: pointer to the stack to check
 * Return: returns the top  item or
 * minimum int value if stack is empty
 */
int peek(Stack *stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top];
}
