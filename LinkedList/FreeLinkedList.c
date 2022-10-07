#include "linked.h" 
/**
 * free_linked_list - Function that clears the memory space
 * consumed by the program
 *
 * Return: No return
 */
void free_linked_list(node_t *list)
{
	node_t *new;

	if (!list)
		return ;

	while (list != NULL)
	{
		new = list;
		list = list->next;
		free(new);
	}
}
/**
 * free_circularly_linked_list - Function to free the allocated space in the
 * circularly linked list
 * @head: Pointer to the head node of the singly linked list
 * Return: No return
 */
void free_circularly_linked_list(node_d *head)
{
	node_d *new;

	if (!head)
		return ;

	new = head;
	new->prev->next = NULL;
	while (new -> next != NULL)
	{
		new = new->next;
		free(new->prev);
	}
	free(new);
}
/**
 * free_doubly_linked_list - Function to free the space occupied by the doubly
 * doubly linked list
 * @node: Pointer to the head of the doubly linked list
 * Return: No return
 */
void free_doubly_linked_list(node_d *node)
{
	node_d *old;

	if (!node)
		return ;

	while (node != NULL)
	{
		old = node;
		node = node->next;
		free(old);
	}
}
