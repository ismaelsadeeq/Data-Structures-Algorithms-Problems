#include "linked.h" 
/**
 * print_linked_list - Function to print contents of the linked list
 * @list: Pointer to the head of the linked list
 * Return: No return
 */
void print_linked_list(node_t *list)
{
	int num = 0;

	if (!list)
		return ;

	while (list != NULL)
	{
		printf("The %d value is %d\n", num, list->value);
		num = num + 1;
		list = list -> next;
	}
}
/**
 * print_circularly_linked_list - Function to print the values in the
 * circularly linked list
 * @head: Pointer to the head of the circularly linked list
 * Return: No return
 */
void print_circularly_linked_list(node_d *head)
{
	node_d *old;
	size_t num = 0;

	if (!head)
		return ;

	old = head;
	while (old -> next != head)
	{
		printf("The %ld value in the circularly linked ", num);
		printf("list is %d\n", old->value);
		num++;
		old = old->next;
	}
}
/**
 * print_doubly_linked_list - Function to print the doubly linked list
 * @node: Pointer to the head node of the doubly linked list
 * Return: No return
 */
void print_doubly_linked_list(node_d *node)
{
	node_d *path;
	size_t num = 0;

	if (!node)
		return ;

	path = node;
	while(path->next != NULL)
	{
		printf("The %ld value in the doubly linked list is %d\n", num, path->value);
		num++;
		path = path->next;
	}
}
