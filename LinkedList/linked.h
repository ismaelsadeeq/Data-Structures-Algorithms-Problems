#ifndef _LINKED_H_
#define _LINKED_H_

/**
 * Built-in C libraries
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Structure for the singly linked list
 */
typedef struct linked 
{
	struct linked *next;
	int value;
} node_t;

/**
 * Structure for a doubly linked list
 */
typedef struct doubly
{
	int value;
	struct doubly *next;
	struct doubly *prev;
} node_d;

/**
 * Self written functions
 */
void print_linked_list(node_t *list);
node_t *create_linked_list(int *array, size_t length);
void free_linked_list(node_t *list);
void print_doubly_linked_list(node_d *node);
node_d *create_doubly_linked_list(int *array, size_t length);
void free_doubly_linked_list(node_d *node);
node_d *create_circularly_linked_list(int *array, size_t length);
void print_circularly_linked_list(node_d *node);
void free_circularly_linked_list(node_d *node);

#endif
