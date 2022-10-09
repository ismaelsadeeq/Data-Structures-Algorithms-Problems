#include "linked.h"

/**
 * delete_last_node_singly_linked_list - Function to delete the last node in
 * a singly linked list
 * @node: Pointer to the head node of the linked list
 * Return: Pointer to the head node after deletion or NULL
 */
node_t *delete_last_node_singly_linked_list(node_t *new_node)
{
	node_t *current, *new_end;
	
	if (!new_node)
		return (NULL);

	current = new_node;
	while (current->next)
	{
		new_end = current;
		current = current->next;
	}
	new_end->next = NULL;
	free(current);
	return (new_node);
}
/**
 * delete_last_node_doubly_linked_list - Function to delete the last node from
 * a singly linked list
 * @node: Pointer to the head of the doubly linked list
 * Return: Pointer to the head of a doubly linked list or NULL
 */
node_d *delete_last_node_doubly_linked_list(node_d *new_node)
{
	node_d *current, *present;
	
	if (!new_node)
		return (NULL);

	current = new_node;
	while (current->next)
	{
		present = current;
		current = current->next;
	}
	present -> next = NULL;
	current -> prev = NULL;
	free(current);
	return (new_node);
}
/**
 * delete_last_node_circularly_linked_list - Function to delete the last node in
 * a circularly linked list
 * @new_node: Pointer to the head of the circularly linked list
 * Return: pointer to the head of the circularly linked list
 */
node_d *delete_last_node_circularly_linked_list(node_d *new_node)
{
	node_d *current, *present;

	if (!new_node)
		return (NULL);

	current = new_node;
	while (current->next != new_node)
	{
		present = current;
		current = current->next;
	}
	free(current);
	present->next = new_node;
	new_node->prev = present;
	return (new_node);
}
