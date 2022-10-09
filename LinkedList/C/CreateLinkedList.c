#include "linked.h" 
/**
 * create_linked_list - Function to create a linked list
 * @array: An array containing the integers to be inputed in the list
 * @length: The size of the list
 * Return: Pointer to the created list
 */
node_t *create_linked_list(int *array, size_t length)
{
	node_t *old, *new;
	size_t size;

	new = malloc(sizeof(node_t) * length);

	if (!new || !array)
		return NULL;

	old = new;
	size = 0;

	if (!array || new == NULL)
		return new;

	while (size < length)
	{
		new -> value = array[size];
		if ((size + 1) < length)
		{
			new -> next = malloc(sizeof(node_t));
			new = new -> next;
		}
		size = size + 1;
	}

	new->next = NULL;
	return old;
}
/**
 * create_circularly_linked_list - Function to create a circularly linked list
 * @array: An array of integers
 * @length: Length of the array
 * Return: Pointer to the head of the array or NULL
 */
node_d *create_circularly_linked_list(int *array, size_t length)
{
	node_d *new, *old, *present;
	size_t size = 0;

	new = malloc(sizeof(node_d));

	if (!array || new == NULL)
		return NULL;

	old = new;
	while (size < length)
	{
		old -> value = array[size];
		size++;
		present = old;
		old -> next = malloc(sizeof(node_d));
		old = old -> next;
		old -> prev = present;
		present->next = old;
	}
	old -> next = new;
	new -> prev = old;
	return (new);
}
/**
 * create_doubly_linked_list - Function to create a doubly linked list
 * @array: An array of integers
 * @length: Length of the array of integers
 * Return: Pointer to the head of the newly created linked list
 */
node_d *create_doubly_linked_list(int *array, size_t length)
{
	node_d *past, *present, *future;
	size_t size = 0, place;
	
	future = malloc(sizeof(node_d) * length);

	if (!future || !array)
		return NULL;

	past = future;
	while (size < length)
	{
		place = size;
		size++;
		past->value = array[place];
		present = past;
		past->next = malloc(sizeof(node_d) * length);
		past = past->next;
		if (size == 0)
		{
			past->prev = NULL;
		}
		else
		{
			past->prev = present;
			present->next = past;
		}
	}
	past->next = NULL;
	return future;
}
